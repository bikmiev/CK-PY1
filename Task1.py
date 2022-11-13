from pprint import pprint # TODO решить с помощью list comprehension и распечатать его

num = 16

def foo (num):
    abc_dict= []
    for n in range(num):
        abc_dict.append({"bin": bin(n),
        "dec": (n),
        "oct": oct(n),
        "hex":hex(n)})

    return abc_dict



pprint(foo(num))