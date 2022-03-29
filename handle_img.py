from PIL import Image
import os

for file in os.listdir(os.path.join('raw') + file ):
	if file.endswith('.jpg'):
		image_file = Image.open(file)
		image_file = image_file.convert('L')
		image_file.save(os.path.join('result') + file[:-4] + '_grey.png')