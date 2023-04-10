rows = int(input("Write rows\n"))
columns = int(input("Write columns\n"))
pieces = int(input("Write how many pieces do you want\n"))

if pieces < rows*columns and (pieces % rows == 0 or pieces % columns == 0):
    print('Enjoy your chocolate!')
else:
    print('No, you can\'t do that!')
