tuple1 = (20, 10, 60, 70, 50, 20, 80, 20, 10, 20, 60, 60, 50)
set1=set(tuple1) #bir kümeye cevirdim.
dict={}
for i in set1:
    dict[i]=tuple1.count(i)
print (dict)