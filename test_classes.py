import types

def foo():
    print ("foo")

class A:
    def bar( self ):
        print( "bar")

def fooFighters( self ):
    print( "fooFighters")


a2 = A()
a2.m = types.MethodType(fooFighters, a2)

a2.m()


for x in range(9):
    print(x)
    if x == 2:
        break
