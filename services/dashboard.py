from flask import Flask, render_template, request
from common.config import AppConfig
import pandas as pd
from services.openweather_api import get_weather
def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    @app.get("/")
    def index():

        return render_template("index.html")

    @app.get("/wyniki")
    def wyniki():
        df = pd.read_excel(AppConfig.WEATHER_FILE[0])
        latest_row = df.head(1)
        city = df["place"].unique()[0]

        latest = latest_row.to_dict(orient="records")[0]
        # Konwertuje dataframe do zwykłej listy ze słownikami
        df = df.to_dict(orient="records")

        print(latest)

        return render_template(
            "wyniki.html",
            df=df,
            city=city,
            latest=latest
        )

    @app.route("/wyszukaj", methods=["GET","POST"])
    def wyszukaj():
        weather = {}
        if request.method == "POST":
            try:
                query = request.form["query"]
                if query !=0 and query != "":
                    weather = get_weather(query)
                    return render_template(
                        "wyszukaj.html",
                        weather=weather
                    )
            except Exception as e:
                return f"error {e}"
        elif request.method == "GET":
            return render_template("wyszukaj.html")
        else:
            return f"error {request.method}"
    return app