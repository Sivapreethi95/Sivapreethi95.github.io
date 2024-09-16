#reading all the contents of a file.
#open the file for reading data.

#read strings from the file.


#closing the file.

def readContents(fileName):
    f = open(fileName, 'r')
    print('The file contents of', fileName, 'are:')
    str = f.read()
    print(str)

readContents('contents.txt')
readContents('kavithai.txt')
readContents('preethi.txt')