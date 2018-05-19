import datetime

def printHeader():
    print('--------------------')
    print(' Birthday countdown ')
    print('--------------------')
    print()

def getUserBirthday():
    print('When were you born')
    year = int(input('"Year [YYYY]: '))
    month = int(input('"Month [MM]: '))
    day = int(input('"Day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday

def calculateDaysBetween(originalDate, targetDate):
    thisYear = datetime.date(targetDate.year, originalDate.month,originalDate.day)
    dt = thisYear - targetDate
    return dt.days


def printBirthdayInformation(days):
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday will be in {} days'.format(days))
    else:
        print('Happy Birthday!!!')

def main():
    printHeader()
    bDay = getUserBirthday()
    today = datetime.date.today()
    numberOfDays = calculateDaysBetween(bDay, today)
    printBirthdayInformation(numberOfDays)


main()