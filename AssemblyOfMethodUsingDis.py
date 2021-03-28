from dis import dis

def adderFunc(a,b):
    return (a+b)

def forAssembly():
    a = 43;
    b = 1_199;
    c = a+b
    c += 1
    return c


dis(adderFunc)
dis(forAssembly)

# The dis (disassembly) method will show you the steps taken by assembly language.
