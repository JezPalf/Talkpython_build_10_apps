import os
import shutil
import requests



def getCats(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = getDataFromURL(url)
    saveImage(folder, name, data)



def getDataFromURL(url):
    response = requests.get(url,stream = True)
    return response.raw



def saveImage(folder, name, data):
    fileName = os.path.join(folder, name + '.jpg')
    with open(fileName, 'wb') as fout:
        shutil.copyfileobj(data, fout)