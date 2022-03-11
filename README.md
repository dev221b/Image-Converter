# Project Name : Image Resizer/Converter
This project can be used to resize an image to desired dimensions and also to convert the format of an image from one to another. This is an efficient project which can be used effortlessly by anyone. The help comments direct the user on what to do. The project can also be further modified to rotate or filter images and so much more. In short, this simple yet powerful project can be used to apply quick efficient changes to an image by using very few lines of code.
## Team Members and Personal Github URL
Devika B - https://github.com/dev221b
Nazal Thanzeer VN - https://github.com/nazalthanzeervn
## Team ID : Python / 330
## Link to product walkthrough
https://www.loom.com/share/556cf227714240c28768425ada422bef
## How it Works?
The project works on the PILLOW library 
Typer library is used to implemnt command line interface so that the users can effortlessly use the project
The project has two functions : resize and convert
Resize : The function is used to resize the concerned immage to the desired width and height. It accepts the input file location, desired width and height as integers and the output file location. The resized image is stored in the specified output location.
Convert : The function is used to convert the format of the image concerned. The function accepts the input file location, the current format of the image and the desired format. For example, if the image is in jpeg format and the user needs to convert it into png format, the function effectively produced an image in the desired format and saves it with the same name but in different format in your system.
## Libraries Used
PILLOW - 9.0.1
Typer - 0.3.2
## How to configure
Install any Pyhton version (3.6 or above recommended)
pip install typer and Pillow
## How to Run
Type "typer .\Image_Converter.py run <command you wish to run> <input paramaters>"
In case of confusions, type "typer .\Image_Converter.py --help" and the instructions or command help will be displayed making the project easy and efficient at the same time.
