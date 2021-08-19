"""MemeEngine class to generate a meme given an image and quote."""

import os
import random
from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    """Class will read and post-process an image"""
    
    def __init__(self, output_dir: str):
        """Instantiate class variables"""
        self.output_dir = output_dir
        
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str:
        """
        Method to load, resize, add caption at a random location.
        Parameters:
            img_path: string indicating image location
            text: quote
            author: author of quote
            width: default is 500
        Returns:
            string indicating output file path
        """

        img = Image.open(img_path)
        img_out = f'{self.output_dir}/{random.randint(0,1000)}.png'

        x_size = img.size[0]
        y_size = img.size[1]
        height = int(width*y_size/x_size)
        im_resize = img.resize((width, height), Image.NEAREST)
        
        msg = f'{text}-{author}'
        fnt = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf', 20)
        txt_x = random.choice(range(35,70))
        txt_y = random.choice(range(35,height-100))
        txt = ImageDraw.Draw(im_resize)
        txt.text((txt_x, txt_y), msg, font=fnt, fill=(255,255,255,255))

        im_resize.save(img_out, "png")
        
        return img_out