# Convert this into a bunch of programs, at least 5, and then save in your personal GitHub.
# Also, take all the other ones as well especially logger, fraction, salesman.
# For the logger, make sure that it uses a new file if the existing one deletes.
# Copy the dictionary fstring app from your programs and paste them here somehow,
# Finally, do the LCD problem - The LCD generator.
# While statement for inputs
# Lastly, converting all numbers to alphabet format. 13 should be thirteen, 126 should one hundred and twenty six.
#           but make it spotless.

# Ultimate guide - https://data-flair.training/blogs/python-interview-questions/ - Ultimate guide
# add collections (all classes), shutil, pandas, numpy, requests, 

# Can this be the best Python tutorial ever? It prints the code it self and then shows what the code is used for?    
# Make one line tutorials and define functions. Make this the best tutorial eve4
# Check which modules are fully imported and which ones are not.
# Start researching amazing projects and OOP and testing project should be done.
# parametrized tests. include your tests in here but don't run them - just leave instructions on how to run them!
# TKINTER for the salesman problem. Make the GPS coordinates using exactly how BBK asked for.
# Do string formatting quizzes and tests, please # Using file objects to extract data, out, on a project that keeps on running
# Perfecting While for integers and strings using functions and try except else finally
# Make most of these into functions, please. Convert most into functions

# 543 AND 599 have PyTz and Timezones available.

# PF = Program related functions (not for tutorial purposes).




import getpass
# Cool way to ask whether username is needed.
if __name__ == '__main__':
    user_name = input("Who are you?")

pass_word = getpass.getpass("Enter your password, please.")

def pass_user_check(user_name, pass_word):

    def user_check(user_name):
        if (user_name == "hamza" or user_name == "Hamza"):
            return True
        else:
            return not True

    def pass_check(pass_word):
        if pass_word == "malik" or pass_word == "Malik":
            return True
        else:
            return not True

    user_acceptance = user_check(user_name); 
    pass_acceptance = pass_check(pass_word);
   
    a = user_acceptance; b = pass_acceptance
    if a and b:
        return 1;
    elif a or b:
        return 7;
    else:
        return 0;

print(pass_user_check(user_name, pass_word))

pass_user_check1 = pass_user_check(user_name, pass_word)

if pass_user_check1 == 1:
    print("Hi Hamza. You're in. Correct username and password")
elif pass_user_check1 == 7:
    print("Hi there. You got one of the inputs right.")
else:
    print("You are not Hamza. \nExiting... Now.\nBitch!\nDo not access me again.")
    import sys
    sys.exit("\n\n\n\t\t\t\t\t\t\t\t\tPython Module Locks; Enabling now.\n\n\n")




print("""

This program is for covering all the checklists made by Hamza Malik.

It is to slowly evolve into the best simple to intermediate to advanced tutorial, ever. 

Modules are available in Python Module Index. For e.g. Math, Calendar, Functools and Random.""")

print("To install a module via CMD, you can do pip module install and you can view all installed modules\
    by writing pip list")

print("Please reduce the number of undefined and unused imports done via wildcard import.")

from random import *
from time import *
import logging

logging.basicConfig(filename="project_main.log", level = logging.DEBUG, format = "%(asctime)s: %(levelname)s:\
     %(message)s") # Good tip for logging

# PF
def d_print(): # This is to add double space
    
    print.__call__("\n\n")
    eee = 10
# PF
def sp(): # This is to add single space
    print()

p_list = ["Harry", "is", "counting", "likeanidiot."]
en = [(x,y) for x, y in enumerate(p_list, 1)]
print(en)
logging.debug("The project has covered enumerate.")



# MAP, FILTER AND LAMBDA
empty_lambda  = lambda: print("Hamza") # an empty lambda function is like def empty_lambda(): print "Hamza"
for_map = [2,3,4,5,6]
list_map = list(map(lambda x:x**2, for_map))
filter_list = list(filter(lambda x: x%2 == 0, for_map))
print(list_map)
print(filter_list)

list_nones = [1,"",3,4,"",5,"",6]
print(list(filter(None, list_nones))) # How to remove Nones from a list using filter.

logging.debug("The project has covered map, lambda, filter.")


# TIME imported via *

a = localtime()
for x in a:
  print(x)
d = ctime()
print(d)
# We've learned that localtime gives you the whole break down and that time.ctime is the current time.
x = perf_counter()
y = time()
z = time_ns()
print(x,y,z)



# Reduce

from functools import reduce # for the reduce function

data1 = [2,3,5,7,11,13,17,23,29]
data1.insert(4, 45)
def mul(x,y):
    return (x*y)
Reduce = reduce(mul, data1)
print(Reduce * 100)
d_print()

logging.debug("The project has covered reduce function from functools.")



# F STRINGS - explained %d%s%.f | 
# Also, format(**names12) 

user = ["Hamza", 143, "Malik", 11.444333]
# .<>f takes the amount of decimal places it needs to take.
print("Hello %s %s. You are roll number %s and fpoint %.2f" % (user[0], user[2], user[1], user[3]))
print('So, {}{}, when did you get put on roll {}'. format(user[0], user[2], user[1]))
d_print()
print("now, we have a dictionary and a very clever way of using it.")
names11 = {'H': "Hamza", 'M': "Mark", 'E': "Ego"}
names111 = "Hey. My name is {0[H]} and {0[M]}, {0[E]}".format(names11)
print(names111)
flist = ["Hamza", "Hamna", "Mark"]
print("The room is with {0[0]}{0[1]}{0[2]}".format(flist))
# The above is to extract stuff from dictionaries and lists to make a string work.
names12  = {'H': "Hamza", 'M': "Mark", 'E': "Ego"}
names121 = "I am {H},{M} & {E}.".format(**names12) # No idea where the ** came from. 
# names121 explained; .format(**names12) is for dictionaries. If the key is a string, do not use inverted commas in the F string
print(names121)
results12 = [1,2,3,4]; p_results12 = [5,6,7,8];
for result,p_result in zip(results12,p_results12): # Good tip
    print('{:3}{:20}'.format(result,p_result)) # This will give you a strange format.


# Zip and unzip dictionaries

def unpack_dict(a,b,c):
    print(a+b+b)
packed_dict = {"a":23, "b": 444, "C": 5665}

unpack_dict(**packed_dict)



# Zip and Unzip via function # Good tip

zipped = zip(["A","L", "C"],[1,4,3]) # we combine the list
def unzip_zipped(zipped): # Good tip
    n,m = zip(*zipped)
    n_m = list(zip(*zip)) # this one might not work.
    return f"The zipped {list(zipped)} is now broken to {n} & {m} or as a new list, {n_m}."



# Matrix rows to columns conversion | Also using zip and unzip.

matrix_of_doom = [[-1,20,3,4,5],[-3,40,5,6,7],[-8,70,6,5,4],[-4,50,6,7,8],[-10,100,10,10,10]]
print(list(zip(*matrix_of_doom))) # this will give a version of the matrix with rows as columns and columns as rows

for x in range(1,12): # Good tip
    print("I am number, {0:02} and {0:04} and {0:05}". format(x))
# This means that the placeholders (Curly) let you format the number from within. 
# More to learn about there.
# Placing commas in big numbers.
print("I am {:,.2f} years only".format((1000**2 + .43))) # The thousand separators are there, with 2 decimal places as well.
# Using commas to create thousand separators. 
a = f'1MB is equal to {1000**2:,.2f}'
b = "1MB is equal to {0:_.2f}".format(1000**2)
format_with_commas = f"{123123123:,}" # this will automatically do it. % will not.


# Basic addition and subtraction game - fill in the missing float.

Ex_A = 1.43322 + 2.56678; print(Ex_A); Ex_B = 3.14356 + 0.85644; print(Ex_B); Ex_C = 3.01231334 + 0.98768666; print(Ex_C); 
Ex_D = 2.11134788 + 1.88865212; print(Ex_D); Ex_E = 8.44331123143 + 1.55668876857; print(Ex_E); Ex_F = 7.31261943143 + 2.68738056857; print(Ex_F)
Ex_G = 00000000343.43 +  1.57 ; print("Ex_G, when 343.43 needs to be made a full 345.00, the answer is..", Ex_G)
Ex_H = 3.0000034 + 0.9999966; print("Ex_H, the final one is:", Ex_H); Ex_I = 0.01846271931 + 3.98153728069; print(Ex_I)
Ex_J = 2.95186638474 + 1.04813361526; print(Ex_J)


# A method/function that does the same as above - just for mental math skills, that's all.


def fill_in_missing_one(x = None):
    import random
    import time

    a = random.random()
    print("we have =", a)
    time.sleep(2.43)
    print("Bring it up to 4.0")
    time.sleep(2.43)
    answer = input("Type your answer.")
    time.sleep(2.43)
    if float(answer) + a == 4.0:
        return "Good Job!!!"
    else:
        print("Your answer:",answer)
        print("Mine answer:", 4-a)
        return "You still suck!!!"



# Sets, unions, intersection, not common and subtraction
set_A = {x for x in range(1,15)}
set_B = {x for x in range(1,16) if x % 2 != 0 if x > 3}
def set_compare(set1, set2):
    intersection = set1 & set2
    union = set1.update(set2)
    not_common = set1 ^ set2
    return intersection, union, not_common



logging.debug("The project has covered fstrings as well..")

# A function that counts and prints numbers that are bigger than their neighboring ones.

zed = [int(i) for i in input()] # Good tip
def lower_or_bigger(zed):
    nums = []
    counter = 0
    for i in range(1, len(zed) - 1):
        if zed[i - 1] < zed[i] > zed[i + 1]:
            counter += 1
            nums.append(zed[i])
    print(counter, nums)



d_print()
# JOIN AND SPLIT makes list to string and string to list. 
# Convert a list of strings and integers to a string, in one line.
list_of_intandstr = [1,5,"H",21, "R",44,45,46,"W"]; 
string_of_intandstr = ",".join(list(map(str, list_of_intandstr))).replace(",","");  # Converting the list to a string of numebrs and strings altogether.
print(string_of_intandstr) # this will give you the string of qth list full of integers and strings, right away. 
# We skipped, or just mashed in one line, many steps.
# Another way with a different example but done in steps to understand with ease. 
X = ["A","B","C"]
X = ",".join(X) # the comma on the left is to tell Python to remove comma and join the dissected string.
X = X.replace(",", " ");
# this is to be added on the page itself and we can then escalate .
# and now do not have the page itself.
print(X) # just a bit of split, join and replace.
# And, finally, once again...
# When you've a list of integers and you want to join them together - BUT join only lets you do that to a list of strings.
list_of_integers = [1,4,3,2,5,6,7,22,3,4,55,66,34]
list_of_strings = list(map(str, list_of_integers))
list_of_strings = ",".join(list_of_strings)
list_of_strings = list_of_strings.replace(",", "")
list_of_strings = (",".join(list(map(str, list_of_integers)))).replace(",", ""); print(list_of_strings)
d_print() # This means that we are moving on to a new topic.


# Print formats and nested loops
# Q. Form a nested loop for multiplication.

print("Below, we're going to make a column and row of a 4 by 4")
for x in range(4):
    for y in range(4):
        print("O", end = " ")
    print() # this cancels it out, entirely.
ghazi = choice([x for x in range(1, 9)])
x = ["Ghazi is more than 5 or just 5" if ghazi >= 5 else "Ghazi less than 5"]
x = x.pop()
print(x)
print("ID", id(x)) # ID of variables
d_print()

listrandom = []
for x in range(100):
    listrandom.append(randrange(143))
print("range of random 100 numbers.")
print(listrandom)
print("One number out of the above 100.")
print(choice(listrandom))
print("10 numbers that have mean 2 and standard deviation of 3.")
for x in range(10):
    print(normalvariate(2,3))


# Make a random list of numbers of your choice using a 'set' of numbers

seq1 = {x for x in range(56,72)}



# Finding one odd from even list or one even in odd list

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]


# Multiplication loop.
# From 1 to 10.
def tables(factor):
    i = 1
    while i < factor[-1]:
        for x in factor:
            print("  ",(i * x), end = "\t")
            if x == factor[-1]:
                i = i + 1
                print()
    print("The above is a table holding multiplcation of integers from 1 to 10, each multiplied to each digit from 1 to 10.")            


# Intersting looping style. Weird one, really.
for x in "______________":
    print("xxx") # This counts as long as the number of underscores.

# Sorting.

unsorted = [3,2,6,7,1,2,4,9]; print(sorted(unsorted))
unsorted.sort()
lii_1 = [-4,1-5,6,3,4]
slii_1 = sorted(lii_1, key=abs)
dictionary_for_sort = {}
tuple_11 = (4,5,2,8,9,2,1,3,6)
print(sorted(tuple_11)) # this will sort the tuple and return a list. 


# List, input and split.

print([int(x) for x in input().split()])
# This one takes an input and splits it into a list, by itself.


factor = [x for x in range(5, 16)]
# Now, how can we print factors of a given number or set of numbers?
a = 100
numberlist = [x for x in range(1,(a+1)) ] # try with a generator.
factors = []
for x in numberlist:
    if a % x == 0:
        factors.append(x)
if len(factors) == 2 and factors[0] == 1 and factors[-1] == a:
    print("a is a prime number")
else:
    print(factors)

list_of_strings_numbers = [235, 'AJK', 'AAA', 'KKK', 789, 'JJJ', 'QQQ', 101010, 'JQK']
# We need to arrange them by first breaking them all in on list - ASSIGN1
# We need to rearrange them according to the sum of their elements ascii value (encoding);
# for example, ord("A") = 65
# First, convert to string
list_of_strings_numbers = list(map(str, list_of_strings_numbers))
list_of_strings_numbers = sorted(list_of_strings_numbers, key=lambda k: sum(ord(c) for c in k))


#uniform
for x in range(10):
    print(uniform(2,11))
print()
print("and now with basic methodology, Uniform.")
print(uniform(3,10), "! uniform") # This prints a float between 3 and 10.
print(round(uniform(3,10)), "uniform, rounded.")

list2 = [x for x in range(10)]
print(list2)
shuffle(list2) # Shuffles the list 'list2'
print(list2) # print the shuffled list.
print(randrange(0,4300,43)) # Generates a random integer multiple of 43 between 0,4300
print(randint(5,101)) # generates a random integer between 5 and 101
print()
print(random()*43) # Generates a random number between 0,43

# Make a list using the string you already have here.

Split_String = [x for x in "Hamza"]; print(Split_String) # split a string on just one line.

# Random password selection, please! QQQ

# GENERATORS

print("Here we have a generator that stores data")
def gen(x):
    for x in range(x):
        yield x**2 + 3
for x in gen(10):
    print(x, end = " ")
print()
print("More on generators and why we they are used,") # Corey Schafer.

def gen2(y):
    for x in range(y):
        yield (x * 1000)
numss = gen2(20)
for x in gen2(20):
    print(x)
 
def gen3(x):
    for a in x:
        yield a*a
gen3_list = gen3([x for x in range(5)])

# the print next(gen3) does not work QQQ # Corey.
print()
print()


# Fibonnaci using recursion and with cache


dic = {}
def fib(n):
  if n in dic:
    return dic[n]

  if n ==1 or n ==2:
    value = 1
  else:
    value = fib(n-1) + fib(n-2)
  dic[n] = value
  return value

print(fib(400)) # Prodigy # 
# or import lru_cache from functools and then write @ lru_cache(maxsize = 1000)
# Logging and it's notes.
# Open all programs in Python memory.

from os import getcwd, listdir, walk, chdir, path, environ
print("The following is the directory we are currently in.")
current_dir = getcwd()
print(current_dir)
print("The following is the list of files and folders in", current_dir)
print(listdir())
print("We are changing our directory to something easier, for testing purposes only.")
chdir(r"C:\Users\ABC\Desktop\PROJECTS\MODULES\\")
print("Using OS.WALK, we can print all that is there. ")
oswalk = walk(r"C:\Users\ABC\Desktop\PROJECTS\MODULES\\")
print(oswalk)
print("Now, this is going to show Paths, Directories and Files.")
print()
for paths, dirs, files in oswalk:
    print("Paths:", paths)
    sp()
    print("Directories", dirs)
    sp()
    print("Files", files)

path1 = getcwd() # just to get the directory again,
print(path1) # print the current directory
print(path.split(path1)) # Just a more neater way to print the path and file/folder separately. 
print("This is to check whether the file name is a file or a folder")
print(path.isdir(r"C:\Users\ABC\Desktop\PROJECTS\\"))
#  You can use walk and then this in a recurring function to open and extract all that are notepad files. 
print(path.exists(r"C:\\")) # Check if path exists.
print("To find all path methods, dir(path)")
print("""makedirs("STATISTICS", 0o666)""") # This is how you add multiple directories

# THE ALL USERS PROGRAM DATA # The Home path
all__users = (environ.get("HOMEPATH"))
print(all__users)

# TO EFFICIENTLY CREATE A FILE PATH. besides using OS.WALK()
new_path_1 = path.join(all__users, "thisnewfile.txt") # this won't create a new path rather just give 1.

# Path finder # Not for duplicate files, but could be
exee = "made1.txt"
for x,y,z in walk(r"C:\Users\\"):
    if exee in z:
        print(x,y) # This will give you the path of the small file you are looking for.
        print(path.abspath(path.join(x,exee)))

print(path.isdir(r"C:\Users\\")) # checks if this a dir
print(path.isfile(r"C:\Users\\ABC\Desktop\PROJECTS\MODULES\OS\made1.txt")) #checks if this is a file

d_print()

# Opening a file from os and then renaming it using a function called rename1 - Try


# DATETIME



print("Now, we experiment with the datetime module.")
import datetime
today_date = datetime.datetime.today()
print(today_date.isoweekday()) # This will print the number of weekday it is.
print(today_date.weekday()) # This will give one int less than isoweekday as it follows PY list index.
bday_mine = datetime.date(2020, 4, 30)
date_of_today = datetime.date.today()
delta_t = bday_mine - date_of_today # this give you the number of days left till your Birthday = strippin timme!
seconds_left = delta_t.total_seconds # seconds left till bday
date_after_bday = bday_mine + datetime.timedelta(days = 43) # date, 43 days, after my bday.
# date plus time delta = new date ||| date - timedelta = new date.


date1 = datetime.datetime(2016, 11, 26, 16, 30, 00) # PRINT THE DATE AND TIME, JUST THE WAY YOU WANT IT TO BE
print(date1)
a = (2012, 3, 14, 12,30,45)
my_date = datetime.datetime(a[0],a[1],a[2],a[3],a[4],a[5])
sentencewithdate = "{:%B %d, %Y}".format(my_date)
# Use fromtimestamp and strf and timezones.
dtdt = datetime.datetime(2012,12,12,12,14,20)
print(dtdt)
print(datetime.date(2019,2,3))
print(datetime.time(19,2,43,43))
print(datetime.timedelta(2,3.3,4,5,6,7,8), "The amount of time passed with regards to entered.") # This tells you the amount of time passed. (days,secs,micro,milli,mins,hours,weeks)
print(datetime.timedelta.max, "The max.")
print(datetime.timedelta.min, "The min.")
print(datetime.timedelta.resolution) # (days,secs,micro,milli,mins,hours,weeks)
a = (datetime.timedelta(hours = 24, seconds = 143)) # the first entry to the amount of time spent
b = (datetime.timedelta(hours = 48)) # The next entry to the time spent.
print(b-a, "This is the answer!")
print(datetime.timedelta(days=-1, seconds = 68400)) # this one



#CONVERT TOTAL SECONDS TO EPOCH   # amount of seconds, days or minutes passed used a timedelta against time min.



the_time1 = datetime.datetime(2019, 11, 26, 18, 38,43) # this is a timetuple.
print(the_time1)
the_time = time() # this gives the time since 01-01-1970 in seconds
print(datetime.datetime.fromtimestamp(the_time)) # this converts the seconds to date
ts = datetime.datetime.fromtimestamp(the_time).strftime('%Y-%m-%d | %H:%M:%S') # Format the date.
print(ts)
# OR
print("{:%B,%d,%m   %H::%M::%S}".format(the_time1))

# strftime vs strptime - datetime.datetime.strftime(datetime.date.today, ("%d%m%y"))
# datetime.datetime.strptime("24/12/2019", "%d%m%Y") this is how it all works.



# Converting a year into seconds. 
tot = datetime.timedelta(days = 365)
print(tot, "YEAR!!!")
print(datetime.timedelta.total_seconds(tot))
print(datetime.timedelta.total_seconds(datetime.timedelta(minutes = 1000*2))) # Converting years to seconds.



# Scope | Globals | Locals
if "tot" in globals():
    print("YES")
try:
    print(datetime.date.today())
    shitime = (time.gmtime(x))
    print(shitime)
    xxxx = time()
    print(datetime.datetime.fromtimestamp(xxxx))
except:
    print("We will fix this later.")
    logging.warning("Line 377 has a problem.")



# Timezones (basics)
import pytz

today_date = (datetime.datetime.today())


d111 = datetime.datetime.now(tz=pytz.UTC)
dt11 = datetime.datetime(2019,12,5,15,39,43,43000, tzinfo=pytz.UTC)
print(d111.astimezone(pytz.timezone("Europe/London")))
print(dt11.astimezone(pytz.timezone("Australia/Melbourne"))) # first we make it aware of timezones.
print(dt11.astimezone(pytz.timezone("Australia/Melbourne"))) # And then cause another frenzy fok tuime

# GOT PAKISTAN TOO.

todayy = datetime.datetime.now()#(tz=pytz.UTC)
print(todayy.astimezone(pytz.timezone("Asia/Karachi"))) 
# Make UTC aware by adding or minusing hours.

#ALL TIMEZONES

for tzz in pytz.all_timezones:
  print(tzz)

import time; print(time.localtime()); print(time.localtime(1)); time.asctime() # just a reminder
time.localtime() # this gives current time
time.localtime(200000) # this gives current time according to seconds entered from Epoch time.



# CALENDAR
import calendar
#print month of year
January2019 = calendar.month(2019,1,4,1)
print(January2019)
# check leap
year1 = 2019  
print(calendar.isleap(year1))
# try for multiple (2000-2019)
for x in range(2000, 2020):
    print(x, calendar.isleap(x))

print(calendar.calendar(2019)) # prints the calendar with dimensions year width length.
print(calendar.day_abbr[4]) # Day abbreviation
print(calendar.day_name[2]) # Day full
print(calendar.February) # Number of month
print(calendar.leapdays(2000,2090)) 

print(calendar.monthlen(2019,4)) # Length of month
print(calendar.monthrange(2019,4)) # Length of month
print(calendar.nextmonth(2019,3)) # Next month
print(calendar.prcal(2011,1)) # Just prints the god damn calendar of year suggested and month

d_print()



# Reading and writing files. Then deleting the evidence. #Make Python interesting. 
print(getcwd())

try:
    f = open(r"""C:\Users\ABC\Desktop\PROJECTS\RW\ROUGH\N1.txt""", "w")
    f.write("This is the 1st sentence.")
    f.close()

    f = open(r"""C:\Users\ABC\Desktop\PROJECTS\RW\ROUGH\N1.txt""", "r")
    for data in f:
        print(data)
    f.close()

    f = open(r"""C:\Users\ABC\Desktop\PROJECTS\RW\ROUGH\N1.txt""", "r")
    f1 = open(r"""C:\Users\ABC\Desktop\PROJECTS\RW\ROUGH\N2.txt""", "w")
    for data in f:
        f1.write("NEWLY COPIED")
    f1.write(data)

    f1.close()
    f.close()

    f1 = open(r"""C:\Users\ABC\Desktop\PROJECTS\RW\ROUGH\N2.txt""", "r")

    for data in f1:
        print(data)
    f1.close()

    print(listdir())
    remove((r"""C:\Users\ABC\Desktop\PROJECTS\RW\ROUGH\N2.txt"""))
    chdir(r"""C:\Users\ABC\Desktop\PROJECTS\RW\ROUGH\\""")
    print(listdir())

    f = open(r"""C:\Users\ABC\Desktop\PROJECTS\RW\ROUGH\N1.txt""", "a")
    f.write("\nThe file has been deleted for good, me lord.")
    f.close()
except:
    print("That did not work")
    logging.warning("File opener and copier from 420 has a problem.")

# with open closes the file all by itself.
# Reading and writing files on the same notepad file and CSVs (write the differently. )


# This one has a problem, for no reason at all.


# IMPORT MY OWN



from fun import * 
print("We've imported our own function and used it for raising the power, max element and Fibonnaci")
print("The square, max of list and fibonnaci")
print(square(33, -2))
print(maxx([1,6,22,4,5,45,67,33,55,6]))
print(fibonnaci(6))



# IMPORTING A Python FILE THAT IS NOT IN THE SAME DIRECTORY, BITCH.



print()
print("We put a file in the folder within the same directory and imported using MODULES.dick (The name of it.)")
print()
import RW.importing
print()

# Appending a path of directory. 


# IMPORTING A FILE THAT IS IN A COMPLETELY DIFFERENT DIRECTORY, CALLED BIRKBECK



import sys
print(getcwd())
sys.path.append(r"C:\Users\ABC\Desktop\BIRKBECK") # Changees the directory.
print(getcwd())


print(sys.argv) # This will print a list of arguments you enter in the command line. 
print("there are 2 ways of changing the directory, SYS and OS. ")

# The below changes the way it outputs or prints
sys.displayhook = lambda x: print ("Yo", x) # This will print a tuple of "YO" and whatever you've typed in the parameter sector.
# More about the printfunction
def print_function(*objects):
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) # this is the basic syntax of the print function.

print_function("hamaz", "is", "here", "to", "make", "it", "happen")

sys.modules.keys() # gives all the modules that we've printed.

before = [m for m in sys.modules]
import numpy
after = [m for m in sys.modules]
print([m for m in after if m not in before])

# <<<<<<<<<<<>>>>>>>>>>>>
# Finally, Except, Else, Try.
from string import ascii_lowercase
alphas_1 = [x for x in ascii_lowercase][1:5]
rand_list_num = [x for x in range(1,5)]
main_list_1 = alphas_1 + rand_list_num
shuffle(main_list_1)

try:
    x_x = choice(main_list_1)
    logging.debug("The PC has chosen", x_x)
    if type(x) == int:
        print("1")
    else:
        raise ValueError("Wrong.") # This is to happen if the value is wrong.
except NameError:
    print("This is only raised when NameError is raised.")
    logging.debug("At 514", x_x, "was chosen by your laptop, NameError.")
except:
    print("A letter was given by the user.")
    logging.debug("At 514", x_x, "was chosen by your laptop. NameError.")
else:
    print("So, this else works if try works.")
    print(x_x)
    logging.info("The file copier at 513 worked and your laptop chose", x_x)
finally:
    print("This will happen regardless of the above.")
    print(x)
    print("If try and else used, it will print the number you entered,\
        however letter will be printed if error raised." )
    logging.info("The file copier at 513 worked and your laptop chose", x)

d_print()


import math; print(dir(math)); print(math.isfinite(float("inf"))) # The infinite number

print(math.isinf(float("inf")))

a = float("inf") # this is a representation of infinity. 
b = float("-inf")
print(type(a))
print(math.e) # prints the value of Euler's number.
print(math.exp(4)) # Exponential value of e raised to 4.
print(math.log2(3))
print(math.log10(3))
print(math.ceil(1.54)) # finds the next number to come after the whole number. 



# Eucledian Distance of A and B
point_A, point_B = (1,2) # similar to x1,y1 # 1
point_Q, point_R = (7,9) # similar to x2,y2 # 2
EUC = math.sqrt(((point_A-point_Q)**2) + ((point_B-point_R)**2))
print(str(EUC)+ ", the Eucledian distance.")

# Find full sum of an iterator
iterX = iter([44,55,66])
print(math.fsum(iterX)) # this will print the full sum of iterator.
# again
iterY = [1,2,3,4,5].__iter__()



# Generator function # Part of iterables.

def gen_fun1(x):
    for y in range(x):
        yield y

ass11 = gen_fun1(20)
print(next(ass11))
print(next(ass11))
print(next(ass11))



# Dictionary comprehension.
A_11 = ["A","B", "C", "D"]
A_12 = [1,2,3,4]
A_dic = {x:y for x,y in zip(A_11, A_12)}
print(A_dic)
dic_list = [(x,y) for x, y in A_dic.items()]
print(dic_list)

# Another one.
d11 = {1: 143, 2: 243, 3:65};

for x, y in zip([f for f in range(1, d11.__len__() + 1)], d11.items()):
    print(x,y)



# Dictionary in dictionary. 

dic_in_dic = {"H": {"name": "hamza", "age": 23}, "H1":{"name": "Hamna", "age": 10}}; print(dic_in_dic)
# We will work on this later. 



# Dictionary which has lists as values and keys as normal

Dict1 = {

    "Hamza" : ["Lahore", "London"],
    "Marcel": ["Spain", "London"],
    "Farhana" : ["Islamabad", "London"]
    
    }
Dict1["Hamza"].append("UK based only.")
print(Dict1)
d_print()



# SPAWN ALL LETTERS IN ASCII (CAPITALS, LOWERSs)

from string import ascii_lowercase, ascii_uppercase, ascii_letters, printable
print(ascii_letters, ascii_lowercase, ascii_uppercase)
print(printable)
joined_everything = ''.join([chr(i) for i in range(128)])
print(joined_everything, " ... everything you need!")
test_list = []
alpha = 'a'
for i in range(0, 26): 
    test_list.append(alpha) 
    alpha = chr(ord(alpha) + 1)
print(test_list)
lowerr = (ascii_lowercase)
stringgs = [x for x in lowerr]




#Enumerate
import itertools
STRx = ["A","B"]
def my_enumerate(x, start = 0):
    counting = itertools.count(start)
    return((next(counting), y) for y in x)

# OR 

STRx = ["A","B", "C"]
def my_enumerate(strx):
    for x,  y in enumerate(strx, 1):
      print(str(x) +  " " +  y)
(my_enumerate(STRx))



# Comprehensions of Lists, Sets, Dictionaries.

# Lists' Comprehensions.
# DEL statement. 
w_list = ["   H   ", "    a    ", "    m    ", "     z    ", "     a    "]; 
del w_list[2] # the DEL statement. 
print(w_list)

# the above list has got spaces on each element's left and right.
print([x.strip() for x in w_list]) # space has now been removed. 
unusual_string = "Hamza Malik, Mark Adams, Marcel Blanes."
print([x for x in unusual_string]) # this will divide all the letters,single strings and the spaces and comma.
print([x for x in unusual_string.split()]) # this is more suitable as it will just split the list. 
print(unusual_string.split()) # This will divide the names.

another_list = [1,1,1,2,3,3,3,4,4,4,5,5,5]
# remove duplicates without using a set.
print(list(dict.fromkeys(another_list)))

# Also, list comprehension with x,y within square brackets


# Dictionary comprehension
A_11 = ["A","B", "C", "D"]
A_12 = [1,2,3,4]
A_dic = {x:y for x,y in zip(A_11, A_12)}

# Find dictionary key by value can be done my making function or without it as well.

def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

# Finding max of list but with another key
list65 = [(1, "H"), (2, "B"), (3, "D")]
print(max(list65, key = lambda k: ord(k[1])))
# Meaning k is the element and ord is the ascii value of that string in element/tuple
list66 = ["hamza", "is", "studying"] # find most scoring in terms of alphabet position
print(max(list66, key= lambda k: sum(ord(c) for c in k)))


# Finding size of list in memory:
L123 = [4,8,1,9,3,5,7]
L1234 = [x + 2 for x in L123]
L1234.append(1431); L1234.append(1432); L1234.append(1433)
print(L123.__sizeof__())
print(L123.__le__(L1234)) # Checks whether the object is le (Lesser or equal than) argument object.
print(L123.__ge__(L1234)) # Checks whether the object is le (Lesser or equal than) argument object.

# These can be used to check whether the length of one list is growing more than the other one.

# Finding length in several ways - how the system works from within.
    print(L123.__len__()); print(len(L123)); print(list.__len__(L123));
#   The double underscore; The usual method; Using class to call a method that takes it's instance as argument.
# Something like:
"""
class list:
    def __len__(L123)

"""



# Sorted Dictionary by value when values are numbers and counting # Good tip

dict_unsorted = {x:y for x,y in zip(["H", "a", "m","Z", "a"],[55,6,34,1,2])}

def dict_sorted_by_values1(dict_unsorted):
    return {a:b for a,b in sorted(dict_unsorted.items(), key= lambda i:i[1])}

def dict_sorted_by_values2(dict_unsorted):
    try:
        import operator
        return sorted(xs.items(), key=operator.itemgetter(1))
    except:
        print("Seems to be a problem, nerd.")



# Sets
set_com = {x for x in range(12) if x % 2 == 0}; print(set_com)
set_skip = {x for x in range(2,30,4)}; print(set_skip) # this one skips a few steps
set_com.update(set_skip) # to add a list or set to another set.

fruits = {"apple", "banana", "cherry"} # remove and discard
fruits.discard("banana")
fruits.remove("apple")


# Turn dict keys to list

dictionary_1 = {1 : "H", 7:"jj", 67:"UXU"}
list_of_keys = list(dictionary_1.keys()) # the same can be done for items as well



# Identical or same elements in list
list76 = [1,1,1,2]; print(list76[1:]==list76[:-1]) # Not same
list77 = [1,1,1,1]; print(len(set(list77)) == 1) # Same, with another method



# How to check whether an instance is a certain class. 
string___1 = "ABC"; print(isinstance(string___1, str))
list___1 = [1,2,3]; print(isinstance(list___1, list))
gen__1 = (x for x in range(20)); print(isinstance(gen__1, tuple))



# Using this and random to make roll numbers or something else.





# You know, you can copy paste the actual code in the three '"""' and then print what you are doing. 

# Command line, Recursion question - regain from quiz. When you're free to do so.


# SYS, OS (almost done.) and NUMPY and Arrays (Telusko)

""" We have file 1 file 2 and file 3 - We have our lists in file 1, imported to main file 2.
Then, we edit the lists within here. In file 3 we have a list joiner. That we can use to edit the file 1 lists."""

# Integrate with WXPython, OS and SYS.

# This cannot include the SYS Command Line argument as yet. 

# Subprocess? No idea.

# XRANGE # Not in builtin functions

# Decode a b byte size string.

bstring = b'Hamza is here'
bstring = bstring.decode("utf-8")
print(bstring)


# HIGHER ORDER FUNCTIONS

import inspect

def total_one(x,y,z):
    return x+y+z

inspect_1 = (inspect.getargspec(total_one)) # this will print out the number of arguments it can take. 
# check how many arguments a function is assigned to take. 
inspect_2 = (inspect.getfullargspec(total_one))
print(len(inspect_2[0])) # this wll give the number of variables in a given method.

# Another way using (inspect.signature)

kilo1 = inspect.signature(total_one)
kilo1 = kilo1.parameters
print(kilo1["x"])
print(len(kilo1)) # this will also give you the number of arguments in the function.


# Weird chr and ord

print(chr(639),chr(699),chr(678),chr(643));



# Globals; are all the variables, methods and functions you've used in the main program,
# Locals; are all the variables you've made in functions. 
# If a variable is similar to a global, for example, a = 10 outside, 
# but a = 5 inside, the code, globle a will make a = 5 the main one.

if "eee" in locals(): # Remember to use commas to find the variable
    print("True")
else:
    print("False")

if "eee" in globals(): # Remember to use commas to find the variable
    print("True")
else:
    print("False")

if 'bstring' in globals(): # Remember to use commas to find the variable
    print("True")
else:
    print("False")
# So, this is amazing. With the locals, we can check whether there is a variable in any of our functions there.


ii = 15
def func22():
    global ii # This will use the one assigned outside.
    ii = 143
    print(ii) # this will print ii as the one assigned as the global one inside the function.
print(ii)
func22()

# FINALLY

pop = 143
def pop1():
    pop = 14
    print(id(globals()["pop"]))
    print(pop)
print(id(pop))



# Writing a file that counts the number of times this python file has been run.



x = (path.getctime(r"C:\Users\ABC\\"))

# 1563878655.3978593
print(datetime.date.today())

shitime = (gmtime(x))
print(shitime)
import time # Good tip
xxxx = time.time()
print(datetime.datetime.fromtimestamp(xxxx)) # Found it, bro.

# Another way of finding out the amount of time a function took


import timeit

def fibonacci12(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci12(n-1) + fibonacci12(n-2)
    
timeit.timeit('fibonacci12(35)', globals=globals(), number=1)

# PLAYING AROUND WITH VARIABLES AND AWESOME TECHNIQUES.

mm,nn = (1,2)
print(mm)
print(nn)
xn, _ = (22,33) # an underscore can be used as a variable name.
print(xn)
print(_)
a_, b_, c_, *d_ = (1,2,3,4,5,6,7,8,9,10) # the * will cover all the rest of the values for d. abcd will cover the 1st four.
#or
_q,_r,*_s, _t, _4 = (1,2,3,4,5,6,7,8,9,10,11)
print(_4)
print(_s)

jjj,kkk,lll = 1,4,3; print(jjj,kkk,lll)
try:
    jjj,kkk,lll = TTT # this will NOT work, however, refer to the one below,
except:
    print("will not work.")
TtT = jjj,kkk,lll; print(TtT)



# OOP 1

# When there is an object."something", that means attribute. 
# When there is something.something() - it means class.function/method(argument), for e.g. list.append("2") (self brings list out already.)
# When a = [1,2,3], a is an object of list class. So, a.append(2) - append is a function

class Human():
    pass

Hamza = Human() # is now an object of the Human class.
Hamza.first = "hamza" # first is an attribute and it's value is "hamza"
Hamza.last = "malik"
print(Hamza.first)
print(hasattr(Hamza, "first")) # Check if an object has a certain attribute. 

setattr(Hamza, "role", "Programmer")
setattr(Hamza, "backup", "{:,.02f}".format(4000000)) # this is amazing.
print(hasattr(Hamza, "role"))
print(hasattr(Hamza, "bodysize"))


class Person():
    pass

hamza = Person()
hamza.first = "Hamza"
hamza.last = "Malik"
hamza.sis = "hamna"
b = hamza.sis
print(b)
print(hamza.sis) # this is what setattr does, basically.


pay_key = "pay"
pay_val = 45_000; print("{:,}".format(pay_val))
# Over here, we have to set pay as the attribute and 40000 as the value.
# What to fucking do?
hamza.pay_key = pay_val


# We can use setattr.
setattr(hamza, pay_key, pay_val)
print(hamza.pay_key)
print()
pay = getattr(hamza, pay_key)
print(pay)

setattr(hamza, "Name", "MALII") # Although, you've done them in commas, they will be printed without as of syntax.
print(hamza.Name)
xxx = getattr(hamza, "Name") # But this is to avoid using hamza.Name, rather just one variable. 
print(xxx) # These all work in their own ways.

dic = {"sex":"Male", "height": "tall"}
for x,y in dic.items():
    setattr(hamza,x,y)

print(hamza.sex)
print(hamza.height) # So, we can get things put in a dictionary, like US and UK style and then found.
setattr(hamza, "car", "Mercedes E350")
# GET CLASS OF INSTANCE AS A STRING / __name__ gives the name of a class
print(hamza.__class__.__name__)
#OR
print(type(hamza).__name__)


# if key not in dict, key = Person()
# all values of key are then key.value = "hamza.
# Dict within dict = {Hamza:{name,age}, Hamna:{name,age}}"

class SuperOne():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def printer(self):
        return f"{self.name}"
    def __str__(self):
        return f"The object has name {self.name} and age {self.age}"
    def __eq__(self, other):
        return self.age == other.age
class SubOne(SuperOne):
    def __init__(self, name, age, number, postcode):
        super().__init__(name, age)
        self.number=number
        self.postcode = postcode
    def __str__(self):
        return



# File renamer.
try:
    chdir(r"C:\Users\ABC\Desktop\BIRKBECK\PRINCIPLES OF PROGRAMMING\prodigies\\")
    dict = {}
    listt = []
    i = 1
    for f in listdir():
        a,b = path.splitext(f)
        x = str(i) + " " + a + b
        i = i+1
        os.rename(f, x) # This is how you rename files.
    logging.info("Files have been renamed, 810.")
except:
    print("This is to do with paths and all.")
    # then you can rename your files. by rename (f, x)
    logging.info("Files not renamed at 810.")


# When are you going to go through the rest and add all the checklist stuff onto your project.

# Iterators

iter1 = [a for a in range(10)]
iter1 = reversed(iter1)
print(next(iter1))
iterB = [x for x in range(10)]
iterB = b.__iter__()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# now 
print(iterB.__next__()) # this will go o till it's finished, completely. 
# Bring it back to normal by doing the following;
set_B = list(iterB)

# Another example

n_iter = 2
print(1 if n_iter == 2 else 0) # if and else used in one.   
def square(x):
  return x**2
print("True" if 9 in [square(x) for x in range(10)] else "False")
a = [square(x) for x in range(14)]
a = a.__iter__()

print (next(a))
print (next(a))
print (next(a)) # Once the iteration ends, it does not do anymore of these.

# Finally, using while loop:
nums_1 = [2,3,4,5,6]
it_nums_1 = iter(nums_1)

while True:
    try:
        print(next(it_nums_1))
    except StopIteration: # This means that when a StopIteration error is raised, you break.
        break
    except:
        print("If any error is raised, this is what happens.")

for_only = [x for x in range(5)]
for x in for_only:
    print(x)
else:
    print ('The else will still run in a for loop.')

# TALLY OF THE TIMES THIS PROGRAM HAS BEEN RUN.

import os
print(getcwd())
for x,y,z in walk(getcwd()):
    pass
chdir(r"C:\Users\ABC\Desktop\PROJECTS\MODULES\OS\madeup\\")

print(listdir())
i = ""
with open(r"made1.txt", "r") as f:
    xx = f.read()
    i = int(xx)

with open(r"made1.txt", "w") as f:
    i += 1
    f.write(str(i))
    
print("This file has been run",i, "times.")
logging.critical(f"HAS BEEN RUN {i} times now.")

logging.info("We are at the end of your program and now it's time to make more.")

# MORE ON READING FILES AND MANIPLULATING THE DATE.
with open("C:\\Users\ABC\Desktop\\BASIC COMPUTING AND CMD\\forus.txt", "r") as fff:
    # x = fff.read()
    y = fff.readline()
    z = fff.readlines(1)
    print(z)



# https://www.techbeamers.com/essential-python-tips-tricks-programmers/#tip2

# Bitwise operations
first_oper = 4
second_oper = 6
first_oper | second_oper # OR gate
first_oper ^ second_oper # XOR gate 1 if 10 01 else 0
~ first_oper # NOT
~ second_oper # NOT 
first_oper >> second_oper # 1<<2, moves 1 two places to the left. becomes 4
first_oper << second_oper # 1>>2, moves 1 two places to the right. becomes 0

print(True/2) # 0.5
print(False * 2) # 0
print(True + 2) # 3 

def truth(x):
    if x == 1:
        print(True)
    else:
        print(False)
if truth(1):
    print("This works.")
def t():
    return True
if t():
    print("Booleans help.")

# Very simple to understand.
def operator_acronyms(a9 = None, a10 = None):
    a9 = 12
    a10 = 15
    a9.__lt__(a10) # less than
    a9.__le__(a10) # lesser or equal
    a9.__eq__(a10) # equal
    a9.__ne__(a10) # not equal
    a9.__gt__(a10) # greater than
    a9.__ge__(a10) # greater or equal

# Binary, Hexa and Octal
number_bin = 19
print(bin(number_bin)) # 0b10011
print(hex(number_bin)) # 0o23
print(oct(number_bin)) # 0x13
# Use int() to conver the number back to integer value.

# Using string formatting for hexa, octa, binary, int and floats

print("This sentence has hex {0:x}, oct {0:o}, bin {0:b}, dec {0:d} and positive {0: f} an negative {0:f} space {0:+f} no space{0:-f} float.".format(43))
# This is really something you should memorize.

# Percentage
print("Percentage: {0:.2%}".format(43.3/100)) 

# Binary to decimal and hexa to decimal and octa to decimal
print(int("10111", 2))
print(int("0xcfff", 16))

# Unicode, encode and decode
unicode1 = u"Thisisastring".encode("utf-8")
unicode2 = unicode1.decode("utf-8") # but fir decode only 
unicodestring = u"Hello world"; utf8string = unicodestring.encode("utf-8"); plainstring1 = (utf8string, "utf-8")

print(list(map(ord, "Hamza"))) # [72, 97, 109, 122, 97]
aaaaaa = (list(map(chr, [72, 97, 109, 122, 97]))); print(aaaaaa) # Will bring the ascii character back to string.

# Testing
import pytest
# the following will only run when as a seperate test_file.py

def square(x):
    return x**2
def total(a,b):
    if type(a) == int and type(b) == int:
        return a+b
    else:
        raise TypeError ("Not possible, jerk.")
@pytest.mark.parametrize("test_input, expected_output", [(2,4),(3,9)])
def test_square(test_input, expected_output):
    a = square(test_input)
    assert a == expected_output
def test_total1():
    with pytest.raises(Exception): # this is a Exception test, only.
        assert total("r", 4)
@pytest.mark.windows
def test_windows1():
    assert True
@pytest.mark.windows
def test_windows2():
    assert True
@pytest.mark.mac
def test_mac1():
    assert True
@pytest.mark.mac
def test_mac2():
    assert True


# Inputting program that needs to be made better


def inputter(record_rl):
    try:
        dt = datetime.datetime.now()
        dt = "{:%d %B, %Y @ %H:%M:%S}".format(dt)
        name = input("What is your name, bitch??!")
        name = name.capitalize()
        hours = int(input("Hours?"))
        minutes = int(input("Minutes?"))
        minutes = round(minutes/60, 2)
        number_1 = hours + minutes
        print("The amount of hours you worked are " + str(number_1) + ".")
        print("You are about to enter, for your name:")
        print()
        print(f"{hours} hours and {minutes} minutes, and, in decimal points, you get {number_1} hours as of {dt}")
        print()
        hours_n_time = str(number_1), dt        
        if name not in record_rl.keys():
            record_rl[name] = [hours_n_time]
            print("A record of your name has been made with the hours entered; you may enter more but follow procedure, please.")
        elif name in record_rl.keys():
            record_rl[name].append(hours_n_time)
            print("Another entry has been added to your name.")
    except:
        print("You did not enter a number, dumbass.")
        #return inputter(lst)
    start_again = input("Start again? Enter for yes or N for no.")
    if start_again == "" or start_again == " ":
        return inputter(lst)
    elif start_again == "N" or start_again == "n" or start_again == "Nn" or "N" in start_again or "n" in start_again:
        pass
    else:
        print("You need to press Enter or N/n.")
    if len(record_rl) > 0:
        print(record_rl)
    else: 
        print("No values entered by the dumbass who became incharge for a few minutes.")
        
lst = {}
inputter(lst)

chdir("C:\\Users\\ABC\\Desktop\\PROJECTS\\")
# check if file exists.


appended = input("What changes have you made to the program?")
iii = ""
if path.isfile("C:\\Users\\ABC\\Desktop\\PROJECTS\\projectlog1.txt") == True:
    iii = "a"
else:
    iii = "w"

with open("C:\\Users\\ABC\\Desktop\\PROJECTS\\projectlog1.txt", iii) as focal:
        focal.write("Changes made: " + appended + " - " + datetime.datetime.now().strftime("%B%Y%m - %H%M%S") + "\n")



# TIPS and TRICKS

tricky_list = [1,2,3,None,(),[],]
print(len(tricky_list)) # 6, because they are all taking a place there.
tricky_list = {1,2,3,None,()} # 5, because sets do not take lists - they are not hashable as they can be changed.
# If list has same elements
def list_has_same_elements():
    xxxxx = [1,1,1,1,1,1]
    if xxxxx[1:] == xxxxx[:-1] and len(set(xxxxx)) == 1:
        print("Same.")
# Hashable means mutable.
# Hash able, *expand list, **expand dict
def expand_function():
    tuple_example1 = (1,2,3,4) 
    tuple_example2 = (5,6,7,8)
    list_example1 = [1,2,3,45,67]
    list_example2 = [55,66,77,88,99]
    dict_example1 = {1:"H", 2:"T"}
    dict_example2 = {2:"R", 3: "J"}
    a = {tuple_example2, tuple_example1} # this will work
    b = {*list_example1, *list_example2} # this will make a set of elements
    c = {**dict_example1, **dict_example2} # this will combine two dicts
    return a, b, c
# However, 

def double_tuple():
    tinytuple = (123, 'techbeamers')
    tinylist = ["Hacksaw", 1]
    tinystring = "Hamza"
    print(tinytuple * 2) # will give double the tuple
    print(tinylist * 3) # Same for list.
    print(tinystring * 4)


# MODULE SEARCHPATH

# Using two operators on the same line for something like 143 < x < 200

nnnn = 10
result12 = 1 < nnnn < 20
print(result12) 

if 1 < nnnn < 11:
  print("Wazzaa")
# And with that being said, we can make 

generate_for_me = (c for c in range(43) if c not in range(10,21))
# Variables in different ways.
lll,mmm,nnn,ooo,ppp,qqq = (1,4,3), "H", ["A","B","C"], {"name": "Hamza", "age": "24"}, {3,4,5,6}, 143

# default value of function
def greeting1(greeting, name = "You"):
    return f'{greeting}, {name}'
# args and kwargs
def argskwargs(*args, **kwargs):
    print(args)
    print(kwargs)
def normalargskwargs(a, *b, **c):
    print(a)
    print(b)
    print(c)
normalargskwargs("Hamza", 1,2,3,4,5, h = "Hamzas", m = "Mark")
def normal(a, b, c=None):
    if c!=None:
        return a+b+c
    else:
        return a+b
print(normal(2,3))

# FUNCTIONS THAT ARE WITHIN OTHER FUNCTIONS.

def double(x):
    return 2*x
def square(x):
    return x**2
def vectorize(f):
    def new(X):
        Y = []
        for x in X:
            Y.append(f(x))
        return Y
    return new
print(vectorize(double)([1,2,3,4,5])) # when there is a function within another, function()() runs the inner one too
xxxx = (vectorize(square))
print(xxxx([1,2,3,4,5]))

def vectorize():
    def new():
        a = 2
        return 2
    return new
print(vectorize()()) # Look at this one right here.

# TESTING UNITS VIA PARAMETRIZE

def square(x):
    return x ** 2
def sum(x,y):
    return x+y

import pytest

@pytest.mark.parametrize("INPUT, OUTPUT", [(4,16),(5,25)])
def test_square(INPUT, OUTPUT):
    a = para.square(INPUT)
    assert a == OUTPUT # You can put in as many tests as you want and it will do it for you.

@pytest.mark.parametrize("INPUT1, INPUT2, OUTPUT", [(4,4,8),(5,5, 10)]) 
def test_sum(INPUT1, INPUT2, OUTPUT):
    a = para.sum(INPUT1, INPUT2)
    assert a == OUTPUT # In this case we have 2 inputs and one output.

# More on OOP; assigning variables to class variables.

print(sys.modules.items())

# Remember, this is the core and it will be very helpful when learning the big boy modules;
# Django, Beautiful Soup, Re (Requests), Regex, Sellenium, HTML (basics), Datetime, TimeZone, Unittesting, Numpy, Pandas, Scipy
# .... SQL, MySQL, sci-kit, matplotlib.