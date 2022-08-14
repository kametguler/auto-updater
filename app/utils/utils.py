
def get_version():
    with open('app/media/version.txt', 'r') as f:
        version = f.read()
    f.close()
    return version

def set_new_version():
    new_version = float(get_version()) + 0.1
    w = "{:.2f}".format(new_version)
    with open('app/media/version.txt', 'w') as f:
        version = f.write(str(w))
    f.close()


if __name__ == '__main__':
    print(get_version())