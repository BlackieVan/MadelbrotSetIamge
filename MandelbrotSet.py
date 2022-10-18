import time
from PIL import Image
import math
import cmath
import ColorFunction as cf


# Color Mode of the iamge.
# "L" for GaryLevel or "RGB" for RGB image.
colormode = "RGB"

# Color Function (if color mode is "RGB")
colorfunction=cf.Argon

# Width and Height of the image.
width  = 1920
height = 1080

# Center point X,Y value and Radius
x0 =  0.3
y0 =  0.58
r  =  0.1

rh   = r
rw   = rh / height * width
xmin = x0 - rw
xmax = x0 + rw
ymin = y0 - rh
ymax = y0 + rh

# Times of max interations.
n = 100

# Escaping speed of the point.
def mandelbrot(x,y) :
    y = height - y
    x = ( 2 * x - width  ) / width  * rw + x0
    y = ( 2 * y - height ) / height * rh + y0
    z = 0
    c = x + y * (1j)
    for i in range(n) :
        z = z * z + c
        if abs(z) > 2 :
            return i
    return n

# Pixel color determined by color mode.
if colormode == "L":
    def pixel(x, y):
        return mandelbrot(x, y) * 255 // n
if colormode == "RGB":
    def pixel(x, y):
        return colorfunction(mandelbrot(x, y) * 255 // n)
    
time_start = time.time()

img = Image.new(colormode,(width,height))

def fill(width,height):
    for x in range(width) :
        for y in range(height) :
            img.putpixel((x,y),pixel(x,y))

fill(width,height)
     
img.save("Images\\Mandelbrot_X%.4f_Y%.4f_R%.4f_N%d_W%d_H%d_" %(x0,y0,r,n,width,height)+time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))+".png")

time_end = time.time()

print("Done!")
print("Totally cost %.3f s" %(time_end-time_start))




