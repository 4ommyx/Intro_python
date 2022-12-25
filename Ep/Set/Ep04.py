# set operator

# Union()
num1 = {1,2,3,4,57,6,4,64,8,9,86,5}
num2 = {1,2,4,56,3,4,5,6,64,4}
num3 = {1,2,3}
numu = num1.union(num2)
# num1.update(num2) # นำข้อมูลมาต่อกัน

print(numu)

# Copy()
# num3 = num2.copy()
# print(num3)

# Diff()
numd = num1.difference(num2)
print(numd)

# Intersec ()
numi = num1.intersection(num2)
print(numi)

# Supset
sub = num1.issubset(num2)
print(sub)
sub1 = num3.issubset(num1)
print(sub1)

# min , max(set name)
print(min(num1))
print(max(num1))
