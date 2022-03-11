from PIL import Image
import typer

app=typer.Typer(help="Custom help")

@app.command()
def resize(file:str,width:int,height:int,out:str):
    """
    Accepts input file, new width, new height, output file
    """
    img = Image.open(file)
    img = img.resize((width,height), Image.ANTIALIAS)
    img.save(out)
    print("Saved")

@app.command()
def convert(file:str,input:str,output:str):
    """
    Accepts input file, input format, output format
    """
    img=Image.open(f'{file}.{input}')
    img = img.convert('RGB')
    img.save(f'{file}.{output}')
    print("Converted")
if __name__ == "__main__":
    app()
