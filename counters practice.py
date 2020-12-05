import collections


print(dir(collections))

a = [x for x in range(1,43)]
b = [x for x in range(1,43)]
c = [x for x in range(1,43)]


print(a)
print(b)
print(c)

a.extend(b)
a.extend(c)

print("\n")
print(a)

col = collections.Counter(a)
print("\n\n")
print(col.clear)

a = [x for x in range(5)]
a1 = ["A", a]

b = [x for x in range(5, 5+5)]
b1 = ["B", b]

c = [ x for x in range(10, 15)]
c1 = ["C", c]

d = [x for x in range(37,44)]
d1 = ["D", d]

print(a1)
print(b1)
print(c1)

# Convert the list of single string and list into one list, please.

def method_1(a1):
    f = a1[0]
    g = a1[-1]
    final = [f]
    for x in g:
        final.append(x)

    return final

print("\n\n\n")
a1 = method_1(a1)
b1 = method_1(b1)
c1 = method_1(c1)
d1 = method_1(d1)
print("\n\n\n")

lists_1 = [a1,b1,c1,d1]

columns = ["First", "Second", "Third", "Fourth"]

print("All clear!!!")

dict_1 = {x:y for x,y in zip(columns, lists_1)}
print("\n\n\n")

for x,y in dict_1.items():
    print(f">>> '{x}' is equal to >>> '{y}' ");

print(dict_1.keys())





