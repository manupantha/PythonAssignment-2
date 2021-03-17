tuple1 = ('Solam', 'Rana', 22)
tuple2 = ('Manu', 'Pantha', 21)
tuple3 = ('Amrita', 'Pandey', 28)
list1 = [tuple1, tuple2, tuple3]
list1.sort(key=lambda x: x[1])
print(list1)
