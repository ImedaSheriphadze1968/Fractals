import numpy as np
import matplotlib.pyplot as plt


# მანდელბროტის გენერაცია
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


# ჯულიას გენერაცია
def julia(c, z, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


# იწვის გემი ფრაქტალის გენერაცია
def burning_ship(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = complex(abs(z.real), abs(z.imag)) ** 2 + c
    return max_iter


# ფენიქსის ნაკრები-ის გენერაცია
def phoenix(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = (z * z + c) ** 2 + c
    return max_iter


# ტრირქა ფრაქტალის გენერაცია
def tricorn(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = np.conj(z) ** 2 + c
    return max_iter


# მანდალა გენერაცია
def mandala(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 10:
            return n
        z = z * z + c
    return max_iter


# სერპინსკის სამკუთხედი-ის გენერაცია
def sierpinski(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 1:
            return n
        z = z * z + c
    return max_iter


# ლაპლასიური ფრაქტალი-ის გენერაცია
def laplacian(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 3:
            return n
        z = z * z - c
    return max_iter


# კანტორის ნაკრები-ის გენერაცია
def cantor(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = np.abs(z) ** 2 + c
    return max_iter


# ბარნსლი ფერნი-ის გენერაცია
def barnsley_fern(c, max_iter):
    x, y = 0, 0
    for n in range(max_iter):
        r = np.random.rand()
        if r < 0.02:
            x, y = 0, 0.16 * y
        elif r < 0.17:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.3:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        c = complex(x, y)
        if abs(c) > 3:
            return n
    return max_iter


# ფრაქტალის გენერაცია (10 სხვადასხვა ტიპის)
def generate_fractal(width, height, x_min, x_max, y_min, y_max, max_iter, fractal_type, c=None):
    image = np.zeros((height, width))  # ქმნის ცარიელ სურათს
    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)  # რეალური ნაწილი
            imag = y_min + (y / height) * (y_max - y_min)  # მმომავალი ნაწილი
            z = complex(real, imag)
            if fractal_type == 'mandelbrot':
                image[y, x] = mandelbrot(z, max_iter)
            elif fractal_type == 'julia' and c is not None:  # მხოლოდ ჯულიას შემთხვევაში
                image[y, x] = julia(c, z, max_iter)
            elif fractal_type == 'burning_ship':
                image[y, x] = burning_ship(z, max_iter)
            elif fractal_type == 'phoenix':
                image[y, x] = phoenix(z, max_iter)
            elif fractal_type == 'tricorn':
                image[y, x] = tricorn(z, max_iter)
            elif fractal_type == 'mandala':
                image[y, x] = mandala(z, max_iter)
            elif fractal_type == 'sierpinski':
                image[y, x] = sierpinski(z, max_iter)
            elif fractal_type == 'laplacian':
                image[y, x] = laplacian(z, max_iter)
            elif fractal_type == 'cantor':
                image[y, x] = cantor(z, max_iter)
            elif fractal_type == 'barnsley_fern':
                image[y, x] = barnsley_fern(z, max_iter)
    return image


# გამოსახულების ვიზუალიზაცია
def plot_fractal(image, title):
    plt.figure(figsize=(10, 10))
    plt.imshow(image, cmap='plasma', extent=[-2, 1, -1.5, 1.5])  # მკვეთრი ფერები, როგორიცაა 'plasma'
    plt.colorbar()
    plt.title(title)
    plt.axis('off')  # უცხადებს, რომ ღერძები არ იქნება ნაჩვენები
    plt.show()


# მთავარი ფუნქცია
def main():
    width, height = 800, 800  # სურათის ზომები
    x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5  # ფრაქტალის საზღვრები
    max_iter = 256  # მაქსიმალური iterations

    fractals = ['mandelbrot', 'julia', 'burning_ship', 'phoenix', 'tricorn', 'mandala', 'sierpinski', 'laplacian',
                'cantor', 'barnsley_fern']
    c = complex(0.355, 0.355)  # `c` value for Julia Set

    for fractal in fractals:
        fractal_image = generate_fractal(width, height, x_min, x_max, y_min, y_max, max_iter, fractal,
                                         c if fractal == 'julia' else None)
        plot_fractal(fractal_image, f"{fractal.capitalize()} Fractal")


if __name__ == "__main__":
    main()
