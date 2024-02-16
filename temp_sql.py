import time
import requests
import selectorlib
from datetime import datetime
import sqlite3

#Esatblish a conneciton and a server
connection = sqlite3.connect("data.db")

#scrap temp from
URL = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temp"]
    return value

def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temp VALUES(?,?)",(now, extracted))
    connection.commit()

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
        time.sleep(20)


#store in a txt file, text file should alwso contain the date
#tempdata.txt: date,temperature
#create stremlit app with temperature values in the tempdata.txt

