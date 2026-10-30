from datetime import datetime
import pandas as pd
temp_c = lambda temp: round(temp - 273.15, 2)

km_h = lambda wind: round(wind * 3.6, 2)

timestamp = lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")

time_dt = lambda time: datetime.fromtimestamp(time).strftime("%H:%M:%S")

def readexcel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        return e