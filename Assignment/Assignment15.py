
numm = int(input("Enter your count : "))

"""
+ o + o +  if i odd  (j odd print + / j even print o)
o + o + o  if i even (j odd print o / j even print +)        
+ o + o +
o + o + o

"""
for i in range(numm):

    for j  in range(numm):

        if i % 2 != 0:

            if j % 2 !=0:
                print("+",end=" ")
            else:
                print("o",end=" ")

        else:

            if j % 2 !=0:
                print("o",end=" ")
            else:
                print("+",end=" ")

    print(" ")
