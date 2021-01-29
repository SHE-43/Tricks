# Beautiful code.
# Generate random values via comprehension and generators.

import random as rd

names = ['Avery ', 'Ayla', 'Bailey', 'Bella ', 'Blake ', 'Blakely', 'Bonnie ', 'Brianna ', 'Briella', 'Brielle ', 'Brooke ', 'Brooklyn ', 'Callie', 'Camila', 'Camille ', 'Caroline ', 'Catalina', 'Charlie ', 'Charlotte ', 'Chloe', 'Claire ', 'Clara ', 'Cora', 'Daisy', 'Dakota ', 'Daniela ', 'Darcie ', 'Delaney ', 'Delilah', 'Destiny ', 'Diana ', 'Eden ', 'Elaina ', 'Eleanor ', 'Elena ', 'Eliana ', 'Elise', 'Eliza ', 'Elizabeth', 'Ella ', 'Ellie ', 'Eloise ', 'Elsie', 'Elspeth', 'Ember ', 'Emery', 'Emilia', 'Emily', 'Emma ', 'Erin ']
IDs = [x for x in range(10000, 10000 + len(names))]
emails = [f"{x.lower().strip()}@mail.com" for x in names]
contact_numbers = ["0" + "".join([rd.choice(list("01234566789")) for x in range(9)]) for y in range(len(names))]
print(len(names))
print(len(IDs))


print(contact_numbers)
