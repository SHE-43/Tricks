import timeit

#print(dir(timeit))
f = timeit.timeit()
f1 = timeit.time

print(f"timeitTIME is {f1}")

cache = {0:0,1:0,2:1,3:1}
def fibo(x):
    if x in cache:
        return cache[x]
    else:
        value = fibo(x-1)+ fibo(x-2)
        cache[x] = value
    return cache[x]
print(fibo(103))

cache_list = [0,0,1,1] # O,1,2,3
def fibo_list(number): # number = 3
    # Find Fibo of position 3.
    if number <= len(cache_list): # if 3 <= 4
        return cache_list[number-1] # return cache_list[ 3 ]
    else:
        value = fibo_list(number - 1) + fibo_list(number - 2)
        cache_list.append(value)
    return cache_list[number-1]


d = {'number':[x for x in range(25, 46)]}

print(fibo_list(1))
print(fibo_list(2))
print(fibo_list(3))
print(fibo_list(4))
print(fibo_list(5))
print(fibo_list(6))
print(fibo_list(7))
print(fibo_list(8+1))
print(fibo_list(8+1+1))
print(fibo_list(8+1+1+1))
print(fibo_list(8+1+1+1+1))
print(fibo_list(8+1+1+1+1+1))
print(fibo_list(8+1+1+1+1+1+1))
print(fibo_list(8+1+1+1+1+1+1+1))
print(fibo_list(8+1+1+1+1+1+1+1+1))

print("\n\nMoving on to for LOOP\n\n")

for turn in range(len( d['number'] )):
    print(d['number'][turn])
    print(fibo_list(**d         )) # Changing the format of the dictionary and then opening it, possibly.
    # Unzip the dictionary so that d[number] == 25 (single number) single, like me!


#print(fibo_list(  **d       ))
    

















