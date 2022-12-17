
"""
+++++ if i = 1 or i = numm print +
+   + if j = 1 or j = numm print +
+   +
+   +
+++++

"""

numm = int(input("Enter your count : "))

for i in range(numm):

    for j  in range(numm):

        if(i == 0 or i == numm-1 ):
            print("+",end=" ")

        else:
            if(j == 0 or j == numm-1):
                print("+",end=" ")
            else:
                print(" ",end=" ")

    print(" ")

# for i in range(numm):
#     for j in range(numm):

#         if(i == 0 or i == numm-1 or j == 0 or j == numm-1):

#             print("+",end=" ") #ต่อกัน

#         else:

#             print(" ",end=" ")

#     print(" ")# ขึ้นบรรทัดใหม่


        