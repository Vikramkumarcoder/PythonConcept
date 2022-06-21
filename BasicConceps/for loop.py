#list1 = ['rohan', int, float, 'Vikram', 1, 5, 8, 2, 9, 4, 6, 67, 2004, 2737]
#for item in list1:
#	if str(item).isnumeric() and item>=6:
#		print(item)
list2 = [['Rohan', 12], ['Vikram', 13], ['Manish Bhaiya', 2], ['Vinit', 7]]

dict1 = dict(list2)
print (dict1)

for item in dict1:
	print(item)
	
for item,  age in dict1.items( ):
	if age>=7:
		print(item, age)

for item in list2:
	if str(item). isalpha():
		print(item)
	