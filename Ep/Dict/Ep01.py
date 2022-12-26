
# dict สามารถ disign index ได้ ว่าindexจะเป็น int float str boolen etc.
# dict --> key(การเข้าถึงข้อมูล),value(ค่าของข้อมูล)
# list / tuple --> index,value

# การสร้าง dict (key เปรียบเสมือน index ที่เราสามารถเข้าถึงด้วยชื่อตัวแปรอะไรก็ได้)
# ชื่อตัวแปร = {key:value,key1:value1,...,keyn,valuen}
colors = {"red":"แดง","blue":"น้ำเงิน",157:"บ้านออม"}
score = {"aom":200,"mu":2}
print(colors["red"])
print(colors[157])
print(score["aom"])

animals = dict(cat="แมว",dog="สุนัข")
print(animals["cat"])