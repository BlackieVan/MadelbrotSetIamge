import math

#Reference Websites:
#uigradients.com
#webkul.github.io/coolhue/
#webgradients.com
        
def CoolColor(age):
    if age == 255:
        return (0,0,0)
    return (age,255-age,255)

# Name:CanYouFeelTheLoveTonight Colors:#4568DC->#B06AB3
def CanYouFeelTheLoveTonight(age):
    if age == 255:
        return (0,0,0)
    return (int(176-0.420*age),int(106-0.008*age),int(179+0.161*age))
    
# Nmae:Yoda Colors:#493240->#FF0099
def YodaBlack(age):
    if age == 255:
        return (0,0,0)
    return (int(73+0.714*age),int(50-0.196*age),int(64+0.349*age))

def Yoda(age):
    return (int(73+0.714*age),int(50-0.196*age),int(64+0.349*age))


def YodaWhite(age):
    if age == 255:
        return (255,255,255)
    return (int(73+0.714*age),int(50-0.196*age),int(64+0.349*age))


# Name:Argon Colors:#03001E->#7303C0->#EC38BC->#FDEFF9
def Argon(age):
    if age == 255:
        return (0,0,0)
    elif age < 86:
        return (int(3+1.318*age),int(0+0.035*age),int(30+1.906*age))
    elif age < 171:
        return (int(115+1.424*(age-85)),int(3+0.624*(age-85)),int(192-0.047*(age-85)))
    else:
        return (int(236+0.200*(age-170)),int(56+2.153*(age-170)),int(188+0.718*(age-170)))
    return list_argon[age]


# Nmae:Pinky Colors:#DD5E89->#F7BB97
def Pinky(age):
    if age == 255:
        return (0,0,0)
    age=255-age     #reverse colorfuction
    return (int(221+0.102*age),int(94+0.365*age),int(137+0.055*age))
    
# Name:Flickr Colors:#FF0084->#33001B
def Flickr(age):
    if age == 255:
        return (0,0,0)
    age=255-age     #reverse colorfuction
    return (int(255-0.8*age),0,int(132-0.412*age))


# Name:Sublime Light Colors:#FC5C7D->#6A82FB
def SublimeLight(age):
    if age == 255:
        return (0,0,0)
    age=255-age     #reverse colorfuction
    return (int(252+-0.573*age),int(92+0.149*age),int(125+0.494*age))
