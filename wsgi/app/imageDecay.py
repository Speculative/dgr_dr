from PIL import Image
import random, io

def makeThumbnail(imagePath):
	print "fuck you"
	im = Image.open(imagePath)
	height = im.size[1]
	width = im.size[0]
	shortestLength = 0
	if height > width:
		shortestLength = width
	else:
		shortestLength = height
	sideL = shortestLength / 5
	print sideL
	heightL = random.randint(0,height-sideL)
	widthL = random.randint(0,width-sideL)
	box = (widthL, heightL, widthL + sideL, heightL + sideL)
	part = im.crop(box)
	part = part.resize((160,20))
	outfile = imagePath + ".thumbnail"
	if imagePath != outfile:
		try:
			part.save(outfile, "PNG")
		except IOError:
			print("cannot create thumbnail for", imagePath)

def corruptImage(imagePath, numPixels):
	im = Image.open(imagePath)
	height = im.size[1]
	width = im.size[0]
	for x in range(0, numPixels):
		opperand = random.randint(0,1)
		direction = random.randint(0,1)
		if height > width:
			shortestLength = width
		else:
			shortestLength = height
		sideL = random.randint(1,10)
		heightL = random.randint(0,height-sideL)
		widthL = random.randint(0,width-sideL)
		if(direction):
			box = (widthL, 0, widthL + sideL, height)
		else:
			box = (0, heightL, width, heightL + sideL)
		part = im.crop(box)
		buff = part.tobytes()
		n = len(buff)
		new=""
		start = random.randint(0,n-2)
		end = random.randint(start,n-1)
		for b in range(n):
			if(start<b<end):
				if(opperand):
					new+=chr( ( ord(buff[b])|ord(buff[(b+10)%len(buff)]) )%256 )
				else:
					new+=chr( ( ord(buff[b])^ord(buff[(b+10)%len(buff)]) )%256 )
			else:
				new += chr(ord(buff[b]))
		if(direction):
			newImage = Image.frombytes("RGB", (sideL,height), new)
		else:
			newImage = Image.frombytes("RGB", (width,sideL), new)
		im.paste(newImage, box)
	try:
		im.save(imagePath)
	except IOError:
		print("cannot corrupt image apparently", imagePath)


if __name__ == "__main__":
	makeThumbnail("test.JPG");
	corruptImage("test.JPG", 10)
