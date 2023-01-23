import sys
import getopt
import imageio.v2 as imageio
import os
from pygifsicle import optimize

default_fps = 60


def parse_args(argv):
    arg_file_name = ""
    arg_path = ""
    arg_fps = ""
    arg_help = "{0} -n <file_name> -p <path> -f <fps>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hn:p:f:", ["help",
                                                         "file_name=",
                                                         "path=",
                                                         "fps="])
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

    print('file_name:', arg_file_name)
    print('path:', arg_path)
    if arg_fps:
        print('fps:', arg_fps)
    else:
        print('fps:', default_fps + '*default')

    return arg_file_name, arg_path, int(arg_fps)


def append_images(folder_images):
    images = []
    image_types = (".png", ".jpg", ".jpeg")
    for image in os.listdir(folder_images):
        if image.endswith(image_types):
            images.append(folder_images + '/' + image)
    return images


def make_gif(file_name, path, fps=default_fps):
    # fps: change this for GIF speed. The higher, the faster
    images = append_images(path + '/')
    gif_path = path + '/' + file_name + '.gif'
    with imageio.get_writer(gif_path, mode='I', fps=fps) as writer:
        for image in images:
            writer.append_data(imageio.imread(image))

    optimize(gif_path)


if __name__ == "__main__":
    arg_file_name, arg_path, arg_fps = parse_args(sys.argv)

    if arg_fps:
        make_gif(file_name=arg_file_name, path=arg_path, fps=arg_fps)
    else:
        make_gif(file_name=arg_file_name, path=arg_path)
