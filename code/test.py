import tkinter as tk
import math

class Room3D:
    def __init__(self, root):
        self.root = root
        self.root.title("Căn phòng 3D - Vanilla Python (Tkinter + Math)")
        self.width = 900
        self.height = 650
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#181824")
        self.canvas.pack(fill="both", expand=True)

        # Góc nhìn camera và vị trí
        self.yaw = 0.0          # Xoay trái/phải
        self.pitch = 0.15       # Nhìn lên/xuống
        self.cam_dist = 8.5     # Khoảng cách camera (Zoom)

        self.last_mouse_x = 0
        self.last_mouse_y = 0

        # Danh sách các mặt phẳng (faces) tạo nên căn phòng và đồ vật
        # Định dạng mỗi mặt: (danh_sách_đỉnh_3D, màu_tô, màu_viền)
        self.faces = []
        self.build_scene()

        # Gán sự kiện chuột và bàn phím
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.root.bind("<Left>", lambda e: self.rotate(yaw=-0.08))
        self.root.bind("<Right>", lambda e: self.rotate(yaw=0.08))
        self.root.bind("<Up>", lambda e: self.rotate(pitch=-0.08))
        self.root.bind("<Down>", lambda e: self.rotate(pitch=0.08))

        self.render()

    def add_box(self, x, y, z, dx, dy, dz, color, outline="#1e1e1e"):
        """Hàm hỗ trợ tạo một khối hộp 3D từ tọa độ góc (x, y, z) và kích thước (dx, dy, dz)"""
        v = [
            (x, y, z), (x+dx, y, z), (x+dx, y+dy, z), (x, y+dy, z),
            (x, y, z+dz), (x+dx, y, z+dz), (x+dx, y+dy, z+dz), (x, y+dy, z+dz)
        ]
        box_faces = [
            [v[0], v[1], v[2], v[3]], # Mặt sau
            [v[4], v[5], v[6], v[7]], # Mặt trước
            [v[0], v[1], v[5], v[4]], # Mặt đáy
            [v[2], v[3], v[7], v[6]], # Mặt trên
            [v[0], v[3], v[7], v[4]], # Mặt trái
            [v[1], v[2], v[6], v[5]]  # Mặt phải
        ]
        for f in box_faces:
            self.faces.append((f, color, outline))

    def build_scene(self):
        """Thiết kế cấu trúc căn phòng và nội thất"""
        # Hệ tọa độ: X (ngang: -3 đến 3), Y (cao: -2 đến 2), Z (sâu: -3 đến 3)
        
        # 1. Sàn nhà, Vách tường sau và Tường trái
        self.faces.append(([(-3, -2, -3), (3, -2, -3), (3, -2, 3), (-3, -2, 3)], "#c89d7c", "#8a6448")) # Sàn gỗ
        self.faces.append(([(-3, -2, 3), (3, -2, 3), (3, 2, 3), (-3, 2, 3)], "#f2efe9", "#cccccc"))     # Tường sau
        self.faces.append(([(-3, -2, -3), (-3, -2, 3), (-3, 2, 3), (-3, 2, -3)], "#e5e0d8", "#cccccc")) # Tường trái

        # 2. Cửa sổ trên tường trái
        self.faces.append(([(-2.98, -0.5, -1.5), (-2.98, -0.5, 1.0), (-2.98, 1.2, 1.0), (-2.98, 1.2, -1.5)], "#87CEEB", "#4a3525"))

        # 3. Thảm trải sàn
        self.faces.append(([(-1.8, -1.98, -1.5), (1.8, -1.98, -1.5), (1.8, -1.98, 1.5), (-1.8, -1.98, 1.5)], "#d9d2c5", "#b5ae9e"))

        # 4. Kệ TV và TV (Sát tường sau Z = 3)
        self.add_box(-1.6, -2.0, 2.3, 3.2, 0.45, 0.6, "#a67b5b")   # Kệ gỗ
        self.add_box(-1.1, -1.3, 2.85, 2.2, 1.2, 0.08, "#141414")  # Màn hình TV

        # 5. Ghế Sofa (Hướng về phía TV)
        self.add_box(-1.3, -2.0, -1.2, 2.6, 0.4, 0.9, "#7d8471")   # Đệm ngồi
        self.add_box(-1.3, -1.6, -1.2, 2.6, 0.55, 0.25, "#686f5c") # Tựa lưng
        self.add_box(-1.5, -2.0, -1.2, 0.25, 0.65, 0.9, "#686f5c") # Tay vịn trái
        self.add_box(1.25, -2.0, -1.2, 0.25, 0.65, 0.9, "#686f5c") # Tay vịn phải

        # 6. Bàn trà ở giữa
        self.add_box(-0.7, -1.55, 0.3, 1.4, 0.08, 0.7, "#e6ccb2")  # Mặt bàn
        self.add_box(-0.6, -2.0, 0.4, 0.1, 0.45, 0.1, "#333333")   # Chân bàn 1
        self.add_box(0.5, -2.0, 0.4, 0.1, 0.45, 0.1, "#333333")    # Chân bàn 2
        self.add_box(-0.6, -2.0, 0.8, 0.1, 0.45, 0.1, "#333333")   # Chân bàn 3
        self.add_box(0.5, -2.0, 0.8, 0.1, 0.45, 0.1, "#333333")    # Chân bàn 4

        # 7. Tủ sách góc phải
        self.add_box(1.8, -2.0, 2.1, 0.9, 2.6, 0.8, "#8c6239")

        # 8. Chậu cây góc trái
        self.add_box(-2.6, -2.0, 2.1, 0.5, 0.5, 0.5, "#ffffff")    # Chậu trắng
        self.add_box(-2.55, -1.5, 2.15, 0.4, 0.9, 0.4, "#2d6a4f")  # Tán lá xanh

    def transform_vertex(self, x, y, z):
        """Xoay điểm 3D quanh trục Y (yaw) và trục X (pitch)"""
        # Xoay quanh trục Y
        cos_y, sin_y = math.cos(self.yaw), math.sin(self.yaw)
        x1 = x * cos_y - z * sin_y
        z1 = z * cos_y + x * sin_y

        # Xoay quanh trục X
        cos_p, sin_p = math.cos(self.pitch), math.sin(self.pitch)
        y2 = y * cos_p - z1 * sin_p
        z2 = z1 * cos_p + y * sin_p

        # Dịch chuyển ra xa camera
        z2 += self.cam_dist
        return x1, y2, z2

    def project(self, x, y, z):
        """Chiếu tọa độ 3D (x, y, z) lên màn hình 2D (screen_x, screen_y)"""
        fov = 650
        if z <= 0.1:
            z = 0.1
        sx = self.width / 2 + (x * fov) / z
        sy = self.height / 2 - (y * fov) / z # Trục Y của Tkinter hướng xuống
        return sx, sy

    def render(self):
        self.canvas.delete("all")
        rendered_faces = []

        for vertices, color, outline in self.faces:
            transformed = [self.transform_vertex(*v) for v in vertices]
            # Tính độ sâu trung bình (Z) của mặt phẳng để áp dụng Painter's Algorithm
            avg_z = sum(v[2] for v in transformed) / len(transformed)
            rendered_faces.append((avg_z, transformed, color, outline))

        # Sắp xếp các mặt từ xa đến gần (Z lớn vẽ trước, Z nhỏ vẽ đè lên sau)
        rendered_faces.sort(key=lambda item: item[0], reverse=True)

        for avg_z, transformed, color, outline in rendered_faces:
            if avg_z <= 0.5:
                continue
            polygon_2d = []
            for v in transformed:
                polygon_2d.extend(self.project(*v))
            self.canvas.create_polygon(polygon_2d, fill=color, outline=outline, width=1.5)

        # Hiển thị hướng dẫn điều khiển
        self.canvas.create_text(
            20, 20, anchor="nw", fill="#ffffff", font=("Segoe UI", 11, "bold"),
            text="🖱️ Kéo chuột trái / Phím mũi tên: Xoay góc nhìn 3D\n🔍 Con lăn chuột: Phóng to / Thu nhỏ"
        )

    def on_mouse_down(self, event):
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y

    def on_mouse_drag(self, event):
        dx = event.x - self.last_mouse_x
        dy = event.y - self.last_mouse_y
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y
        self.rotate(yaw=dx * 0.008, pitch=dy * 0.008)

    def on_mouse_wheel(self, event):
        self.cam_dist -= event.delta * 0.003
        self.cam_dist = max(4.0, min(18.0, self.cam_dist))
        self.render()

    def rotate(self, yaw=0.0, pitch=0.0):
        self.yaw += yaw
        self.pitch = max(-1.2, min(1.2, self.pitch + pitch))
        self.render()

if __name__ == "__main__":
    root = tk.Tk()
    app = Room3D(root)
    root.mainloop()
