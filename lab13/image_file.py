from PIL import Image

from display_object import DisplayObject


class ImageFile(DisplayObject):
    def __init__(self, path: str):
        self.image = self.load(path)

    def display(self):
        print("Displaying image.")
        self.image.show()

    def load(self, image_path: str):
        print("Loading image.")
        image = Image.open(image_path)
        return image
