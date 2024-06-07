from PIL import Image

def concatenate_images_vertically(images):
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    total_height = sum(heights)

    new_image = Image.new('RGB', (total_width, total_height))

    y_offset = 0
    for image in images:
        new_image.paste(image, (0, y_offset))
        y_offset += image.size[1]

    return new_image
from PIL import Image

def concatenate_images_horizontally(images):
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_image = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for image in images:
        new_image.paste(image, (x_offset, 0))
        x_offset += image.size[0]

    return new_image

image1 = Image.open('line_chart_KS (1).png')
image2 = Image.open('KS (1).png')
result_image = concatenate_images_horizontally([image2, image1])
result_image.save('result_KS.jpg')

image1 = Image.open('output/1024/AES CBC MODE histogram.png')
image2 = Image.open('output/1024/DES CBC MODE histogram.png')
image3 = Image.open('output/1024/DES3 CBC MODE histogram.png')
image4 = Image.open('output/1024/Blowfish CBC MODE histogram.png')
image5 = Image.open('output/1024/RC4 MODE histogram.png')

result_image = concatenate_images_vertically([image1, image2,image3,image4,image5])
result_image.save(f'1024result.jpg')