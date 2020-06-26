'''
Convert string to camel-case.
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
'''

def to_camel_case(string):
    upper = string[0].isupper()
    out = ""
    for letter in string:
        if letter.isalpha() and upper:
            out += letter.upper()
            upper = False
        elif letter.isalpha():
            out += letter.lower()
        else:
            upper = True
    return out

print(to_camel_case("the-stealth-warrior"))
