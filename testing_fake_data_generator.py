# Beautiful code.
# Generate random values via comprehension and generators.

import random as rd
import pandas as pd

names = ['Avery ', 'Ayla', 'Bailey', 'Bella ', 'Blake ', 'Blakely', 'Bonnie ', 'Brianna ', 'Briella', 'Brielle ', 'Brooke ', 'Brooklyn ', 'Callie', 'Camila', 'Camille ', 'Caroline ', 'Catalina', 'Charlie ', 'Charlotte ', 'Chloe', 'Claire ', 'Clara ', 'Cora', 'Daisy', 'Dakota ', 'Daniela ', 'Darcie ', 'Delaney ', 'Delilah', 'Destiny ', 'Diana ', 'Eden ', 'Elaina ', 'Eleanor ', 'Elena ', 'Eliana ', 'Elise', 'Eliza ', 'Elizabeth', 'Ella ', 'Ellie ', 'Eloise ', 'Elsie', 'Elspeth', 'Ember ', 'Emery', 'Emilia', 'Emily', 'Emma ', 'Erin ']
IDs = [x for x in range(10000, 10000 + len(names))]
emails = [f"{x.lower().strip()}@mail.com" for x in names]
contact_numbers = ["0" + "".join([rd.choice(list("01234566789")) for x in range(9)]) for y in range(len(names))]
addresses = ["".join([rd.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) for x in range(14)]) for y in range(len(names)) ]
dobs = ["".join([rd.choice(list("01234566789")) for x in range(6)]) for y in range(len(names))]
genders = [rd.choice(["Male", "Female", "Transgender" ,"No Comment"]) for x in range(len(names))]

path = r"C:\Users\ABC\Desktop\Source-Management-System-Trial--main\Source-Management-System-Trial--main\files_excel\SMS.xlsx"

df = pd.read_excel(path, engine='openpyxl', dtype = "object")
# Customer ID Full Name Email Gender Contact  DOB Address
df["Customer ID"] = IDs
df["Full Name"] = names
df["Email"] = emails
df["Gender"] = genders
df["Contact"] = contact_numbers
df["DOB"] = dobs
df["Address"] = addresses



writer = pd.ExcelWriter(path)
df.to_excel(writer, index = False)
writer.save()



