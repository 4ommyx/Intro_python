# List Parameter เป็นการใช้ 
# list tuple ร่วมกับ function

def fruit(item):
    print(item)
    for i in range(len(item)):
        print(i+1,item[i])

fruitt=["มะม่วง","มะละกอ"]
fruit(fruitt)

fruittt=("มะม่วง","มะละกอ")
fruit(fruittt)


