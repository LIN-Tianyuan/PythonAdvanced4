__all__ = ['test']

def test(a, b):
    print(a + b)

def test_a():
    print('test_a')

def test_b():
    print('test_b')


# Appeler la fonction uniquement dans le fichier actuel
if __name__ == '__main__':
    test_a()