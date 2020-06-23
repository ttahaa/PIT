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
explanation = "Hello world.We are alive.Come in there is no thunder here"

result = explanation.capitalize()
# Hello world.we are alive.come in there is no thunder here

result = explanation.casefold()
# hello world.we are alive.come in there is no thunder here

result = explanation.center(100,"*")
#*********************Hello world.We are alive.Come in there is no thunder here**********************

result = explanation.count("e")
#10 Ama  ("e",15) deseydik 15. karakterden sonraki "e" leri sayardı.

print(result)