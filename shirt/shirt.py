import sys
import csv
import PIL

extensions = [".jpeg", ".jpg", ".png"]
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

i=0
for file in sys.argv[1:]:
    for extension in extensions:
        i += 1
        if file.endswith(extension) == True:
            break
        if i == 3:
            sys.exit("Invalid input")


try:
    with Image.open(sys.argv[1]) as file:
        PIL.ImageOps.fit(file, method=Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        Image.paste(file, box=None, mask=None)
        Image.save(sys.argv[2], format=None)