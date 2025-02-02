def func01():
    print("C'est le début de func01.")
    num = 1 / 0
    print("C'est la fin de func01.")

def func02():
    print("C'est le début de func02.")
    func01()
    print("C'est la fin de func02.")

def main():
    try:
        func02()
    except Exception as e:
        print(e)

main()