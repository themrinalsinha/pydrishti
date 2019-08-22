import cv2
import numpy as np

from PIL import ImageDraw, Image

class ProcessImageData:

    def bounding_box(self, mark_image=False):
        pixel_data    = self.image.load()
        width, height = self.image.size

        # finding coordinates of bounding rectangle
        x_min = width
        y_min = height
        x_max = 0
        y_max = 0

        for i in range(width):
            for j in range(height):
                if pixel_data[i, j][0] == 0:
                    # getting corners of bounding rectangel
                    if i < x_min: x_min = i
                    if j < y_min: y_min = j
                    if i > x_max: x_max = i
                    if j > y_max: y_max = j
        coordinates = (x_min, y_min, x_max, y_max)
        if not mark_image:
            return coordinates

        draw = ImageDraw.Draw(self.image)
        draw.rectangle(coordinates, fill=None, outline=(255, 0, 0))
        return self.image

    # change size of image in same ratio
    def change_size(self, size):
        wpercent = (size / float(self.image.size[0]))
        h_size   = int((float(self.image.size[1])*float(wpercent)))
        image    = self.image.resize((size, h_size), Image.ANTIALIAS)
        return image

    # makes line thinner
    def erosion(self, x=2, y=2, iterations=1, suppress_scaling=False):
        if not suppress_scaling:
            x = x * self.width / 200
            y = y * self.height / 100
        image  = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        kernel = np.ones((x, y), np.uint8)
        image  = cv2.erode(image, kernel, iterations=iterations)
        image  = Image.fromarray(image)
        return image

    # makes line thicker
    def dilation(self, x=2, y=2, iterations=1, suppress_scaling=False):
        if not suppress_scaling:
            x = x * self.width / 200
            y = y * self.height / 100
        image  = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        kernel = np.ones((x, y), np.uint8)
        image  = cv2.dilate(image, kernel, iterations=iterations)
        image  = Image.fromarray(image)
        return image
