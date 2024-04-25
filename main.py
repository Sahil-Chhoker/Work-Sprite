import os
import cv2 as cv
from tkinter import LabelFrame, Tk, Button, Label, Entry, filedialog, Canvas, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")
        self.root.geometry("1280x720")

        self.setup_sprite_renderer()
        self.setup_image_slitter()

    def setup_sprite_renderer(self):
        self.sprite_frame = LabelFrame(self.root, text="Sprite Renderer")
        self.sprite_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.sprite_canvas = Canvas(self.sprite_frame)
        self.sprite_canvas.pack(fill="both", expand="yes", padx=10, pady=10)

        self.sprite_selections = []

        self.select_sprite_button = Button(self.sprite_frame, text="Select Sprite", command=self.select_sprite)
        self.select_sprite_button.pack(pady=5)

        self.save_sprite_button = Button(self.sprite_frame, text="Save Selections", command=self.save_sprite_selections)
        self.save_sprite_button.pack(pady=5)

        self.sprite_canvas.bind("<Button-1>", self.start_selection)
        self.sprite_canvas.bind("<B1-Motion>", self.draw_selection)
        self.sprite_canvas.bind("<ButtonRelease-1>", self.end_selection)

    def setup_image_slitter(self):
        self.slitter_frame = LabelFrame(self.root, text="Image Slitter")
        self.slitter_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.step_label = Label(self.slitter_frame, text="Step Size:")
        self.step_label.grid(row=0, column=0, padx=10, pady=5)

        self.step_entry = Entry(self.slitter_frame)
        self.step_entry.grid(row=0, column=1, padx=10, pady=5)

        self.select_image_button = Button(self.slitter_frame, text="Select Image", command=self.select_image)
        self.select_image_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.save_path_label = Label(self.slitter_frame, text="Save Path:")
        self.save_path_label.grid(row=2, column=0, padx=10, pady=5)

        self.save_path_entry = Entry(self.slitter_frame)
        self.save_path_entry.grid(row=2, column=1, padx=10, pady=5)

        self.select_save_path_button = Button(self.slitter_frame, text="Select Save Path", command=self.select_save_path)
        self.select_save_path_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.split_button = Button(self.slitter_frame, text="Split Image", command=self.split_image, state='disabled')
        self.split_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def select_sprite(self):
        file_path = askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if file_path:
            self.sprite_image = Image.open(file_path)
            self.display_sprite(self.sprite_image)

    def display_sprite(self, image):
        self.sprite_image_tk = ImageTk.PhotoImage(image)
        self.sprite_canvas.config(width=self.sprite_image_tk.width(), height=self.sprite_image_tk.height())
        self.sprite_canvas.create_image(0, 0, anchor="nw", image=self.sprite_image_tk)

    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.sprite_canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    def draw_selection(self, event):
        self.sprite_canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def end_selection(self, event):
        end_x = event.x
        end_y = event.y
        self.sprite_selections.append((min(self.start_x, end_x), min(self.start_y, end_y), max(self.start_x, end_x), max(self.start_y, end_y)))

    def save_sprite_selections(self):
        if self.sprite_image and self.sprite_selections:
            output_file = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if output_file:
                for i, sel in enumerate(self.sprite_selections):
                    selection_img = self.sprite_image.crop(sel)
                    selection_img.save(output_file + f"_selection_{i}.png")

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if file_path:
            self.image_path = file_path
            self.split_button.config(state='normal')

    def select_save_path(self):
        save_path = filedialog.askdirectory()
        if save_path:
            self.save_path_entry.delete(0, 'end')
            self.save_path_entry.insert(0, save_path)

    def split_image(self):
        step = self.step_entry.get()
        save_path = self.save_path_entry.get()

        if step.isdigit():
            if save_path:
                filename = os.path.basename(self.image_path)
                sprite = cv.imread(self.image_path)
                im_length, im_width, im_channel = sprite.shape

                step = int(step)

                if step == 0:
                    i = 0
                    try:
                        while os.path.exists(os.path.join(save_path, f"{i}.png")):
                            os.remove(os.path.join(save_path, f"{i}.png"))
                            i += 1
                    except:
                        messagebox.showinfo("Info", "All files are successfully deleted")
                else:
                    sprite_list = []
                    for i in range(0, im_width, step):
                        crop_sprite = sprite[0:im_length, i:i+step]
                        sprite_list.append(crop_sprite)

                    os.chdir(save_path)
                    for i in range(len(sprite_list)):
                        cv.imwrite(f"{i}.png", sprite_list[i])
                    messagebox.showinfo("Info", "Image successfully splitted")
            else:
                messagebox.showerror("Error", "Please select a save path")
        else:
            messagebox.showerror("Error", "Please enter a valid step size (integer)")

if __name__ == "__main__":
    root = Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
