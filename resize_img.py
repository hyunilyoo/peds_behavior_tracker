# How to use
# EX: python resize_img.py -d test_imgs/ -s 800 600:

from PIL import Image
import os
import argparse

def resize_img(directory, size):
    for img in os.listdir(directory):
        if img != '.DS_Store':
            im = Image.open(directory + img)
            img_resized = im.resize(size, Image.ANTIALIAS)
            img_resized.save(directory + img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resize images')
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Image size')
    args = parser.parse_args()
    resize_img(args.directory, args.size)
