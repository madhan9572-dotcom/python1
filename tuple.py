#tuples in python
# Tuple is a collection of multiple values that is ordered and cannot be changed after creation
student= ("Madhan",90,"python")
print(student[0])

#access values in a tuple
student = ("Madhan",21,85.5)

print(student[0])
print(student[1])
print(student[2])

#immutable nature of tuples
studen=("Madhan",21,85.5)

student[1]=22
#This gives an error because we cannot modify a tuple


#tuples are immutable,meaning they cannot be changed after they created.they are defined 
numbers=(10,20,20,30,20)

print(numbers.count(20))

#tuple in index method
numbers = (10,20,30,40)

print(numbers.index(30))


#various methods
numbers = (10,20,30,40,50,60)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

