import typer 
from dataModeOn import Processing
from validate import Validate

app = typer.Typer()


@app.command()
def helloworld(name: str):
    print(f"fuck you {name}")


#validate commmand
@app.command()
def validate(file: str):
    something = Validate(file)
    something.theLoop()


#processing command
@app.command()
def process(file: str):
    something = Processing(file)
    something.theLoop()
    print(something.getDic())



if __name__ == "__main__":
    app()
