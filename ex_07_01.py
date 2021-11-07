
fh = open('mbox-short.txt')

for lz in fh:
    ly = lz.rstrip()
    print(ly.upper())
