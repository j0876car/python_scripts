
def MakeaBed():
    print('must make your bed true')
    return

def TakeShower():
    print('must take shower false')
    return

def GoToMovie():
    print('now go to movie')

n= int(input('Enter number:'))
r=n>=100
#print(r)
if r == True:
    MakeaBed()
else:
    TakeShower()
    GoToMovie()
    #print('This works too')


