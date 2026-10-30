import mysql.connector as sql
from common.config import AppConfig
import pandas as pd
def create_connection():
    return sql.connect(host=AppConfig.DB_HOST,
                       user=AppConfig.DB_USER,
                       password=AppConfig.DB_PASSWORD,
                       database=AppConfig.DB_NAME,
                       port=AppConfig.DB_PORT
                       )
test = create_connection()
print(test)


def initialize_db():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS records (
            id CHAR(36) NOT NULL DEFAULT (UUID()) PRIMARY KEY,
            place VARCHAR(255) NOT NULL,
            temp FLOAT NOT NULL,
            feel FLOAT NOT NULL,
            wind FLOAT NOT NULL,
            timestamp TIMESTAMP NOT NULL,
            sunrise TIME NOT NULL,
            sunset TIME NOT NULL
        );
        """

        cursor.execute(query)
        print("Table created successfully or exists")
        cursor.close()
    except Exception as e:
        print(e)

def insert_record(data):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO records (place, temp, feel, wind, timestamp, sunrise, sunset)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            data["place"],
            data["temp"],
            data["feels_like"],
            data["wind"],
            data["timestamp"],
            data["sunrise"],
            data["sunset"]
        )

        cursor.execute(query, values)
        conn.commit()
        print("Record inserted successfully into MySQL table")
        cursor.close()

    except Exception as e:
        print(e)

def read_record():
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT * FROM records
        """
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        print(e)
