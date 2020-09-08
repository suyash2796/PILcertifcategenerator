from PIL import Image, ImageFont, ImageDraw
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import itertools 
import pandas as pd
import smtplib
import os



mail_content = '''Dear {},

Congrats! You performed very well in Quiz competition.

Attached is your Certificate of participation. We wish you best of luck for your future.

Regards
XYZ
'''

#The mail addresses and password
sender_address = 'xyz@gmail.com'
sender_pass = '**********'

def generator():
	#test_names.xlsx sheet will have two columns- One for names and one for emails
	df = pd.read_excel("../data/resource/test_names.xlsx")
	names = df['NAMES'].to_list()
	emails = df['email'].to_list()
	im = Image.open("../data/incoming/test.png")
	location = (220, 60)
	text_color = (100, 100, 200)
	font_path = "../data/resource/arial.ttf"
	font = ImageFont.truetype(font_path, 26)
	for (name, email) in zip(names, emails): 
		im = Image.open("../data/incoming/test.png")
		d = ImageDraw.Draw(im)	
		d.text(location, name,fill=text_color, font=font)
		certificate_name = "../data/work/"+ name + ".png"
		im.save(certificate_name)
		print("Certificate generated for-{}".format(name))
		SendMail(name,certificate_name,email)


def SendMail(name, ImgFileName, mail_id):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'test e-mail'
    msg['From'] = sender_address
    msg['To'] = mail_id
    msg.attach(MIMEText(mail_content.format(name), 'plain'))
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(sender_address, sender_pass)
    s.sendmail(sender_address, mail_id, msg.as_string())
    s.quit()
    print('Mail Sent')

generator()
