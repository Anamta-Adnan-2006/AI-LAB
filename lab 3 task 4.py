def match_strings(str1, str2):
    if str1 == str2:
        return True
    else:
        return False
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if match_strings(string1, string2):
    print(" The strings match")
else:
    print("The strings do not match.")
