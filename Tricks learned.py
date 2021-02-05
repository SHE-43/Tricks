import os; from importlib import import_module
import hashlib
# This is project2.py and Morsels an Dan Bader tricks go here please.

# Use algorithms,
# Move the tutorials to separate file

print("counting")
import_module("time").sleep(1.43)


print(hashlib.algorithms_available)

print(hashlib.sha1("Hamza".encode()).hexdigest())


os.urandom(1024)

gen = (import_module("random").randint(1,43) for x in range(32))

print([x for x in gen])

# Make own variable without manual assigning. Global and local dict

x = 43
globals()["my_variable%s" % x] = "This is made using globals"

print(my_variable43)

locals()["local_var"] = "Local variable"

print(local_var)

# AND

import sys

print(sys.modules[__name__])

this = sys.modules[__name__]
setattr(this, "UsingSys", "SysVariable")

print(UsingSys)

import random



print(random.randrange(65,99,4))
print(random.sample(range(65,92), 10))
f = [chr(x) for x in range(65,78)] # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
RCF = lambda x : random.choice(x)
l1 = [RCF(f)+RCF(f)+RCF(f) for n in range(12)]; 
print(l1);



def fromYield(g):
    yield from g

for x in fromYield(gen):
    print(x)

a = dict() # nested one

b = import_module("copy").deepcopy(a)

exec(f"var_{4} = 23")
print(var_4)
print("MODULES", "\n")
print(print(sys.modules))


# OrderedDict

from collections import OrderedDict, defaultdict, ChainMap

d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for x,y in d.items():
    print(x,y)

d = OrderedDict({1:3, 4:3})
print(d.items())


e = defaultdict(list) # LOL
e['a'] = 1
e['b'] = 2
e['c'] = 3
e['d'] = 4


print(e["e"])

dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'd' : 3, 'c' : 4 } 
chain = ChainMap(dic1, dic2)
print("\n")
print(chain.maps)
print("\n")
print(chain.keys())

print("\n")
for x,y in chain.items():
    print(x,y)

dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
dic3 = { 'f' : 5 } 
  
# initializing ChainMap 
chain = ChainMap(dic1, dic2) 
  
# printing chainMap using map 
print ("All the ChainMap contents are : ") 
print (chain.maps) 
  
# using new_child() to add new dictionary 
chain1 = chain.new_child(dic3) 
  
# printing chainMap using map 
print ("Displaying new ChainMap : ") 
print (chain1.maps) 
  
# displaying value associated with b before reversing 
print ("Value associated with b before reversing is : ",end="") 
print (chain1['b']) 
  
# reversing the ChainMap 
chain1.maps = reversed(chain1.maps) 
  
# displaying value associated with b after reversing 
print ("Value associated with b after reversing is : ",end="") 
print (chain1['b']) 

# https://www.geeksforgeeks.org/chainmap-in-python/?ref=lbp

# itertool to convert lists in to one.


import itertools  
import operator
a = [[1, 2], [3, 4], [5, 6]] 
print(list(itertools.chain.from_iterable(a))) 

# Itertools count

def func(a,n):
    if a<n:
        return # can be used without any other need.
    elif a == n:
        return 0
    else:
        return 1

print(func(5,5))

# Turn this to class so it is only used when a class object is made.



data = [1,2,3,4,5]

try:
    result =  itertools.accumulate(data, lambda x : 4 )
except: 
    print("Not working")



# Meaning of accumulate(iterable: Iterable[_T], func: Callable[[_T, _T], _T]=...) -> Iterator[_T]
#            accumulate([1,2,3,4,5], )   
a = zip([1,2,3,4,5],[7,8,9,1],[1,2,3,45]) # learn the zip class.
# for x,y in a:
#     print(x+y)

for x in a:
    print(x)

import collections
collections.Callable # Check please.
i = [1,2,3,4,5].__iter__()
print(sum(i))
print(sum([1,2,3,4,5]))

# Assert

def assertMethod(sales, returns):
    if sales>returns:
        assert True
    elif sales< returns:
        assert False, "Oh NOOOOO!"
    else:
        raise AssertionError("This is an error")
try:
    print(assertMethod(5,55))
except:
    print("We have assertion error.")

# Single and Double Underscore
# Like function, class returns an object.
# Using lists as variable and using other class objects as arguments for subclasses. Supers as well.
class TestClass:
    pass

# Count from 13 to infinite
counter = itertools.count(start = 13)
for x in range(5):
    if x != 4:
        print(next(counter), end = "--")
    else:
        print(next(counter))

# This will cycle over and over for as much as you want - could have used this in cities.py
cycling_list = [chr(x) for x in range(66,70)]
some_alphabets = itertools.cycle(cycling_list)
for x in range(17):
    if x != 16:
        print(next(some_alphabets), end = "--")
    else:
        print(next(some_alphabets))
        
# islice
names = itertools.cycle(["Mike", "Hollow", "Will", "Biggie"]) # infinite cycle
limited = itertools.islice(names, 0,6) # finite cycle with range 6
for name in limited:
    print(name, end = " ")

def fibonacci_itertools():
    prev, curr = 0,1
    while True:
        yield curr
        prev, curr = curr, prev + curr

print("\n")

f = fibonacci_itertools() # this is an infinite loop
slice_of_f = itertools.islice(f,0,30)

l = len(list(slice_of_f)) # this will use up the whole generator and you are then out.

f = fibonacci_itertools() # this is an infinite loop

slice_of_f = list(itertools.islice(f,0,30)) # Now, a list

reversed_slice_of_f = slice_of_f[::-1]

dict1 = {f"No. {x}": slice_of_f[x] for x in range(1, len(slice_of_f)-7)}
print(dict1)

from functools import partial

just_numbers = partial(filter, str.isupper) # will only contain the ones that are upper
print(list(just_numbers(list(["a","A","B"]))))

upOrLow = [random.choice([str.upper,str.lower])("a") for x in range(14)]

for x,y in zip(upOrLow, list(just_numbers(upOrLow))):
    print(x + " : "+ y)

# Detention - functions as arguments.

a = str.upper
b = str.lower


sentence = "I will not swear in class again. "
sentence = sentence.split(" ")

new_string = "";

# try using functions in a list
# or use a number that randomly changes

for word in sentence:
    new_string += random.choice([a,b])(word) + " "
    # trim at the end

print(new_string)


class ZipMe:
    def __init__(self, *lists): # 
        self.lists = lists # tuple of lists
        number_of_lists = lists.__len__()
        if number_of_lists == 0:
            return 
        
    def check_length_of_all_lists(self):
        # list of lenghts
        # or dictionary of lengths please.
        pass

    def __p__(self):
        return self.lists

a = ZipMe([1,2,3],[1,2,3])
print(a)

x = 10
y = 9


if x:
    class Mod():...
else:
    class Abc():...
    encoding:str

# Formatting

word = "Hey there this is in quotes"
print(f"Check this out as it is in quotes {word!r}.")

int1 = repr(1)
int2 = str(1)

print(type(int1), type(int2))

# ljust, rjust

word1 = "H"
word2 = "M"
word3 = "Z"

print(word1.rjust(2), word2.rjust(3), word3.rjust(4))
print(word1.rjust(2), word2.rjust(3), word3.rjust(5))
print(word1.ljust(2), word2.ljust(3), word3.center(3))


# Zfill

print("12".zfill(5))
print("-3.14".zfill(5))
print("12.12318347834".zfill(34))

# Using underscore to make commas in numbers

a = 1_000_000
print(f"{a:,}")
print(f"{a:,.5f}")


def rot13_weak(message):
    # new_string = [chr(ord('a') + 12 - (ord('z') - ord(letter))) if ord(letter) > (ord('a') + 12) else chr(ord(letter) + 13) for letter in message.lower()]
    return "".join(
        [y.upper() if x == True else y for x,y in zip(
        [True if x.isupper() else False for x in message], 
        [chr(ord('a') + 12 - (ord('z') - ord(letter))) if ord(letter) > (ord('a') + 12) else chr(ord(letter) + 13) for letter in message.lower()])
        ]
        )

def rot13(message):    
    return "".join(
            [letter.upper()
                if boolean == True else letter 
                for boolean, letter in zip(
                    [True if letter.isupper() and letter.isalpha() else False for letter in message], 
                    [chr(ord(letter)-13) 
                            if ord(letter) > ord('m') else chr(ord(letter) + 13) 
                            if letter.isalpha() else letter 
                                for letter in message.lower()])])



print("\n\n\nPropertyMEthodIncomplete")



class GradeClass: 
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def msg(self):
        return self.name + " got grade" + self.grade

hamza = GradeClass("Hamza", "143")
print(hamza.msg())
hamza.msg = "Oh know"
print(hamza.msg)








print("\n\n\nFathers of Python - Method annotations")
# From the Fathers of Python

class Test1:
    @classmethod
    def method1(cls):
        print("Hey there.")

    # Yet another way. using ->
    def conjugator(self) -> complex:
        print("Get Nothing.")

    # A way to add better documentation - from the Fathers of Python.
    def helperMethod(self, n  : "Just n", h: "just h") -> "Nothing":
        print(n)





print("\n\n\nDynamic classes")


# Dynamic Classes

def user_init(self, userName, userAge, userSubjects):
    self.userName = userName
    self.userAge = userAge
    self.userSubjects = userSubjects



# Real example coming up.
# Property methods can be used to change the methods.
# theVariable name is the class name
User = type("User", (), {"total":0, 
                        "name" : "User Class", 
                        "method1" : lambda: print("Hello"), 
                        "__init__" : user_init, # because methods can be assigned as objects.
                        "sayHi" : lambda self: f"Hi, I a {self.userName} and I am {self.userAge} with subjects {self.userSubjects}."
                        }
                        )


print("\n\n\nAny / All")


print(all([1,0,3,4,5]) >= 1)
print(any([1,0,3,4,5]) >= 1)


print("\n\n\ndict using zip and comprehension.")


print({x:y for x,y in zip([1,3,5], [2,4,6])}) # How to make a dictionary using two lists.

avc = "Hazma"
print(avc.__doc__)




print("\n\n\nMore annotations.")

def speed(distance: "This is the distance", time: "Time taken") -> "Kilometers / Hour":
    return distance/time


print(speed.__annotations__)
print("{:,.2f} {}".format(speed(2000000,30), speed.__annotations__["return"]    )) # {:,.2f} gives a comma and only 2 decimal places.


rd = {'type':float, 'units': 'Kilometers / Hour', 'docstring':"Results"}

def f() -> rd:
    pass

print(f.__annotations__['return']['type'])

# LEARN!


def validate(func, locals):
    for var, test in func.__annotations__.items():
        value = locals[var]
        try: 
            pr=test.__name__+': '+test.__docstring__
        except AttributeError:
            pr=test.__name__   
        msg = '{}=={}; Test: {}'.format(var, value, pr)
        assert test(value), msg

def between(lo, hi):
    def _between(x):
            return lo <= x <= hi
    _between.__docstring__='must be between {} and {}'.format(lo,hi)       
    return _between

def f(x: between(3,10), y:lambda _y: isinstance(_y,int)):
    validate(f, locals())
    print(x,y)



condtion = True

x = 43 if condtion else 21


alphabets_till_E = [chr(x) for x in range(ord('A'), ord('A')+5)]
alphabets_till_J = [chr(x) for x in range(ord('F'), ord('F')+5)]
print(alphabets_till_E)
print(alphabets_till_J)
xxx = alphabets_till_J.__iter__()
for index, name in enumerate(alphabets_till_E, start = 101):
    print(f"{index} === {name}")
    print(next(xxx))
    print()


a, _ = (1,2)
a, b, *c, d = (1,2,3,4,5,6)
print(c)







print("\n\n\nDecorators\n")





# A bit about decorators.
# Let's make a property one.

def dec(func):
    def wrapper(*args, **kwargs) -> "args are passed in as (1,2), kwargs are passed in as c = 3, d = 4 (dictionary)" : 
        print("Beginning")
        func(*args, **kwargs) # the same args are opened up from (1,2) to 1 and 2. kwargs are passed in as c, d == 3, 4
        # try yielding as well.
        print("Ending")
    return wrapper

print("\n\nUsing decorators.\n")


@dec
def myFunction(a,b, c, d):
    print(a*b*b*a)
    print(c,d)
    # try with return and yield as well.

t = (3,8)
d = {'c': 3, 'd':7}
myFunction(*t, **d)


print("\n\n\nArgs/Kwargs And Formatting\n")

print(*(4,5,6,7))
mydict = d
print(['{}={!r}'.format(k, v) for k, v in mydict.items()])
f = {"c": "is here"}
print("{1} {0} {c}".format(*("Hamza", "Malik"), **f))

print("\n")
print("{}".format("Yo there"))
print("{!s}".format("Yo there")) # __repr__
print("{!r}".format("Yo there")) # __str__
print("{:,.2f}".format(143333333))
string1 = "hamza"
print(string1.__repr__())
print(string1.__str__())

# As integer ratio

i = 1.01
print1 = (i.as_integer_ratio()[0])
print2 = (i.as_integer_ratio()[1])

print(print1/print2)


import os, datetime, time, pdb, sys
from traceback import print_exc
import traceback


FAKE_FOLDER = r"C:\Data\FolderOne\notepad1.txt"
folder_one = os.path.dirname(os.getcwd())
print(f"dirName : {folder_one}")
print(os.path.dirname(FAKE_FOLDER))
print(os.path.getatime(folder_one))


# Convert EPOCH to actual date.


print(time.gmtime(os.path.getatime(folder_one)))
a = time.gmtime(os.path.getatime(folder_one))
b = datetime.datetime.fromtimestamp(time.mktime(a)) # 2020-09-11 10:42:23
# Only this can be converted using strftime
print(datetime.datetime.fromtimestamp(time.mktime(a)))

c = datetime.datetime.strftime(b, "%B")
print(c)

d = datetime.datetime.strptime(c, "%B") # provide the format it is in.
print(d)


# Easiest way to make a class.


class MyException(Exception): ...
try:
    raise MyException("NOOOOO!")
except MyException as f:
    print("\n\n,", f.__class__.__name__, "\n")
    print_exc()

try:
    os.mkdir("C:\\TestFolder") # Only if it does not exist already.
    
except Exception as e:
    print("We had an error.")
    print("Type is", e.__class__.__name__, "\n")
    print_exc() # same thing as...
    print()
    print(traceback.format_exc()) # this.
 


print(os.listdir("C:\\"))



# Best way possible.
try:
    raise
except Exception as r:
    print(sys.exc_info()[0].__name__)
# Best way possible.

# Creating another custom exception.
class myExc(Exception):
    pass
# Testing it.
try:
    raise myExc("Tis is erroooor")
except Exception as e:
    print(e.__class__.__name__)
    print(sys.exc_info()[0].__name__)

# Creating yet another custom exception
class myExc1(Exception):
    def __init__(self, salary, message = "This is wrong and not working!"):
        self.salary = salary
        self.message = message
        super().__init__(self.message + " as salary is lower than {}.".format(self.salary))
# Testing it.
try:
    raise myExc1("£20000")
except Exception as e:
    print_exc()



# Using j - the imaginary number

number_1 = 23

number_1 = 23j


# Working with dictionaries.

a_dict = {1:'a', 2:'b'}
b_dict_copy_a = {**a_dict} # This is a copy and will not interfere with the above - without copy or deepcopy


#Learn following

# except: expression as identifier:
#     pass

# https://www.geeksforgeeks.org/7-cool-python-project-ideas-for-intermediate-developers/?ref=rp

# https://www.geeksforgeeks.org/python-eye-blink-detection-project/?ref=rp

#https://www.geeksforgeeks.org/python-find-hotel-prices-using-hotel-price-comparison-api/?ref=rp
# https://www.geeksforgeeks.org/flight-price-checker-using-python-and-selenium/?ref=rp
# https://www.geeksforgeeks.org/get-bit-coin-price-in-real-time-using-python/?ref=rp
# https://www.geeksforgeeks.org/memory-management-in-python/?ref=rp
# https://www.geeksforgeeks.org/selenium-base-mini-project-using-python/?ref=rp
# https://www.geeksforgeeks.org/intermediate-coding-problems-in-python/?ref=rp
# https://www.geeksforgeeks.org/python-add-logging-to-a-python-script/?ref=rp
# Output of zip will be a generator.


# This is the one we are working on for now as it is easier to work with.
# Can we make sure it is easy though?
