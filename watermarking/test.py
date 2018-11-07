from PIL import Image

i1=Image.open("1.jpg")
i2=Image.open("2.jpg")
print(i2.size)
[w1,h1]=i1.size
t=int(input())
w2=w1//(2**t)
h2=h1//(2**t)
i3=i2.resize((w2, h2))
#i3=i3.load()
r0=0
g0=0
b0=0
for x in range(w1):
	for y in range(h1):
		[r1,g1,b1]=i1.getpixel((x,y))
		[r2,g2,b2]=i3.getpixel((x%w2,y%h2))
		#r1=g1=b1=0
		#i3.putpixel((x,y),(int(r1/4)*4+int(r2/64),int(g1/4)*4+int(g2/64),int(b1/4)*4+int(b2/64)))
		i1.putpixel((x,y),(r1//4*4+r2//64,g1//4*4+g2//64,b1//4*4+b2//64))
		#i3.putpixel((x,y),(r1%4,g1%4,b1%4))
		#print((-r1%4+int(r2/64),-g1%4+int(g2/64),-b1%4+int(b2/64)))
print(r0)
print(g0)
print(b0)
i1.save("7.png","png")
