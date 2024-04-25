# Work-Sprite

The Work-Sprite App is a powerful and user-friendly desktop application built with Python and the Tkinter library. It provides two main functionalities: Sprite Rendering and Image Splitting.

## Features

### Sprite Renderer

- Select and load a sprite image (JPG, JPEG, PNG, BMP)
- Display the sprite image in the canvas
- Select multiple regions of interest (ROIs) on the sprite by dragging the mouse
- Save the selected ROIs as individual PNG files

### Image Slitter

- Select an image file (JPG, JPEG, PNG, BMP) to split
- Set the step size (width) for splitting the image
- Choose the save path for the split image chunks
- Split the image into multiple PNG files based on the specified step size
- Option to delete all previously split files in the save path

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python installed on your system.
3. Install the required dependencies by running the following command:

```
pip install opencv-python Pillow
```

## Usage

1. Run the `main.py` file to start the Work-Sprite App.
2. Use the provided buttons and input fields to navigate through the app's functionalities.
3. For Sprite Rendering:
   - Click "Select Sprite" and choose the desired sprite image file.
   - Use the mouse to select regions of interest on the displayed sprite.
   - Click "Save Selections" and choose a location to save the selected ROIs as individual PNG files.
4. For Image Splitting:
   - Click "Select Image" and choose the image file you want to split.
   - Enter the desired step size (width) for splitting the image.
   - Click "Select Save Path" and choose the directory where you want to save the split image chunks.
   - Click "Split Image" to initiate the splitting process.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Tkinter library for providing the GUI toolkit
- The OpenCV library for image processing capabilities
- The Pillow library for additional image processing support

Enjoy using the Work-Sprite App! If you have any questions or need further assistance, please don't hesitate to reach out.
