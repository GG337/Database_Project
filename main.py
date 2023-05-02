import sys

def say_hi():
    print('hi!')


def add_these(x,y):
    print(x,y)

if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        function_name = args[0]
        if function_name == say_hi.__name__:
            say_hi()
        elif function_name == add_these.__name__:
            if not len(args) == 3:
                print('You either provided too many or not enough arguements to use this function. ')
            else:
                try:
                    x, y = int(args[1]), int(args[2])
                    add_these(x,y)
                except ValueError:
                    print("One of the arguements provided wasn't a number.")

    else:
        print('No arguement was provided')
