import sys, time

indent = 0
indentIncrease = True 

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(.1)     #slow down the execution
        if indentIncrease:
            indent = indent + 1
            if(indent==10):
                indentIncrease = False
        else:
            indent = indent - 1
            if(indent==0):
                indentIncrease = True

except KeyboardInterrupt:
    sys.exit()
