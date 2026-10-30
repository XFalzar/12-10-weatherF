import pandas as pd
import os
from common.config import AppConfig

# import openpyxl - import tylko po to żeby wykonać instalacje

def append(data, index):
    FILE_PATH = AppConfig.WEATHER_FILE[index]
    try:
        new_df = pd.DataFrame(data)  # nowy df z obiektem weather

        if os.path.exists(FILE_PATH):
            old_df = pd.read_excel(FILE_PATH)  # odczytuje stare
            df = pd.concat([old_df, new_df])  # łączę stare z nowym
            df.to_excel(FILE_PATH, index=False)  # zapisuje w jednym pliku - nadpisuje istniejący
        else:
            new_df.to_excel(FILE_PATH, index=False)  # tworze plik z nowym df który wcześniej utworzyłem
    except Exception as e:
        print(e)


