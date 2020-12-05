
message = "Te£st123"
# message = 'n'
new_message = ""
for letter in message.lower():
    if letter.isalpha():
        if ord(letter) > ord('m'):
            
            difference = 13 - (ord('z') - ord(letter))
            new_letter = chr(ord('a') - 1 + difference)
            print(chr(ord('a') + difference))

        else:

            new_letter = chr(ord(letter) + 13)

        new_message += new_letter
    else:

        new_message += letter

final = ""
isUpperOrLower = [True if letter.isupper() and letter.isalpha() else False for letter in message]
for boolean, letter in zip(isUpperOrLower, [x for x in new_message]):
    if boolean == True:
        final += letter.upper()
    else:
        final += letter

print(message)
print(isUpperOrLower)
print(new_message)
print(final)


jake = "TestmeX"

new_Jake = [x if ord(x.lower()) > ord('m') else "empty" for x in jake if len(jake) > 4]
print(new_Jake)


import string

# isalpha and isupper()

def rot13(message):
    
    return "".join(
            [letter.upper()
                if boolean == True else letter 
                for boolean, letter in zip(
                    [True if letter.isupper() and letter.isalpha() else False for letter in message], 
                    [chr(ord(letter)-13) 
                            if ord(letter) > ord('m') else chr(ord(letter) + 13) 
                            if letter.isalpha() else letter 
                                for letter in message.lower()]) 
            ])


print(rot13("Test123$"))
