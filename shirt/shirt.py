from PIL import Image, ImageOps
import sys


def main():
    command_line_check = check_command_line(sys.argv)
    if command_line_check != "ok":
        sys.exit(command_line_check)
    render_img(sys.argv[1], sys.argv[2])


def render_img(input, output):
    with Image.open("shirt.png") as shirt, Image.open(input) as img:
        img = ImageOps.fit(image=img, size=shirt.size)
        img.paste(im=shirt, mask=shirt)
        img.save(output)



def check_command_line(argv):
    if len(argv) < 3:
        return "Too few command-line arguments"
    elif len(argv) > 3:
        return "Too many command-line arguments"
    elif not argv[1].endswith((".jpeg", ".jpg", ".png")):
        return "Invalid input"
    elif not argv[2].endswith((".jpeg", ".jpg", ".png")):
        return "Invalid output"
    elif argv[1].rsplit(".", maxsplit = 1)[-1] != argv[2].rsplit(".", maxsplit = 1)[-1]:
        return "Input and output have different extensions"
    else:
        try:
            with open(argv[1], "r") as program:
                return "ok"
        except FileNotFoundError:
            return "File does not exist"


if __name__ == "__main__":
    main()
