from PIL import Image, ImageFilter
import pytesseract
import requests
from StringIO import StringIO

def process_image(filename):
	image = Image.open(filename)
	image.filter(ImageFilter.SHARPEN)
	return pytesseract.image_to_string(image)

def _get_image(url):
	return StringIO(requests.get(url).content)

def image_string(url):
	return process_image(_get_image(url))