import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from playsound import playsound

class Gui_frame(ttk.Frame):
    def __init__(self, master, animal) -> None:
        super().__init__(master)
        self._animal = animal

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, animal):
        if isinstance(animal, str):
            self._animal = animal
        else:
            raise ValueError("Name must be a string")

class App():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Animals Sound')
        self.window.geometry('1200x600')

        # Get a list of files in the img folder
        img_files = os.listdir('Polimorfismo/AnimalsSoundGUI/img')

        # Create a StringVar to hold the selected animal
        self.animal_var = tk.StringVar()

        # Load the images and store them in a dictionary
        self.images = {}
        for img_file in img_files:
            if img_file.endswith('.png'):
                animal_name = img_file[:-4]  # Remove the file extension
                image_file = f'Polimorfismo/AnimalsSoundGUI/img/{animal_name}.png'
                image = Image.open(image_file)

                # Resize the image to fit the label
                max_width = 800
                max_height = 400
                width, height = image.size
                if width > max_width:
                    height = int(max_width / width * height)
                    width = max_width
                if height > max_height:
                    width = int(max_height / height * width)
                    height = max_height
                image = image.resize((width, height))

                # Convert the image to a PhotoImage and store it in the dictionary
                photo = ImageTk.PhotoImage(image)
                self.images[animal_name] = photo

        # Create a Radiobutton widget for each file in the img folder
        for img_file in img_files:
            if img_file.endswith('.png'):
                animal_name = img_file[:-4]  # Remove the file extension
                rb = ttk.Radiobutton(self.window, text=animal_name, variable=self.animal_var, value=animal_name, command=self.show_image)
                rb.pack(anchor='w', padx=5)

        # Create a Label widget to display the selected image
        self.image_label = tk.Label(self.window)
        self.image_label.pack()

        self.window.mainloop()

    def show_image(self):
        # Get the name of the selected animal
        animal_name = self.animal_var.get()

        # Retrieve the corresponding image from the dictionary and display it in the label
        photo = self.images[animal_name]
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to the PhotoImage to prevent garbage collection

        # Load and play the corresponding sound file
        sound_file = f'Polimorfismo/AnimalsSoundGUI/sound/{animal_name}.mp3'
        playsound(sound_file)

if __name__ == '__main__':
    App()