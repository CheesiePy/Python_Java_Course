
def f():
    return 7

def g(x,y):
    return x**y

def s(str, num):
    return str*num

def fgs(str, x, y):
    return s(str,g(x,y))    


def greet(name):
    return f"Hello {name.title()}, thank for asking about me!"

def greetAll(name_array):
    for i in name_array:
        print(greet(i))


def main():
    name = "Maor"
    name.title
    name_array = ["maor","maor","maor","maor","maor", "matan", "tom", "yair", "elad", "emily", "eliko", "ilay"]
    uniq_names = set(name_array)
    greetAll(uniq_names)
    
main()


print()