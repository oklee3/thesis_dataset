from PIL import Image, ImageDraw
import random
import os, sys

# basic parameters
IMAGE_SIZE = (128, 128)
BACKGROUND_COLOR = (255, 255, 255)

OVERLAP_DIR = "data/images_overlap"
OVERLAP_BW_DIR = "data/images_overlap_bw"

N_IMAGES = 10

os.makedirs(OVERLAP_DIR, exist_ok=True)
os.makedirs(OVERLAP_BW_DIR, exist_ok=True)


# generate a random shape
def random_circle():
    radius = random.randint(8, 20)
    x = random.randint(radius, IMAGE_SIZE[0] - radius)
    y = random.randint(radius, IMAGE_SIZE[1] - radius)

    return {
        "center": (x, y),
        "radius": radius,
        "color": (0, 0, 0)
    }

def random_triangle():
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


# drawing functions
def draw_circle(draw, center, radius, color):
    x, y = center
    draw.ellipse(
        [x - radius, y - radius, x + radius, y + radius],
        fill=color
    )

def draw_triangle(draw, vertices, color):
    draw.polygon(vertices, fill=color)


# IMAGE GENERATING FUNCTIONS
def generate_overlapping_image(idx):
    """
    shapes always overlap, varying size and position
    """
    img = Image.new("RGB", IMAGE_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    circle = random_circle()

    cx, cy = circle["center"]
    size = circle["radius"] 

    max_offset = size // 2
    dx = random.randint(-max_offset, max_offset)
    dy = random.randint(-max_offset, max_offset)
    tx = cx + dx
    ty = cy + dy

    vertices = [
        (tx, ty - size),
        (tx - size, ty + size),
        (tx + size, ty + size)
    ]

    triangle = {
        "vertices": vertices,
        "color": (255, 0, 0)
    }

    draw_circle(draw, circle["center"], circle["radius"], circle["color"])
    draw_triangle(draw, triangle["vertices"], triangle["color"])

    filename = f"overlap_{idx:04d}.png"
    img.save(os.path.join(OVERLAP_DIR, filename))

# image where shapes overlap (black and white only)
def generate_overlapping_image_bw(idx):
    """
    same as above, no color
    """
    img = Image.new("RGB", IMAGE_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    circle = random_circle()

    cx, cy = circle["center"]
    size = circle["radius"] 

    max_offset = size // 2
    dx = random.randint(-max_offset, max_offset)
    dy = random.randint(-max_offset, max_offset)
    tx = cx + dx
    ty = cy + dy

    vertices = [
        (tx, ty - size),
        (tx - size, ty + size),
        (tx + size, ty + size)
    ]

    triangle = {
        "vertices": vertices,
        "color": (0, 0, 0)
    }

    draw_circle(draw, circle["center"], circle["radius"], circle["color"])
    draw_triangle(draw, triangle["vertices"], triangle["color"])

    filename = f"overlap_{idx:04d}.png"
    img.save(os.path.join(OVERLAP_BW_DIR, filename))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 test_script.py [overlap]")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "overlap":
        for i in range(N_IMAGES):
            generate_overlapping_image(i)

    if mode == "overlap_bw":
        for i in range(N_IMAGES):
            generate_overlapping_image_bw(i)
    
