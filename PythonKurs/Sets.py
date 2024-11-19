
fruits = {"orange", "apple", "banana"}
#print(fruits[0])   indekslenemez

for x in fruits :
    print(x)

fruits.add("cherry")
print(fruits)

fruits.update(["grapes", "mango"])
print(fruits)

#sette tekrarlı elemanlar bir kere gösterilir
myList=[1,2,3,4,5,1,3,5]
print(set(myList))

#öge silmek için
fruits.remove("mango")
fruits.discard("grapes")
print(fruits)

#herhangi bir eleman silinir
fruits.pop()
#tamamen silmek
fruits.clear()