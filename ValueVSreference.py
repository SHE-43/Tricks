def p(a):
    print(a)

def increment(a):
    a += 1;
    print(f"id of a is {id(a)}")
    print(a)

num = 1

increment(num)
print(f"id of num, {num} is {id(num)}") # this will not change as it is immutable.


def appender(a):
    print(f"id of a {a} is {id(a)}")
    a.append("Lucky Number")
    print(a)

my_list = [x for x in range(1,3+1)]

p(my_list)
appender(my_list)
p(my_list) # list has now changed permanently when passed as reference as it is mutable.
p(f"and the id is {id(my_list)}")

t = (1,2,3)
t = t + (4,3,3)
t = t + (99,) # as only brackets means an integer (immutable object) only.
print(t)


p("\n\n\n")
p("Changing the variable within the method\n")

def cleaning(a):
    print(f"id of a is {id(a)}")
    a = ["New", "List"]
    print(f"id of a is now {id(a)}.")
list_a = [1,3]
print(id(list_a))
cleaning(list_a)


p("\n\n\n")
print("Globals and Locals")


the_number_1 = 6;
the_number_2 = 7;
the_list_1 = [1,2]
def exampleFunction():
    print(the_number_1)
    print(the_number_1 + 100)
    the_list_1.append(23)
    
    global the_number_2

    the_number_2 += 1_000_000 # now, it will change.
    the_number_1_localized = the_number_1
    the_number_1_localized += 1_000
    # the_number_1 += 200 # this gives an exception as te function cannot change it.
    
    print(the_list_1)
exampleFunction()
p(the_list_1)
p(the_number_2)
p(the_number_1)
p("but the local one changed")
