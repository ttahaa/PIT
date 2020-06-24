
"""
# print("Merhaba Taha Bey.Bugün nasıl hissediyorsunuz ?")
# print("Merhaba wrXA.Çok iyi hissediyorum.")
# print("Günlük sistem güncelleştirmesi ve veri analizi tamamlandı.")
"""
"""
x = input("1.Sayı: ")
y = input("2.Sayı: ")

# print(type(x))
# print(type(y))

toplam = (int(x) + int(y))

# print(toplam)
"""
"""
z = 5             #int
y = 2.5           #float
name = "Taha"     #str
isOnline = True   #bool


# print(type(z))            
# print(type(y))         
# print(type(name))      
# print(type(isOnline))  


# TypeConversion

# int to float

x = float(x)
# print(x)
# print(type(x))

# float to int 

y = int(y)
# print(y)
# print(type(y))

result = str(x) + str(y)
# print(result)
# print(type(result))

isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

# bool to int

isOnline = int(isOnline)
# print(isOnline)
# print(type(isOnline))
"""
"""
name = "Taha"
surname = "Ozdere"
age = 15

greeting = "My name is " + name + " " + surname + " and \nI am " + str(age) + " years old"
length = len(greeting)

# print(greeting)
# print(greeting[0])
# print(greeting[3])
# print(greeting[length-1])
# print(greeting[-1])
# print(greeting[3:7])
# print(greeting[3:])
# print(greeting[:15])
# print(greeting[2:40:3])
"""
"""
name = "Taha"
surname = "Özdere"
age = 15

# print("My name is {} {}".format(name, surname))
# print("My name is {1} {0}".format(name, surname))
# print("My name is {s} {n}".format(n=name, s=surname))
# print("My name is {} {} and I'm {} years old.".format(name, surname, age))
# print("My name is {} {} and I'm {} years old.".format(name, name, name))

# result = 200/700
# print('the result is {r:1.4}'.format(r=result))

# print(f"My name is {name} {surname} and I'm {age} years old.")
"""
"""
message = "Hello There. My name is Taha Özdere"

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()
# message = message.strip()
# message = message.split()
# message = message.split(".")
# message = "---".join(message)

# index = message.find("Taha")
# isFound = message.startswith("H")
# isFound = message.endswith("e")

# message = message.replace("Taha","Ahmet")
# message = message.replace("ç","c")
# message = message.replace("ö","o")
# message = message.replace(" ","-")

message = message.center(50, "*")

print(message)
"""

# message = "Hello There.My name is Hayley Crockery"
# print(message[0])

my_list = [1,2,3]
my_list = ["iki", 8, False, 3.5]
print(my_list)








