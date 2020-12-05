file = open("basicFile.txt", "w")
file.write("hello there")
file.close()

try:
    a = eval(input())
    print(a)
except: # expression as identifier:
    print("You had an error.")
else:
    print(4/1) # occurs if no errors.

finally:
    print("Finally\n\n")


class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback): # it takes the exception and raises it but it closes the file first.
        try:
            print(f"{type}, {value}, {traceback}")
            print("Exit")
        except:
            print("ERROR handled")
        finally:
            self.file.close()
        # if type == Exception: # this will prevent the exception.
        #     return True

with File("file.txt", "a") as f: # with calls the enter method of the class
   
    try: 
        print("middle")
        f.write("\n\nHello there Class method") # this is the middle
        raise EnvironmentError() # this exception comes after the file is closed.
        # the exception is sent to the exit method as traceback and it is then handled.
        # then over here it exits out.
        # the exit method runs first to see if our code will crash or not.
    except:
        print("Exception handled.")

with File("file2.txt", "w") as f:
    f.write("Hey there")



class Open_File():

    def __init__(self, filename, mode): # class object
        self.filename = filename
        self.mode = mode

    def __enter__(self):        # with
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('sample.txt', "w") as f: # f is the return value of 
    f.write("This is Scafer's tutorial.") # makes changes to the file path passed.
    # When it reaches the end, the exit method runs.

print(f.closed)



# Using function

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f # so that it does not return and finish - that is it. Because close has to follow.
    f.close()


with open_file("sample2.txt", "w") as f:
    f.write("Done using Corey's method mode")

print(f.closed)





