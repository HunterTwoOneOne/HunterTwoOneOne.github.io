# Generate grandma's wallpaper

from PIL import Image

# Grid size (200 x 150)
width, height = 200, 150
img = Image.new("RGB", (width, height))

# Define colors
teal = (15, 179, 176)
beige = (232, 217, 192)
violet = (191, 163, 214)
gray = (248, 248, 248)

pixels = img.load()

# Fill grid by index
for y in range(height):
    for x in range(width):
        index = y * width + x + 1  # 1-based index
        if index % 12 == 0:
            pixels[x, y] = violet
        elif index % 3 == 0:
            pixels[x, y] = teal
        elif index % 4 == 0:
            pixels[x, y] = beige
        else:
            pixels[x, y] = gray

print(pixels)

img = img.resize((2000, 1500), resample=Image.NEAREST)
img.save("grid.png")