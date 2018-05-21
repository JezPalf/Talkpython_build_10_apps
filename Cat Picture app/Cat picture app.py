import os
import platform
import subprocess

import catdownload

def main():
    printHeader()

    folder = createOutputFolder()
    print('Created or found folder: ' + folder)
    downloadCats(folder)
    showCats(folder)


def printHeader():
    print('--------------------')
    print('      Cat App')
    print('--------------------')
    print()


def createOutputFolder():
    baseFolder = os.path.dirname(__file__)
    folder = 'catPictures'
    fullPath = os.path.join(baseFolder, folder)

    if not os.path.exists(fullPath) or not os.path.isdir(fullPath):
        print('Creating new folder at {}'.format(fullPath))
        os.mkdir(fullPath)
    return fullPath


def downloadCats(folder):
    print('Checking server....')
    catCount = 8
    for i in range(1,catCount+1):
        name = 'cat_{}'.format(i)
        print('Downloading ' + name)
        catdownload.getCats(folder, name)
    print('Done')


def showCats(folder):
    print('Showing cats....')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('Sorry, unsupported os: ' + platform.system())



if __name__ == '__main__':
    main()