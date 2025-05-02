# 🎨 Image Palette Extractor

This project extracts color palettes from images, providing a set of dominant and complementary colors in multiple formats. It's designed to help designers, developers, and creatives quickly capture the essence of an image’s color scheme.

## Features

1. **Color Extraction:** Uses [ColorThief](https://github.com/fengsp/color-thief-py) to find the dominant color and a palette of top colors from each image.
2. **Multiple Outputs:** Generates:
    - A `.png` palette preview
    - A `.json` file with RGB + HEX values
    - A `.css` file with ready-to-use CSS variables
3. **Batch Processing:** Automatically processes every image in the `input` folder.
4. **Organized Output:** Each image gets its own subfolder in `output` with all generated files.

---

## Setup

### Installation

1. Clone this repository to your local machine.
2. Install the required Python dependencies using `pip install pipenv && pipenv install`.

## Usage

1. Place your input images in the `input` folder.
2. Run the script `main.py`.
3. Translated images will be saved in the `output` folder.

## Notes
For each image in input/, the following will be created in output/<image-name>/:
- palette.json: List of colors in RGB and HEX
- palette.css: CSS variables for easy use in styling
- palette.png: Visual swatch of the palette

## Examples

## Input
![input_example](https://github.com/user-attachments/assets/2905ce45-2e57-4659-8fab-6002140bce9b)

## JSON Format Example
```json
{
  "dominant_color": {
    "rgb": [
      228,
      157,
      63
    ],
    "hex": "#e49d3f"
  },
  "palette": [
    {
      "rgb": [223,141,34],
      "hex": "#df8d22"
    },
    {
      "rgb": [242,216,186],
      "hex": "#f2d8ba"
    },
    {
      "rgb": [241,190,124],
      "hex": "#f1be7c"
    },
    {
      "rgb": [142,66,10],
      "hex": "#8e420a"
    },
    {
      "rgb": [146,86,32],
      "hex": "#925620"
    },
    {
      "rgb": [251,217,122],
      "hex": "#fbd97a"
    }
  ]
}
```

## CSS Format Example

```css
--color1: #df8d22;
--color2: #f2d8ba;
--color3: #f1be7c;
--color4: #8e420a;
--color5: #925620;
--color6: #fbd97a;
```

## Acknowledgments
- [ColorThief](https://github.com/fengsp/color-thief-py) – For color extraction.
- [Pillow (PIL Fork)](https://python-pillow.org/) – For image handling.
- [Matplotlib](https://matplotlib.org/) – For palette visualization.
