# Free code camp Python tutorial

I found this tutorial on Youtube and decide try it. I have already virtualenv, python 3.7 and Pycharm installed on my machine. So first thing is to created the project folder and the virtual enviroment.

```bash
$ mkdir FreeCodeCamp
$ cd FreeCodeCamp
$ virtualenv -p python3 freecodecamp
$ source freecodecamp/bin/activate
$ mkdir girraffeacademy
$ cd girraffeacademy
```

I create a general folder **FreeCodeCamp** that will be my root folder for this project, than I created the virtual environment, activated it and create my python project folder **girrafeacademy** this will be the project on git.
Now I will make this folder a git project, create a README.md file and make my first commit.
> Before this steps I have created a new repository on github name FreeCodeAcademyPython and copy the repository url. 

```bash
$ echo "# FreeCodeAcademyPython" >> README.md 
$ git init
$ git add README.md
$ git commit -m "first commit"
$ remote add origin <<Repository URL>>
$ push -u origin master
```
Open the git project folder (girrafeacademy) on pycharm and set the python interpreter as your enviroment python. Now you have everything that you need to starting learning python.

## Hello World
 To start we will create a new python file on the project, app.py. On this file we will write the following command
```python
print ("Hello World!")
```
You can now run the code and check the message printed on Pycharm console.

## Drawing a Shape
On this part we will draw a shape with the print function in multiple lines.
```python
print ("    /|")
print ("   / |")
print ("  /  |")
print (" /   |")
print ("/____|")
```

After run that we can see the draw that we did on Pycharm console. Python execute every line from top to bottom and the order matter. If we change the order and run the code again we will see that the draw doesn't show a triangle anymore.
```python
print ("/____|")
print ("    /|")
print ("   / |")
print ("  /  |")
print (" /   |")
```

## Variables and Data Types
To begin we will change the what we are printing to the George's Tale.
```python
print("There once was a man named George,")
print("he was 70 years old.")
print("He really liked the name George.")
print("but didn't like being 70.")
```

So if we want to change the character name to John we have to look in all our code and change the places were George appear. The same thing if we want to change the character age. So to make it easier we will create two variables: "character_name" and "character_age" and we will chage our print function to print the variable values.


 ```python
character_name = "John"
character_age = "35"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + "years old. ")
print("He really liked the name " + character_name + ". ")
print("but didn't like being " + character_age + ".")

```
