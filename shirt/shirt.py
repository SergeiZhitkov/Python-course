import sys
from PIL import Image, ImageOps


extensions = [".jpeg", ".jpg", ".png"]
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

i=0
end = ""
for file in sys.argv[1:]:
    for extension in extensions:
        i += 1
        if file.endswith(extension) == True:
            if end == extension:
                end =  "+"
            else:
                end = extension
            break
        if i == 4:
            sys.exit("Invalid input")

if end != "+":
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")

try:
    file = Image.open(sys.argv[1])
except FileNotFoundError:
     sys.exit("Input does not exist")

x, y = file.size

shirt = ImageOps.fit(file, size=(1200, 1600))
file.paste(file, box=(0,0,x,y),mask=shirt)
file.save(sys.argv[2])
