from display_object import DisplayObject
from image_file import ImageFile


class ImageProxy(DisplayObject):
    def __init__(self, path: str):
        self.path = path
        self.display_object = None

    def display(self):
        if self.display_object is None:
            self.display_object = ImageFile(self.path)
        self.display_object.display()
