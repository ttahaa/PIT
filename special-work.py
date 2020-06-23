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

result = explanation.center(100,"/")
# This method puts the symbol at the end and beginning of the string.

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

print(result)