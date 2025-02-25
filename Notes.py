# Lists
# A list is a group of items which are
# accessed through a single identifier



list = [0,0,0,0,0,0,0,0,0,0]

price = [32.23, 12.25, 56.38, 77.55, 39.0]

coworkers = ["Sarah", "Matt","Sophie"]
print(coworkers)
myList = []

coworkers[1]="Tim"
print(coworkers)
print(price)
print(price[0])
# append - add an item to the end of the list
nums = []
nums.append(34)
nums.append(99)
nums.append(21)
print(nums)
coworkers.append("Larry")
print(coworkers)

# insert - inserts an item at a given position
nums=[]
nums.append(34)
nums.insert(0,99)
print(nums)
nums = []
nums.append(34)
nums.insert(0,99)
nums.append(21)
nums.insert(0,7)
nums.append(3)
nums.append(11)
nums.insert(-2,15)
print(nums)

# remove - removes the first matching item in the list
coworkers.remove("Tim")
print(coworkers)
nums = []
nums.append(34)
nums.insert(0,99)
nums.remove(34)
nums.insert(1,7)
nums.append(3)
nums.remove(7)
print(nums)

# pop - removes the item at the given
# location and returns it
coworkers = ["Sarah","Matt","Sophie"]
former=coworkers.pop(1)
print(coworkers)
print(former)

nums = []
nums.append(34)
nums.insert(0,5)
nums.remove(34)
nums.insert(1,7)
nums.append(3)
nums.pop( 2 )
print(nums)

print(coworkers.pop())

queue = []
queue.append( 33 )
queue.append( 22 )
queue.append( 12 )
queue.append( 993 )

print( queue.pop(0) )
print( queue.pop(0) )

stack = []
stack.append( 33 )
stack.append( 22 )
stack.append( 12 )
stack.append( 993 )

print( stack.pop() )
print( stack.pop() )
#nums = []
#print(nums.pop())
# cannot remove from something that is empty

# list processing with loops

bob = [56,65,98,2,25]
for num in bob:
    print(num)

myList = []
for num in range(5):
    myList.append(num)
print(myList)

list = [56, 65, 98, 2, 25]
total = 0
for x in range( len( list) ) :
    total += list[ x ]
print(total)

list = [56, 65, 98, 2, 25]
total = 0
for num in list:
    total += num
print(total)
