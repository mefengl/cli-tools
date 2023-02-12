from datetime import datetime, timedelta
import os
import requests
import typer

app = typer.Typer()

# Load API key from environment variable
API_KEY = os.environ.get("WAKATIME_API_KEY")

@app.command()
def last_week():
    # Retrieve coding statistics for the last 7 days
    start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")
    time_range = f"start={start_date}&end={end_date}"
    response = requests.get(f'https://wakatime.com/api/v1/users/current/summaries?{time_range}&api_key={API_KEY}')
    last_week = response.json()['data'][-7:]
    for day in last_week:
        typer.echo(f"{day['range']['date']}: {day['grand_total']['text']}")

@app.command()
def last_month():
    # Retrieve coding statistics for the last 30 days
    start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")
    time_range = f"start={start_date}&end={end_date}"
    response = requests.get(f'https://wakatime.com/api/v1/users/current/summaries?{time_range}&api_key={API_KEY}')
    last_month = response.json()['data'][-30:]
    for day in last_month:
        typer.echo(f"{day['range']['date']}: {day['grand_total']['text']}")

if __name__ == "__main__":
    app()
