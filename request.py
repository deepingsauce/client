#import requests
from lxml import etree
import httplib
import xml.dom.minidom
import base64

HOST = "220.230.117.99:3000"
API_URL = "/mycallback"

def post_request(xml_content):
    server = httplib.HTTP(HOST)
    server.putrequest("POST",API_URL)
    server.putheader("Host",HOST)
    server.putheader("User-Agent","Python post")
    server.putheader("Content-type","text/xml; charset=\"UTF-8\"")
    server.putheader("Content-length", "%d" % len(xml_content))
    server.endheaders()

    server.send(xml_content)

    statuscode, statusmessage, header = server.getreply()
    result = server.getfile().read()

    print statuscode, statusmessage, header

with open("image.jpg","rb") as image_file:
    encoded_image = base64.b64encode(image_file.read())

#with open("imageToSave.png", "wb") as fh:
#    fh.write(encoded_image.decode('base64'))

root = etree.Element("dps_din", page="/mycallback")
dev_id = etree.SubElement(root, "dev_id")
dev_id.text = "0"
img = etree.SubElement(root, "img")
img.text = encoded_image
print(etree.tostring(root))
post_request(etree.tostring(root))
print("end")

'''

def post_request(xml_location):
    request = open(xml_location,"r").read()
'''  



'''
url = "http://220.230.117.99:3000/mycallback"
xml = """<?xml version='1.0' encoding='utf-8'?>
<a>6</a>"""
headers = {'Content-Type': 'application/xml'}
print requests.post(url,data=xml,headers=headers).text
'''

