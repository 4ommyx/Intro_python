
#การคัดลอก dict copy()
room = {100:"aom",101:"ohm",102:"pee",103:"aus"}
x = room.copy()
print(room)
print(x)

#dictซ้อนdict
name = {
        "aom":{"weigh":60,"hight":120,"fav":["แกงกะหรี่","โกโก้","เย็นตาโฟ"]}
        ,"mu":{"weigh":40,"hight":190,"fav":["ส้มตำ","โกโก้","เฉาก๊วย"]}
        ,"ohm":{"weigh":60,"hight":120,"fav":["ค","ว","ย"]}

}
print(name["aom"])
print(name["mu"])
print(name["ohm"]["fav"]) # เจาะจงเข้าไปใน dict ที่ลึกลงไป
 
if ("โกโก้" in name["aom"]["fav"]) and ("โกโก้" in name["mu"]["fav"]):
    print("True")
else:
    print("False")