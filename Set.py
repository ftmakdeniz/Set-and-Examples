###  Set : Küme ###

"""
kume = set()   ## 1) Küme tanımlama yöntemi
kume2 = {}     ## 2) Küme tanımlama yöntemi

# ÖNEMLİ NOT :  Set ile dolu küme olusturalamaz.
# Nedeni performans kaybı. Önce bos oluşturulur sonra içeri veri atılır.

kume_3 = {1,2,3}
print(kume_3)

kume.add("A")       #Kümeye eleman ekleme
kume.add("C")       #Kümeye eleman ekleme
kume.add("D")       #Kümeye eleman ekleme
kume.add("F")       #Kümeye eleman ekleme
print(kume)

kume.remove("A")    #İçerde değer varsa siler yoksa hata verir
print(kume)

kume.discard("C")    #Remove dan farkı hata patlatmaz
print(kume)

print(len(kume))      #Eleman sayısı
"""

"""
kume = {11,22,33,44,55}
kume2 = {33,44,55,66,77,88,99}


# Küme farkı bulma
kume_farkı =kume - kume2   #1. Yöntem tavsiye edilmeyen
kume_farkı2 = kume2 - kume
print(kume_farkı)
print(kume_farkı2)
"""


"""
### Küme Birleşimi
kume_farkı = kume.difference(kume2)    #Tavsiye edilen yöntem
kume_farkı2 = kume.difference(kume)
print(kume_farkı)
print(kume_farkı2)
"""
"""
# Eleman silme
kume_birlesim = kume.union(kume2)
print(kume_birlesim)
for eleman in kume_birlesim:
    print(eleman)

print(12 in kume_birlesim)   # Kümede elemanın  olup olmadıgını kontrol etmek için
"""
"""
#Var olan kümeye başka bir kümenin elemanlarını ekleyip güncellemek
turkiye = {"apple", "banana", "cherry"}
afrika = {"pineapple", "mango", "papaya"}
turkiye.update(afrika)
print(turkiye)

#Eleman silme
turkiye.remove("papaya")
print(turkiye)

turkiye.discard("apple")
print(turkiye)

#İlk elemanı siler
turkiye.pop()
print(turkiye)

# Kümeyi temizleme
turkiye.clear()
print(turkiye)

del turkiye   ## Ramden siler
# print(turkiye) yazarsak hata verir. del tek basına calısır.

"""
kume = {11,22,33,44,55}
kume2 = {33,44,55,66,77,88,99}
kume3 = {1,2,3,}
#Alt küme
print(f"küme kümesi küme2 kümesinin alt kümesi midir?.{kume.issubset(kume2)}")

#Üst küme
print(f"küme kümesinin küme2 kümesinin üst kümesi midir:{kume.issuperset(kume2)}")

#Ayrık küme
print(f"Küme kümesi  Küme3 kümesinin ayrık kümesi midir?:{kume.isdisjoint(kume3)}")