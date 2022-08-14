import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

version_txt_path = str(BASE_DIR) + "/media/version.txt"

def get_version():
    with open(version_txt_path, 'r') as f:
        version = f.read()
    f.close()
    return version

def set_new_version():
    new_version = float(get_version()) + 0.1
    w = "{:.2f}".format(new_version)
    with open(version_txt_path, 'w') as f:
        f.write(str(w))
    f.close()
