from PIL import Image

i=Image.open("7.png")
[w1,h1]=i.size
I=Image.new('RGB',(w1,h1),'white')
for x in range(w1):
	for y in range(h1):
		[r,g,b]=i.getpixel((x,y))
		I.putpixel((x,y),(85*(r-r//4*4),85*(g-g//4*4),85*(b-b//4*4)))
I.save("6.png","png")
