from lxml import etree
import httplib
import xml.dom.minidom
import base64
import json

HOST = "220.230.117.99:3000"
API_URL = ""	# nodejs: /mycallback

def save_mp3(content):
	sound = open("sound.mp3","w")
	sound.write(content)
	sound.close()

def post_request(content):
	server = httplib.HTTP(HOST)
	server.putrequest("POST",API_URL)
	server.putheader("Host",HOST)
	server.putheader("User-Agent","Python post")
	#server.putheader("Content-type","text/xml; charset=\"UTF-8\"")
	server.putheader("Content-type","application/json; charset=\"UTF-8\"")
	server.putheader("Content-length", "%d" % len(content))
	server.endheaders()

	server.send(content)

	statuscode, statusmessage, header = server.getreply()
	result = server.getfile().read()
	save_mp3(result)

	print(statuscode, statusmessage, header)
	#print(result)

def send_image(imgfile_name):
	with open(imgfile_name,"rb") as image_file:
	    encoded_image = base64.b64encode(image_file.read())

	#with open("imageToSave.png", "wb") as fh:
	#    fh.write(encoded_image.decode('base64'))

	root = etree.Element("dps_din", page="")	# nodejs: /mycallback
	dev_id = etree.SubElement(root, "dev_id")
	dev_id.text = "0"
	img = etree.SubElement(root, "img")
	img.text = encoded_image
	#print(etree.tostring(root))
	post_request(etree.tostring(root))
	print("end")

def send_image_json(imgfile_name):
	with open(imgfile_name,"rb") as image_file:
		encoded_image = base64.b64encode(image_file.read())

	root = {}
	root["dev_id"] = 0
	root["img"] = encoded_image
	post_request(json.dumps(root))
	print("end")

###
#send_image("image.jpg")
send_image_json("block.jpg")

'''
url = "http://220.230.117.99:3000/mycallback"
xml = """<?xml version='1.0' encoding='utf-8'?>
<a>6</a>"""
headers = {'Content-Type': 'application/xml'}
print requests.post(url,data=xml,headers=headers).text
'''

