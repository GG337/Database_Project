import sys

def say_hi(name: str):
    print(f'Hi! {name}')


def add_these(conf: int,seed: int):
    print(conf,seed)

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
                    conf, seed = int(args[1]), int(args[2])
                    add_these(conf,seed)
                    if conf == 1:
                        print(f'Conference is West Coast and is the {seed} seed. :)')
                    elif conf == 2:   
                        print(f'Conference is East Coast and is the {seed} seed. :)')

                except ValueError:
                    print("One of the arguements provided was a number.")

    else:
        print('No arguement was provided')
