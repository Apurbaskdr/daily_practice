def my_decor(func):
    def wrapper():
        print ("Brfore decor")
        func()
        print("After decor")
    return wrapper


@my_decor
def hello_s():
    print("Hello!!")
    
hello_s()