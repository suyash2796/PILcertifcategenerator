from PIL import Image, ImageFont, ImageDraw
im = Image.open("../data/incoming/test.png")
d = ImageDraw.Draw(im)

location = (220, 60)
text_color = (100, 100, 200)
font_path = "../data/resource/arial.ttf"
font = ImageFont.truetype(font_path, 26)
d.text(location, "suyash shrivastava",fill=text_color, font=font)

im.save("../data/work/certificate.png")
