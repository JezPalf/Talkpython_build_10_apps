import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    printHeader()
    folder = getFolderFromUser()
    if not folder:
        print('Sorry, that location cannot be searched.')
        return

    text = getSearchTextFromUser()
    if not text:
        print('Sorry, cannot search for nothing')
        return

    matches = searchFolders(folder, text)
    matchCount = 0
    for m in matches:
        matchCount += 1
        print('------Match------')
        print('file: ' + m.file)
        print('line: {}'.format(m.line))
        print('match: ' + m.text.strip())
        print()
    print('Found {:,} matches'.format(matchCount))


def printHeader():
    print('--------------------')
    print(' File Searcher App')
    print('--------------------')
    print()


def getFolderFromUser():
    folder = input('What folder would you like to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return  None

    return os.path.abspath(folder)


def getSearchTextFromUser():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()


def searchFolders(folder, text):
    items = os.listdir(folder)
    for item in items:
        fullItem = os.path.join(folder, item)
        if os.path.isdir(fullItem):
            yield from searchFolders(fullItem, text)

        else:
            yield from searchFile(fullItem, text)


def searchFile(fileName, searchText):
    with open(fileName, 'r', encoding='utf-8') as fin:
        lineNumber = 0
        for line in fin:
            lineNumber +=1
            if line.lower().find(searchText) >= 0:
                m = SearchResult(line = lineNumber, file = fileName, text=line)
                yield m


if __name__ == '__main__':
    main()


