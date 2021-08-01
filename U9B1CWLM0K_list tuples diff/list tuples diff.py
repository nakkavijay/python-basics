#how to create a list and tuple with comma seperated numbers in python
values = input()
list = values.split(",")
tuple = tuple(list)

print('List :' , list)
print('Tuple :', tuple)