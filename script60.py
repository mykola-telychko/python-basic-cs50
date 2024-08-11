import sys 
from PIL import Image
# Print the version to confirm it's working
# print(Image.__version__)

images = []

for arg in sys.argv[1:]: 
    image = Image.open(arg)
    images.append(image)

images[0].save("1.gif", save_all=True, append_images=[images[1]], duration=200)

# cli> python script60.py 1.gif 2.gif 