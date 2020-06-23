
"""
name = "'Sandrine'"
surName = "'Wilderman'"
city = "'Mantemouth'"
phoneNumber = "'851.494.1217'"
companyName = "'Inc,and Sons,LLC,Group'"
finansNumber = "'85196534'"

result = "My name is {} and my surname is {}. I live in {}. My company name is {}.Finally my finans number is {}. ".format(name,surName,city,companyName,finansNumber)

print(result)
"""
explanation = "Hello world.We are alive.Come in there is no thunder here."

result = explanation.capitalize()
# This method just makes capitalizes the first letter.

result = explanation.casefold()
# This method makes all letters lowercase.

result = explanation.center(100, "/")
# This method puts the symbol at the end and beginning of the string.(.rjust,.ljust)

result = explanation.count(" ")
# This method indicates the number of times the symbol is written.

result = explanation.encode("utf-8")
# This method specifies an encoding style.

result = explanation.endswith("e")
# This method checks which character it ends with.

result = explanation.expandtabs(50)
# Put \ t wherever you want.Then write the number you want.Finally there will be as many spaces as you write.

result = explanation.find("w")
# This method checks the presence of the typed symbol.And prints what order it are in.

result = "My name is {}".format("Coy")
# This method specifies the expression or expressions written in parentheses.

result = explanation.split()
# Separates spaces and prints them in list format.

result = explanation.upper()
# Prints the sentence with a capital letter.

result = explanation.lower()
# Prints sentence in lowercase.

result = explanation.title()
# Capitalizes the first letter of each word.

result = explanation.strip()
# Deletes the first and last spaces.Or deletes characters in parentheses.(.lstrip, .rstrip)

result = explanation.replace("Hello","Hi")
# This method is used for character updating.

result = explanation.index("w",0,25)
# Prints the order in which the symbol in parentheses is.Prints error if no symbol.But "".find" prints -1 if no symbol.We  can specify gap(not required).

result = explanation.isalpha()
# Checks if characters are alphabetical.

result = explanation.isdigit()
# checks if characters are numbers.

print(result)