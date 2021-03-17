list1 = ['Manu', 'Solam', 'Amrita', 'Pooja']
a = input("enter the name:")
found = False
for i in list1:
    if i.casefold() == a.casefold():  # case less matching
        print("found")
        found = True
        break

if not found:
    print("not found")
