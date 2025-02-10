import typer

from kjl.time import get_time_from_timestamp

app = typer.Typer()

@app.command()
def epoch(timestamp: int, timedelta: int = 9):
    time = get_time_from_timestamp(timestamp=timestamp, timedelta=timedelta)
    print(time)


@app.command()
def hello(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    app()
