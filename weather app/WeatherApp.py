
def main():
    printHeader()
    # get location from user
    postCode = input('What is the post code you would like the weather for?')
    # get html from web
    getHtml(postCode)
    # parse html
    # display the forecast

def printHeader():
    print('--------------------')
    print('     Weather App')
    print('--------------------')
    print()

def getHtml(postCode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(postCode)
    #print (url)
    requests

if __name__ == '__main__':
    main()
