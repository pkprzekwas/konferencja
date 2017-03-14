
g = 'global'


def outer(p='param'):
    def inner():
        l = 'local'
        print(g, p, l)
    inner()

outer()
