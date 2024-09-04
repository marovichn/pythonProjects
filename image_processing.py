from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)

filtered_img.save("blured-pikachu.png", "png")
gray_image = img.convert("L")

gray_image.save("gray-pikachu.png", "png")

gray_image.show()
filtered_img.show()