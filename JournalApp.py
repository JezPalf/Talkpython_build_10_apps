import JournalText


def main():
    printHeader()
    runEventLoop()

def printHeader():
    print('--------------------')
    print('    Journal App')
    print('--------------------')
    print()


def runEventLoop():
    print('What would you like to do?')
    journalName = 'default'
    journalData = JournalText.load(journalName)


    cmd = 'EMPTY'
    while cmd != 'x' and cmd:
        cmd = input('[L]ist your current entires, [A]dd to the journal or E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            listEntry(journalData)
        elif cmd == 'a':
            addEntry(journalData)
        elif cmd != 'x' and cmd:
            print('"{}" is invaild input, please try again.'.format(cmd))
    print('Finished')
    JournalText.save(journalName, journalData)

def listEntry(data):
    print('Your journal entries: ')
    entires = reversed(data)
    for (idx, entry) in enumerate(entires):
        print('- [{}] {}'.format(idx+1, entry))


def addEntry(data):
    text = input('Type your entry, <enter> to exit: ')
    JournalText.addEntry(text, data)



if __name__ == '__main__':
    main()