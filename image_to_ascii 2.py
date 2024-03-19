import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
#resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)
#convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value//25]
    return(ascii_str)
def main():
    path = input("Enter the path to the image field : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+100)] for i in range(0, pixel_count, 100))
    print(ascii_image)
    with open("D:\\codes lmao\\learning 1\\learning ever single things ever\\image to ascii\\ascii_image.txt", "w") as f:
        f.write(ascii_image)
main()