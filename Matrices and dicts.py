def func():
    print("Hamza1")
    return 1

def func2():
    print("Hamza2")
    return 1

def func3():
    print("Hamza3")
    return 1

def func4():
    print("Hamza4")
    return 1

L = [func,  func2, func3, func4]
L1 = [func(),  func2(), func3(), func4()]

f = lambda : func()

def main_1(f):
    return f

print("New beginning")

print(main_1(f = 43))

d = {1: func, 2:func2}
d1 = {1: func(), 2: func2()}
#print(main_1(func))

a1 = [chr(x) for x in range(ord('a'), ord('a') + 6)]
b1 = [chr(x) for x in range(ord('A'), ord('A') + 6)]
c1 = [x for x in range(1, 1 + 6)]
c1 = list(map(str, c1))
d1 = [chr(x) for x in range(ord('G'), ord('G') + 6)]

dict_1 = {x+z : y+w for w,x,y,z in zip(a1,b1,c1,d1)}
c = 0
for x,y in dict_1.items():
    c += 1;
    print(f" >> {c} >>> {x} (x+z) is {y} ( y + w )")

c = 0;

s = "Hey there";
s = [x for x in s if x != " "];

print(s);

def remover(word):
    if word[0] == " " or word[0] is " ":
        word[0] == ""
    else:
        return remover(word[1:])

p = "Hey there"
p = [x for x in p]
print(p)
remover(p)
print(p)


list_matrix = [[y for y in range(1,4)] for x in range(3)]
print("\n\nMatrix\n")
print(list_matrix)
list_matrix.insert(1, "\n")
list_matrix.insert(3, "\n")
print(list_matrix)


