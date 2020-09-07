from PIL import Image, ImageFont, ImageDraw
import pandas as pd

df = pd.read_excel("../data/resource/test_names.xlsx")
names = df['NAMES'].to_list()
im = Image.open("../data/incoming/test.png")
location = (220, 60)
text_color = (100, 100, 200)
font_path = "../data/resource/arial.ttf"
font = ImageFont.truetype(font_path, 26)
for name in names:
	im = Image.open("../data/incoming/test.png")
	d = ImageDraw.Draw(im)	
	d.text(location, name,fill=text_color, font=font)
	certificate_name = "../data/work/"+ name + ".png"
	im.save(certificate_name)
	print("Certificate generated for-{}".format(name))
