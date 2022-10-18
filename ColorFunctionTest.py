import ColorFunction as cf
from PIL import Image
import time

colorfunction = cf.SublimeLight

img = Image.new("RGB",(256,30))

for x in range(256) :
    for y in range(30) :
        img.putpixel((x,y),colorfunction(x))
        
img.save("Images\\ColorFunction_%s_" %(colorfunction.__name__)+time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))+".png")

