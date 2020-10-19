d={1:[1,2,3]}
d[1].extend([1,2,3])
print (d)
# set([{1:2},{4:5},{6:7}])
import os
t=os.stat("Rent_C503支出.txt")
print(t)
print (dir(t))
print (t.st_size)