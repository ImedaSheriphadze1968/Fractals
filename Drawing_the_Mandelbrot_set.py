import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ----------  ისე, რომ ფანჯარა გამოჩნდეს ზედა მარცხენა კუთხეში ------------
x = 20
y = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
# --------------------------------------------------------------------

pygame.init()

W = 1200
H = 600

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("მანდელბროტის ნაკრები")
sc.fill(WHITE)

FPS = 30        # კადრების რაოდენობა წამში
clock = pygame.time.Clock()

P = 200                     # ზომა [2*P+1 x 2*P+1]
scale = P / 2               # მასშტაბის ფაქტორი
view = (0, 0)            # ხედვის კუთხის ოფსეტური კოორდინატები
n_iter = 100                # გამეორებების რაოდენობა მანდელბროტის ნაკრების წევრობის შესამოწმებლად

# თითოეული პიქსელის ფერის ლამაზად გამოსახვა
for y in range(-P + view[1], P + view[1], 2):  # ნაბიჯი 2 (პიქსელის თითოეული ობიექტი)
    for x in range(-P + view[0], P + view[0], 2):  # თითოეული სვეტის ხატვა
        a = x / scale
        b = y / scale
        c = complex(a, b)
        z = complex(0)
        n = 0
        for n in range(n_iter):
            z = z**2 + c
            if abs(z) > 2:
                break

        if n == n_iter - 1:
            # ნაკრების ნაწილები შავია
            r = g = b = 0
        else:
            # ფერები, რომლებიც ნიმუშზე დამოკიდებულია
            r = int(255 * (n % 8) / 8)  # წითელი
            g = int(255 * (n % 16) / 16)  # მწვანე
            b = int(255 * (n % 32) / 32)  # ლურჯი

        # ამ შემთხვევაში, ფერები უფრო ფერადი და განსხვავებულია
        pygame.draw.rect(sc, (r, g, b), (x + P - view[0], y + P - view[1], 2, 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(FPS)

