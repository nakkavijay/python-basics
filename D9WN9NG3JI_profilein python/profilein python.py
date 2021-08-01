#HOW TO DO A profile a python script
import cProfile
def sum ():
    print(5,10)
cProfile.run('sum()')