# Free code camp Python tutorial

I found this tutorial on Youtube and decide try it. I have already virtualenv, python 3.7 and Pycharm installed on my machine. So first thing is to created the project folder and the virtual enviroment.

```bash
$ mkdir FreeCodeCamp
$ cd FreeCodeCamp
$ virtualenv -p python3 freecodecamp
$ source freecodecamp/bin/activate
$ mkdir giraffeacademy
$ cd giraffeacademy
```

I create a general folder **FreeCodeCamp** that will be my root folder for this project, than I created the virtual environment, activated it and create my python project folder **girafeacademy** this will be the project on git.
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
Open the git project folder (girafeacademy) on pycharm and set the python interpreter as your enviroment python. Now you have everything that you need to starting learning python.

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
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ". ")
print("but didn't like being " + character_age + ".")

```

We can test our variable changing their values.

 ```python
character_name = "Tom"
character_age = "50"
```

If we run the code again we will see that the name and age are updated.
We also can change the variable value in the middle of the code.

 ```python
character_name = "Tom"
character_age = "50"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

character_name = "Mike"
print("He really liked the name " + character_name + ". ")
print("but didn't like being " + character_age + ".")
```

If you run this code you will see on your console that on the first line the name Tom appear but in the fourth line the name is Mike.

We have many types of variables in python but we will see the three types that is most  usable in python, there are strings (like we use in out previous example), Numbers (that could be integers or not) and boolean (True or False, must be captal letter).

 ```python
#Strings must be inside " "
character_name = "Tom"

#Numbers
character_age = 50 #Interger
character_height = 1,60 #Not integer

#Boolean
is_male = True
```

## Working with Strings
Strings are one of the most used variable on python programs. We can have simple string as we did  before.
 ```python
print("Giraffe Academy")
```

When we are working on strings some times you need to break line, so we can use "\n" and the message will be displayed on a differnt line. If you want to write a quotation mark we need to put a special caracter ("\") before so python will know that is just a caracter and not the end of our string.

 ```python
print("Giraffe\nAcademy")
print("Giraffe \"Academy\"")
```

We can use variables on our code when we are working with string and you can also concatenate strings just add then with + sing.

 ```python
phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool.")
```

Strings types have some fucntions like .lower() or .upper() that will change our string to lower case or upper case.

 ```python
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
```

We can combine functions as we will see in the next code example.
 ```python
phrase = "Giraffe Academy"
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
```

When we run the code above we will see on Pycharm console False and True. This is because the frist line not all the letters are upper case so it return False, but when you use the .upper() function before them all the letter are on upper case so the fucntion .isupper() return True. On the fourth line we can see a new function len(), this function count how many chacacters have our string.
