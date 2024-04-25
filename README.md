# Work-Sprite App

Work-Sprite is a desktop application built with Python and Tkinter that provides two main functionalities: Sprite Rendering and Image Splitting.

## Features

### Sprite Renderer

- Load sprite images (JPG, JPEG, PNG, BMP)
- Select multiple regions of interest (ROIs) by dragging the mouse
- Save selected ROIs as individual PNG files

### Image Slitter

- Split images (JPG, JPEG, PNG, BMP) into multiple chunks
- Set the step size (width) for splitting
- Choose the save path for the split image chunks
- Option to delete previously split files

## Installation

1. Clone the repository or download the source code.
2. Install dependencies: `pip install opencv-python Pillow`

## Usage

1. Run `main.py` to start the app.
2. Use the provided buttons and input fields to navigate through the functionalities.
3. For Sprite Rendering: Select sprite, choose ROIs, and save selections.
4. For Image Splitting: Select image, set step size, choose save path, and split.

## Contributing

Contributions are welcome! Open an issue or submit a pull request for improvements.

## License

[MIT License](LICENSE)

## Acknowledgments

- Tkinter (GUI toolkit)
- OpenCV (image processing)
- Pillow (image processing support)
