import requests
import bs4
import collections

weatherReport = collections.namedtuple('weatherReport',
                                       'cond, temp, scale, loc')

def main():
    printHeader()
    # get location from user
    Code = input('What is the post code you would like the weather for? [xxxx xxx]')
    # get html from web
    html = getHtml(Code)
    # parse html
    report = getWeather(html)
    # display the forecast
    print('The temperature in {} is {}{} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

def printHeader():
    print('--------------------')
    print('     Weather App')
    print('--------------------')
    print()

def getHtml(postCode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(postCode)
    response = requests.get(url)

    return response.text

def getWeather(html):

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanUp(loc)
    loc = findLoc(loc)
    condition = cleanUp(condition)
    temp = cleanUp(temp)
    scale = cleanUp(scale)

    #names tuple
    report = weatherReport (cond = condition, temp = temp, scale = scale , loc = loc)
    return report

def cleanUp(text : str):
    if not text:
        return text

    text = text.strip()
    return text

def findLoc(loc : str):
    parts = loc.split('\n')
    return parts[0].strip()




if __name__ == '__main__':
    main()