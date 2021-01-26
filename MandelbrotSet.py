import time
from PIL import Image
import math
import cmath

# Color Mode of the iamge.
# "L" for GaryLevel or "RGB" for RGB image.
colormode = "RGB"

# Width and Height of the image.
width  = 100    
height = 100

# Center point X,Y value and Radius
x0 =  -0.5
y0 =  0
r  =  1

xmin = x0 - r
xmax = x0 + r
ymin = y0 - r
ymax = y0 + r

# Times of max interations.
n = 100

# Escaping speed of the point.
def mandelbrot(x,y) :
    y = height - y
    x = ( 2 * x - width  ) / width  * r + x0
    y = ( 2 * y - height ) / height * r + y0
    z = 0
    c = x + y * (1j)
    for i in range(n) :
        z = z * z + c
        if abs(z) > 2 :
            return i
    return n

# Pixel color determined by color mode.
def pixel(x,y):
    age=mandelbrot(x,y)*255//n
    if colormode == "L":
        return age
    elif colormode =="RGB":
        return colorfunction(age)
    else:
        return 0

# Color Function of the image (if color mode is RGB).
def colorfunction(age):
    if age == 255:
        return (0,0,0)
    return (age,255-age,255)

time_start = time.time()

img = Image.new(colormode,(width,height))

for x in range(width) :
    for y in range(height) :
        img.putpixel((x,y),pixel(x,y))
        
img.save("Mandelbrot_X%.4f_Y%.4f_R%.4f_N%d_W%d_H%d_%d.png" %(x0,y0,r,n,width,height,time.time()))

time_end = time.time()

print("Done!")
print("Totally cost %.2f s" %(time_end-time_start))
