from PIL import Image
import os

for i in os.listdir('original'):
    if i.endswith('jpg'):
        image_file = Image.open('original/' + i)
        image_file = image_file.convert('L')
        image_file.save('result/' + i[:-4] + '_grey.jpg')
