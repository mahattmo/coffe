from PIL import Image, ImageDraw, ImageFont
import os

# Paths to images
image_dir = 'public/images'
images = ['cold-brew.jpg', 'espresso.jpg', 'hero-coffee.jpg', 'latte.jpg', 'mocha.jpg', 'spiced-coffee.jpg']
labels = ['Cold Brew', 'Espresso', 'Hero Coffee', 'Latte', 'Mocha', 'Spiced Coffee']

# Load and resize images
loaded_images = []
for img_name in images:
    img_path = os.path.join(image_dir, img_name)
    img = Image.open(img_path)
    img = img.resize((300, 300), Image.Resampling.LANCZOS)
    loaded_images.append(img)

# Canvas size: 3 columns, 2 rows, with margins
canvas_width = 950
canvas_height = 650
canvas = Image.new('RGB', (canvas_width, canvas_height), '#8B4513')  # Warm brown background

# Paste images in grid
positions = [(25, 25), (350, 25), (675, 25), (25, 350), (350, 350), (675, 350)]
for i, img in enumerate(loaded_images):
    canvas.paste(img, positions[i])

# Add text labels
draw = ImageDraw.Draw(canvas)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except:
    font = ImageFont.load_default()

text_color = 'white'  # High contrast on brown
for i, label in enumerate(labels):
    x, y = positions[i]
    text_x = x + 150 - len(label)*5  # Center text
    text_y = y + 310
    draw.text((text_x, text_y), label, fill=text_color, font=font)

# Create logo
logo_size = 100
logo = Image.new('RGBA', (logo_size, logo_size), (0,0,0,0))
logo_draw = ImageDraw.Draw(logo)

# Coffee cup: brown ellipse and rectangle
cup_color = '#654321'
logo_draw.ellipse([20, 60, 80, 90], fill=cup_color)  # Base
logo_draw.rectangle([30, 30, 70, 80], fill=cup_color)  # Body
logo_draw.ellipse([25, 20, 75, 50], fill=cup_color)  # Top

# Croissant: yellow arcs
croissant_color = '#FFD700'
logo_draw.pieslice([10, 10, 50, 50], 0, 180, fill=croissant_color)
logo_draw.pieslice([10, 10, 50, 50], 180, 360, fill=croissant_color)
logo_draw.ellipse([15, 15, 45, 45], fill=croissant_color)

# Paste logo at top center
logo_x = (canvas_width - logo_size) // 2
logo_y = 10
canvas.paste(logo, (logo_x, logo_y), logo)

# Save the collage
canvas.save('collage.jpg', 'JPEG', quality=95)
print("Collage created: collage.jpg")
