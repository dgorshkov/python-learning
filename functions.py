# Run in terminal!

import random

width = input('Enter width: ')
height = input('Enter height: ')

# Checks is rectangle is tall, returns bool
def istall (w,h):
    return h>w

print 'Width is ' + str(width) + ', height is ' +str(height)
print 'Is it tall? -> ' + str(istall(width,height))
