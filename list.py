thislist = ["apple", "banana", "cherry"]
print(thislist)
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
  # This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("This example returns the items from the beginning to, but NOT including kiwi thislist 4 :", thislist[:4])
#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("This example returns the items from cherry to the end:", thislist[2:])
#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print("Change the second item:", thislist)
#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print("Insert Items :", thislist)
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print("Insert an item as the second position:", thislist)
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print("Remove the second item:", thislist)
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#Sort the list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#Join Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
