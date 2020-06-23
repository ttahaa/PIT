"""
# \n : Önüne gelen ifadeyi bir alt satıra taşır.
print("Bili \nşim")
"""
"""
# print(balbla[5]) [?] içine yazılan sayıya denk gelen karakteri yazdırır.
name = "Taha"
print(name[2])
"""
"""
# print(len(balbla)) len metodu blabla değişkeninin içindeki ifadenin kaç karakterli olduğunu yazdırır.
variables = "Taha Ozdere writing codes."
print(len(variables))
"""
"""
# Yazdırılacak değişkenin içindeki karakter aralığını yazdırmak için [3:5] , [8:21] ; veya [2:40:2] dersek her iki karakterde bir yazdırır.
long = "Hi everybody welcome my work.It really god."
print(long[2:])
print(long[2:15])
print(long[5:30:3])
"""
"""
# Eğer süslü parantez içerisinde : var yanında da örneğin 5:3 varsa sağ taraf virgülden sonraki satır sayısını, sol taraf ise toplam karakter sayısını yazdırır.
islem = 200/700
print('the islem is {i:10.5}'.format(i=islem))
"""
"""
# String bir ifadenin başına f getirilirse değişkenleri yerine koydurarak yazabiliriz.
name = "Kamilcan"
surname = "Sercan"
examNotes = 80
print(f"The student name is {name} {surname} and his exam note is {examNotes}")
"""
"""
# Bir ifade içerisindeki bir harfi değiştirmek için o harften önceki ver sonraki değerleri yazdırır o harfi ise tırnak içerisinde yazarız.
# Hello world kelmesindeki "w" yi "W" ile değiştirin.
w = "Hello world"
print = w[0:6] + "W" + w[-4:]
"""