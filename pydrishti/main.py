from PIL      import Image

from .extract import ExtractImageInfo
from .process import ProcessImageData

class Drishti(ExtractImageInfo, ProcessImageData):
    def __init__(self, image):
        self.image  = Image.open(image)
        self.width  = self.image.size[0]
        self.height = self.image.size[1]
        self.show   = self.image.show()
