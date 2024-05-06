from PIL import Image

def resize_image(size1, size2):

    image = Image.open('qrimg.png')

    print(f"Current size : {image.size}")

    resized_image = image.resize((660, 660))

    resized_image.save('resized-qrimg.png')