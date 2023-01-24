import sys
import getopt
import os
from PIL import Image

default_fps = 60
default_quality = 95


def parse_args(argv):
    arg_file_name = ""
    arg_path = ""
    arg_fps = ""
    arg_quality = ""
    arg_help = "{0} -n <file_name> -p <path> -f <fps> -q <quality>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hn:p:f:q:", ["help",
                                                           "file_name=",
                                                           "path=",
                                                           "fps=",
                                                           "quality"])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-n", "--file_name"):
            arg_file_name = arg
        elif opt in ("-p", "--path"):
            arg_path = arg
        elif opt in ("-f", "--fps"):
            arg_fps = arg
        elif opt in ("-q", "--quality"):
            arg_quality = arg

    print('file_name:', arg_file_name)
    print('path:', arg_path)
    if arg_fps:
        print('fps:', arg_fps)
    else:
        arg_fps = default_fps
        print('fps:', arg_fps, '*default')
    if arg_quality:
        print('quality:', arg_quality)
    else:
        arg_quality = default_quality
        print('quality:', arg_quality, '*default')

    return arg_file_name, arg_path, int(arg_fps), int(arg_quality)


def append_images(folder_images):
    images = []
    image_types = (".png", ".jpg", ".jpeg")
    for image in os.listdir(folder_images):
        if image.endswith(image_types):
            images.append(folder_images + '/' + image)
    return images


def make_gif(file_name, path, fps=default_fps, quality=default_quality):
    # Specify the directory containing the images
    images = append_images(path)
    gif_path = path + '/' + file_name + '.gif'
    # Create a list of image filenames
    frames = [Image.open(image).convert('RGB') for image in images]
    # Save the frames as an optimized GIF
    frames[0].save(gif_path,
                   format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=(fps * 1000) / len(frames),
                   loop=0,
                   optimize=True,
                   quality=quality)


if __name__ == "__main__":
    arg_file_name, arg_path, arg_fps, arg_quality = parse_args(sys.argv)

    make_gif(file_name=arg_file_name, path=arg_path, fps=arg_fps, quality=arg_quality)
