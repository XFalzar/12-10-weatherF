import time
import pandas as pd
from services.openweather_api import get_weather
from services.datafiles import append
from services.dashboard import create_app
from services.mysql_db import initialize_db, insert_record, read_record

initialize_db()
#create_app()


while True:
    # pobieranie danych
    weather = get_weather()

    # zapisywanie do excel
    append([weather],0)

    # zapisywanie do mysql
    insert_record(weather)
    print("Pobrałem dane pogodowe")
    time.sleep(10)