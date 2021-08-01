#how to extract extension from filename in python
fileName = input()
file_extens = fileName.split('.')
print("the extension is " + repr(file_extens[-1]))