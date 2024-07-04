def make_pretty(func):
    def inner():
        print('I am decorated')
        func()
    return inner()


def ordinary():
    print('I am ordinary')

function_decortor=make_pretty(ordinary)
function_decortor()