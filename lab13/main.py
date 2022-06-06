from glob import glob
from image_proxy import ImageProxy


def main():
    gallery = [ImageProxy(path) for path in sorted(glob("images/img*.png"))]
    for image in gallery:
        image.display()


if __name__ == "__main__":
    main()