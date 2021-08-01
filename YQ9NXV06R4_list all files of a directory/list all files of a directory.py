#how to list all files of a Directory in python
from os import listdir
from os.path import isfile , join
file_list= [f for f in listdir('/Users') if isfile (join('/Users',f))]