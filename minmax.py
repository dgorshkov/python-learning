
l = [2,3,5,70,11,13]

maximum = -100
minimum = 100


for foo in l:
    if foo > maximum:
        maximum = foo

for foo in l:
    if foo < minimum:
        minimum = foo

print 'maximum is ' + str(maximum)
print 'minimum is ' + str(minimum)
print 'yay'


