import os
import json
from colorthief import ColorThief
from PIL import Image
import matplotlib.pyplot as plt

INPUT_DIR = "input"
OUTPUT_DIR = "output"
COLOR_COUNT = 6

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def extract_palette(image_path, color_count=COLOR_COUNT):
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=color_count, quality=1)

    return {
        "dominant_color": {
            "rgb": dominant_color,
            "hex": rgb_to_hex(dominant_color)
        },
        "palette": [
            {"rgb": color, "hex": rgb_to_hex(color)} for color in palette
        ]
    }

def save_json(data, out_path):
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2)

def save_css(data, out_path):
    css = ""
    for i, color in enumerate(data["palette"]):
        css += f"--color{i+1}: {color['hex']};\n"
    with open(out_path, 'w') as f:
        f.write(css)

def save_palette_image(palette_data, out_path):
    colors = [color["rgb"] for color in palette_data["palette"]]
    fig, ax = plt.subplots(figsize=(len(colors) * 2, 2))
    for i, color in enumerate(colors):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=[c/255 for c in color]))
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()

def process_images():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(INPUT_DIR, filename)
            base_name = os.path.splitext(filename)[0]
            output_folder = os.path.join(OUTPUT_DIR, base_name)

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            print(f"🔍 Processing {filename}...")

            palette_data = extract_palette(image_path)

            save_json(palette_data, os.path.join(output_folder, "palette.json"))
            save_css(palette_data, os.path.join(output_folder, "palette.css"))
            save_palette_image(palette_data, os.path.join(output_folder, "palette.png"))

            print(f"✅ Saved to {output_folder}/")

if __name__ == "__main__":
    process_images()
