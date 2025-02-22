def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r')
        content = f.read()
        print(content)
    except IOError as e:
        print("Le fichier n'existe pas.")
    finally:
        if f is not None:
            f.close()

def append_to_file(file_name, content):
    f = open(file_name, 'a')
    f.write(content)
    f.close()

if __name__ == '__main__':
    print_file_info('text.txt')
    append_to_file('text.txt', 'alex')