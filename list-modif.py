srclist = [1,3,5,7,11]

newlist = [(x-1)*2 for x in srclist]
tflist = [True if x == 1 else False for x in srclist]
onelist = [x if x == 1 else 0 for x in srclist]
sqlist = [x**2 for x in srclist]

print newlist
print tflist
print onelist
print sqlist