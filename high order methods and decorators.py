variable_2 = "43"
variable_2 = list( map( int, [variable_2] )  )[0]

v = (chr(variable_2 + 33) + "XYX").lower()
w = 51 if variable_2 < 44 else 9000
print(v, "\n\n" + str(w),"\n\nFUNCTIONS BELOW\n\n")

vvv = 99
#j = str(map(lambda b: b * 7000, vvv))
#print(j)

g = map(lambda x : x * 100, ([a for a in range(3,9)], [a1 for a1 in range(13,19)], [a2 for a2 in range(23,29) ]) )
#print(list(g))



def outer_most(arg_1):
    print("Hey outer_most")

    def middle(arg_2):
        print("Middle")
        a = arg_1 * 100;
        b = a + a
        c = arg_2
        dic = { a:b, b : c } # dic[a]
        inner_1 = lambda arg_3, arg_4, function_1 : f"first >>> {arg_3} second >>> {arg_4} and thirdsss >>> {function_1()}"
        print("inner_1")
        return inner_1

    return middle

# A dictionary that has key and value but the next key is the value of the previous and the value is the key of the previous

def jjj():
    print("HEYOOO")
    return "returned HEYYOOOO"

print(outer_most(43)(55)(12,12,jjj))



def out(func_1):
    def innergy(func_2):
        
        print("THE ANSWER IS")
        return func_2
        
    return innergy(func_1)

@out
def adder():
    return 1+1000000


print(adder())



