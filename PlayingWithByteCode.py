def adder123(a,b):
    return a + b

print(adder123(1,2))
print(adder123.__code__)
print(adder123.__code__.co_code) # converts it to bytecode.


# At the end of a method, there is always a return None, just in case.
