fruits = ["apple", "banana", "cherry"]
print(fruits[1])   #return second(banana)

fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"   #change apple to kiwi
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  #add orange to the end of list
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon") #insert lemon as the second element of list
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") #remove banana from the list
print(fruits)

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  #gets the last item

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  #return third, fourth, and fifth element

fruits = ["apple", "banana", "cherry"]
print(len(fruits))