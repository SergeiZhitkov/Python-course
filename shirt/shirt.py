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



try:
    with Image.open(sys.argv[1]) as file:
        ImageOps.fit(file, size=(600, 600))
        file.paste(file, box=None, mask=None)
        file.save(sys.argv[2], format=None)
except FileNotFoundError:
    sys.exit("Input does not exist")