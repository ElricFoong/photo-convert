from PIL import Image
import os

for i in os.listdir('original'):
    if i.endswith('jpg'):  # or ('original/' + i )
        image_file = Image.open(os.path.join('original', i))
        image_file = image_file.convert('L')
        image_file.save(os.path.join('result', i[:-4] + '_grey.jpg'))
        #   ('result/' + i[:-4] + '_grey.jpg)
