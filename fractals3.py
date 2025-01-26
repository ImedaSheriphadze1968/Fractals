import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cv2
from PIL import Image
import io


# ჯულიას ნაკრების გენერაციის ფუნქცია
def julia_set(c, x_min=-1.5, x_max=1.5, y_min=-1.5, y_max=1.5, width=800, height=800, max_iter=256):
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=float)

    for i in range(max_iter):
        Z = Z ** 2 + c
        # დავამატოთ სითუმბე და ვამოწმებთ, რომ Z არ გახდეს არარელევანტური (NaN ან Infinity)
        mask = np.abs(Z) < 10  # მხოლოდ იმაზე ვსაუბრობთ, რაც ცოტა მეტია
        mask = mask & np.isfinite(Z)  # მხოლოდ ფინიტური მნიშვნელობები გამოიყენეთ
        img += mask

    img = np.log(img + 1)  # ფოტო დახატვა - რომ არ იყოს უსასრულო
    return img / img.max()  # ნორმალიზაცია


# ანიმაციის შექმნის ფუნქცია
def animate(julia_set_func, c_values, video_filename="julia_set_animation.mp4", duration=900, fps=30):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_filename, fourcc, fps, (800, 800))  # ვიდეოს გამოტანა

    num_frames = duration * fps  # გრაფიკის ხანგრძლივობა
    for frame in range(num_frames):
        t = frame / num_frames
        c_idx = int(t * len(c_values))
        c = c_values[c_idx % len(c_values)]  # ცვლის კოეფიციენტი
        img = julia_set_func(c)  # გენერირება ჯულიას ნაკრების გამოსახულება

        # ვიზუალიზაცია
        plt.imshow(img, cmap="twilight", origin="lower")
        plt.axis("off")
        plt.draw()
        plt.pause(1. / fps)

        # გამოსახულების გადაღება PIL-ის გამოყენებით
        buf = io.BytesIO()  # იმოგზაურეთ მეხსიერებაში
        plt.savefig(buf, format="png")  # PNG ფორმატში გადარჩენა
        buf.seek(0)
        pil_img = Image.open(buf)  # გამოსახულების გადაკითხვა PIL-ისთვის
        frame_img = np.array(pil_img)  # numpy array-ში გარდაქმნა
        frame_img = cv2.cvtColor(frame_img, cv2.COLOR_RGBA2BGR)  # RGBA -> BGR
        out.write(frame_img)  # ვიდეოში ჩადება
        plt.clf()  # გაწმენდა შემდეგი ფრაგმენტისათვის

    out.release()  # ვიდეო ფაილის დახურვა


# მთავარი ფუნქცია
if __name__ == "__main__":
    # კოეფიციენტები
    c_values = [
        complex(-1),
        complex(-0.2, 0.75),
        complex(-0.1244, 0.756),
        complex(-0.1194, 0.6289),
        complex(-0.7382, 0.0827),
        complex(0.377, -0.248)
    ]

    animate(julia_set, c_values)
