from PIL import Image, ImageDraw
import random
import os

# basic parameters
IMAGE_SIZE = (128, 128)
BACKGROUND_COLOR = (255, 255, 255)
OUTPUT_DIR = "data/images"
N_IMAGES = 10

os.makedirs(OUTPUT_DIR, exist_ok=True)

def draw_circle(draw, center, radius, color):
    '''
    helper function to draw a circle
    '''
    x, y = center
    draw.ellipse(
        [x - radius, y - radius, x + radius, y + radius],
        fill=color
    )

def draw_triangle(draw, vertices, color):
    draw.polygon(vertices, fill=color)

def random_circle():
    '''
    generate a sample circle based on random or editable parameters
    '''
    radius = random.randint(8, 20)
    x = random.randint(radius, IMAGE_SIZE[0] - radius)
    y = random.randint(radius, IMAGE_SIZE[1] - radius)

    return {
        "center": (x, y),
        "radius": radius,
        "color": (0, 0, 0)
    }

def random_triangle():
    '''
    generate sample triange
    '''
    cx = random.randint(30, 100)
    cy = random.randint(30, 100)
    size = random.randint(12, 25)

    vertices = [
        (cx, cy - size),
        (cx - size, cy + size),
        (cx + size, cy + size)
    ]

    return {
        "vertices": vertices,
        "color": (255, 0, 0)
    }

def generate_image(idx):
    '''
    create an image from a triangle and a circle
    '''
    img = Image.new("RGB", IMAGE_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    circle = random_circle()
    triangle = random_triangle()

    draw_circle(draw, circle["center"], circle["radius"], circle["color"])
    draw_triangle(draw, triangle["vertices"], triangle["color"])

    filename = f"img_{idx:04d}.png"
    img.save(os.path.join(OUTPUT_DIR, filename))

if __name__ == "__main__":
    for i in range(N_IMAGES):
        generate_image(i)

    print(f"Generated {N_IMAGES} images in {OUTPUT_DIR}")
