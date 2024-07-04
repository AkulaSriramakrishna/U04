def make_pretty(func):
    def inner():
        print('I am decorated')
        func()
    return inner()

@make_pretty
def ordinary():
    print('I am ordinary')

ordinary()