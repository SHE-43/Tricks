def adderFunc(a,b):
    return (a+b)
from dis import dis


print(adderFunc(43,43))
print("\n\n\n")

def forAssembly():
    a = 43;
    b = 1_199;
    c = a+b
    c += 1
    return c


print(dis(forAssembly))