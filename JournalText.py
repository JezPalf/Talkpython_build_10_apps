import os

"""
This is the journal module.
"""


def load(name):
    """
    This mephod creates and loads a new method.

    :param name: The name of the journal to load.
    :return: A new journal data structure
    """
    
    data = []
    filename = getFullPath(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
               data.append(entry.rstrip())

    return data


def save(name, journalData):
    filename = getFullPath(name)
    print('....saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journalData:
            fout.write(entry +'\n')


def getFullPath(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def addEntry(text, journalData):
    journalData.append(text)
