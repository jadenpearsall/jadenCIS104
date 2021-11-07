filename = input('Enter the file name: ')
try:
    if filename == 'na na boo boo'
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()
file1 = open(filename)
except FileNotFoundError:
    print('File cannot be opened:', filename)
    exit()
