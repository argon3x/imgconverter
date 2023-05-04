#!/usr/bin/python3
# coding: utf-8
from time import sleep
from PIL import Image
import signal, sys, argparse, os

### By Argon3x
### Supported: Debian Based Systems and Termux
### Version: 1.0

# Colors
green = "\033[01;32m"; blue = "\033[01;34m"; red = "\033[01;31m"
purple = "\033[01;35m"; yellow = "\033[01;33m"; end = "\033[00m"

# Context Box
box = f"{purple}[{green}+{purple}]{end}"
ast = f"{blue}[{purple}*{blue}]{end}"

# Function error and interrupt
def interrupt_handler():
    sys.stdout.write(f"\n{blue}>>> {red}Process Canceled {blue}<<<{end}\n\n")
    sys.exit(1)

def error_handler(type_error):
    sys.stdout.write(f"\n{blue}script error: {red}{type_error}{end}\n\n")
    sys.exit(1)

# Call the signals
signal.signal(signal.SIGINT, interrupt_handler)
signal.signal(signal.SIGTERM, error_handler)


# Function Image Converter
def imageConverter(arg_format, arg_input, arg_output, arg_save):
    pme = f"{blue}[{green}~{blue}]{end}"

    # Assign values to empty varibales
    arg_save = arg_save if arg_save is not None else "./"

    if arg_output is None:
        just_the_full_file_name = os.path.basename(arg_input)
        file_name, _ = os.path.splitext(just_the_full_file_name)
        arg_output = '.'.join([file_name, arg_format])
    
    try:
        print(f"\n{pme} {yellow}Converting image to {green}{arg_format.upper()}{end}...........")
        with Image.open(arg_input) as img:
            save_image_as = f"{arg_save}/{arg_output}"
            img.save(save_image_as, arg_format)
    except IOError:
        error_handler(type_error="[!] An Error Ocurred While Converting Image [!]")
    else:
        print(f"{box} {green}Done{end}")


# main function
def main(arg_format, arg_input, arg_output, arg_save):
    os.system('clear')
    print(f"{box} {yellow}Processing the data{end}............")
    sleep(1)
    
    # Checking image format
    print(f"{ast} {yellow}Format to convert {end}-> {purple}{arg_format}{end}", end='')
    if arg_format == 'png' or arg_format == 'jpg':
        print(f"\t{blue}[{green}ok{blue}]{end}")
    else:
        print(f"\t{blue}[{red}failed{blue}]{end}")
        error_handler(type_error=f"{red}Invalid {purple}{arg_format} {red}Format..!!!{end}")

    sleep(1)

    # Checking if image exist 
    name_image = os.path.basename(arg_input)
    print(f"{ast} {yellow}Image Name {end}-> {purple}{name_image}{end}", end='')
    if os.path.exists(arg_input):
        print(f"\t{blue}[{green}ok{blue}]{end}")
    else:
        name_image = os.path.basename(arg_input)
        print(f"\t{blue}[{red}failed{blue}]{end}")
        error_handler(type_error=f"{purple}{name_image} {red}Image Does Not Exist..!!!{end}")

    sleep(1)
   
    # Checking the value of variable
    if not arg_output is None:
        print(f"{ast} {yellow}New Name {end}-> {blue}{arg_output}{end}")

    sleep(1)

    # Checking the value of variable and Checking if exist the directory path
    if not arg_save is None:
        print(f"{ast} {yellow}Save Image To {end}-> {blue}{arg_save}{end}", end='')
        if os.path.isdir(arg_save):
            print(f"\t{blue}[{green}ok{blue}]{end}")
        else:
            print(f"\t{blue}[{red}failed{blue}]{end}")
            error_handler(type_error=f"{purple}{arg_save} {red}Path Does Not Exist..!!!{end}")

    # Call function
    imageConverter(arg_format, arg_input, arg_output, arg_save)


if __name__ == '__main__':
    # Configure the arguments
    parser = argparse.ArgumentParser(description="This script is an image converter from JPG to PNG and from PNG to JPG.")
    parser.add_argument('-f', type=str, required=True, metavar='png/jpg', help='The format is required. (required)')
    parser.add_argument('-i', type=str, required=True, metavar='image', help='Select an imagen to convert into some format. (required)')
    parser.add_argument('-o', type=str, required=False, metavar='new image', help='Save the image with a new name.')
    parser.add_argument('-s', type=str, required=False, metavar='save image', help='Select a path to save the image.')
    args = parser.parse_args()
   
    # Calling the main funcion
    main(args.f, args.i, args.o, args.s)

