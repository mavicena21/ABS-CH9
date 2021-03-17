import os

for foldername, subfolders, filenames in os.walk('C:\\latihan'):
    print('Folder saat ini adalah ' + foldername)

    for subfolder in subfolders:
        print('SUBFOLDER dari ' + foldername + ' adalah ' + subfolder)

    for filename in filenames:
        print('FILE didalam ' + foldername + ' adalah ' + filename)

    print('')

print(os.walk('C:\\latihan'))