# Free code camp Python tutorial

I found this tutorial on Youtube and decide to try it. I have already virtualenv, python 3.7 and Pycharm installed on my machine. So the first thing is to create the project folder and the virtual environment.

```bash
$ mkdir FreeCodeCamp
$ cd FreeCodeCamp
$ virtualenv -p python3 freecodecamp
$ source freecodecamp/bin/activate
$ mkdir giraffeacademy
$ cd giraffeacademy
```

I create a general folder **FreeCodeCamp** that will be my root folder for this project, then I created the virtual environment, activated it and create my python project folder **girafeacademy** this will be the project on git.
Now I will make this folder a git project, create a README.md file and make my first commit.
> Before these steps I have created a new repository on Github name FreeCodeAcademyPython and copy the repository URL. 

```bash
$ echo "# FreeCodeAcademyPython" >> README.md 
$ git init
$ git add README.md
$ git commit -m "first commit"
$ remote add origin <<Repository URL>>
$ push -u origin master
```
Open the git project folder (girafeacademy) on pycharm and set the python interpreter as your environment python. Now you have everything that you need to starting learning python.

## Hello World
 To start we will create a new python file on the project, app.py. On this file, we will write the following command
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

After run that we can see the draw that we did on Pycharm console. Python executes every line from top to bottom and the order matter. If we change the order and run the code again we will see that the draw doesn't show a triangle anymore.
```python
print ("/____|")
print ("    /|")
print ("   / |")
print ("  /  |")
print (" /   |")
```

## Variables and Data Types
To begin we will change what we are printing to George's Tale.
```python
print("There once was a man named George,")
print("he was 70 years old.")
print("He really liked the name George.")
print("but didn't like being 70.")
```

So if we want to change the character name to John we have to look in all our code and change the places were George appears. The same thing if we want to change the character age. So to make it easier we will create two variables: "character_name" and "character_age" and we will change our print function to print the variable values.


 ```python
character_name = "John"
character_age = "35"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ". ")
print("but didn't like being " + character_age + ".")

```

We can test our variable by changing their values.

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

If you run this code you will see on your console that on the first line the name Tom appear but in the fourth line, the name is Mike.

We have many types of variables in python but we will see the three types that are most usable in python, there are strings (like we use in our previous example), Numbers (that could be integers or not) and boolean (True or False, must be capital letter).

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
Strings are one of the most used variables in python programs. We can have a simple string as we did before.
 ```python
print("Giraffe Academy")
```

When we are working on strings some times you need to break the line, so we can use "\n" and the message will be displayed on a different line. If you want to write a quotation mark we need to put a special character ("\") before so python will know that is just a character and not the end of our string.

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

Strings types have some functions like .lower() or .upper() that will change our string to lower case or upper case.

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

When we run the code above we will see three lines on our console, the messages False, True and 15. This is because on the first line, not all the letters are upper case so it returns False, but when you use the .upper() function before them all the letters are on upper case so the function .isupper() returns True. On the third line of our console we see the number 15, this is the return of the function len() this function count how many characters have our string.
If we want to print just a specific character of our string we can use some index to do that, and if you don't know what is the index of your character you can use the .index() function to discover it.

 ```python
phrase = "Giraffe Academy"
print(phrase[0]) # To get the first character of phrase the captal G.
print(phrase[3]) # Get the fourth character of phrase the first a.
print(phrase.index("G")) # Show the index of the captal G.
print(phrase.index("a")) # Show the index of the first a.
print(phrase.index("Acad")) # Show the index where our string start.
print(phrase.index("z")) # Bring an error because phrase don't have any z.
```

Another common function of strings is the .replace(), this function receives two parameters the first one is a string to match and the second is what we want to replace. In the next example, we will change "Giraffe" to "Elephant" and we will run will print "Elephant Academy".
 ```python
phrase = "Giraffe Academy"
print(phrase.replace("Giraffe","Elephant"))
```

## Working with Numbers
When working with number on python you can use integer, float, posive, negative and all the mathematical operations addition, subtraction, multiplication and division (**+**, **-** , **\***, **/**). You can also combine multiple operator and define their order by using parentheses.
 ```python
print(2) # Return 2
print(2.0987) # Return 2.0987
print(-2.0987) # Return -2.0987
print(3 + 4) # Return 7
print(3 - 4.5) # Return -1.5
print(3 * 4 + 5) # Return 17
print(3 * (4 + 5)) # Return 27
```

We have another operator that we can use, the mod operation returns the remainder of a division.
 ```python
print(10 % 3) # Return 1. 10/3 is 3 and remains 1.
```

We can use variables to save our numbers just like we did with strings, We can also convert numbers in strings using the str() function, we use this when we want to concatenate numbers and strings.
 ```python
my_number = 5
print(my_number)
print(str(my_number) + " my favorite number.")
print(my_number + " my favorite number.") # Return error because we don't convert our number into a string.
```
Let's see some functions that we can use with numbers. We can get the absolute value of a number with abs() function. We can calculate the power of a number using the pow() function, this required 2 numbers, the first one is the base and the other one is the multiplying. The max() and min() functions show the maximum value and the minimum value of a list. The round() function will round a float number with the basic rules of rounding. Let's see some examples.
 ```python
my_number = -5
print(abs(my_number)) # Return 5
print(pow(3, 2))  # Return 9
print(pow(6, 4))  # Return 1296, 6*6*6*6
print(max(6, 4))  # Return 6
print(min(6, 4))  # Return 4
print(round(3.3)) # Return 3
print(round(3.7)) # Return 4
```

Python has a library specifically for math functions we can import that library to get access from a bunch of new functions. The floor() function returns the lesser integer than the value that we pass. The ceil() function returns the biggest integer than the value that we pass.

 ```python
from math import * # This line allow us to use functions of library math
print(floor(3.7))  # Return 3
print(floor(2.9))  # Retutn 2
print(floor(-5.5)) # Return -6 the next lowest integer value
print(ceil(3.7))   # Return 4
print(ceil(2.9))   # Return 3
print(ceil(-5.5))  # Return -5 the next largest integer value
```

The last function that we will see is sqrt() as the name sugest it return the square root of an number.
 ```python
from math import * # This line allow us to use functions of library math
print(sqrt(16)) # Return 4.
print(sqrt(36)) # Return 6.
print(sqrt(144)) # Return 12.
```

## Getting Input From Users

Now that you are more familiar with prints and some functions let's starting work with the user's input. We will make a program that receives the user's name and we will answer him with a Hi.
We will store the user name and age in two variables using the function input() this function you pass as a parameter the message that your user will see. After that, we will use the variables that we have to print the user information.

 ```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
```

When you run the code above you can check on your python console the message "Enter your name:", you can click on your console and type your name, after that the message "Enter your age:" and you can type your age, as result you will be able to see the "Hello user! You are XX"

## Building a Basic Calculator

We will build a basic calculator that will get two numbers of user and add then.
 ```python
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)
```

Let's run the code above and use numbers 5 and 8.3 as input, as a result, we will have this.
```bash
Enter a number: 5
Enter another number: 8.3
58.3
```
We can see the result is 58.3 instead of 13.3. This happens because the input function convert user input to string no matter what they type. So our result just concatenates the strings, if we want to use the variables as numbers we have to convert then using the int() function.
 ```python
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)
```

We can run and test it with numbers 4 and 5. It will return 9.
Great! Our first calculator is ready and works for any integer number. But try to input 4.3 and 5.5.
This return an error because our code are not able to treath decimal numbers. To change our program to be able to add two decimal numbers we can change the function int(), we will use float() that is a function to convert to not interger numbers.
 ```python
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)
```

Now our calculator can make the sum of any numbers.

## Mad Libs Game

Mad libs game is a phrasal template word game where you fill some blank space with random words.  We will create our game with a famous poem.

 ```python
print("Roses are red")
print("Violets are blue")
print("I love you")
```

For our game, we will change the words "red", "Violets" and "you" to a color, a Plural Noun and a celebrity. We will do this by creating 3 variables called color, plural_noun, and celebrity and get input from the user.
After that, we will change our print functions to print your variables in the right places.

 ```python
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
```

You can run the code above and input some words and check the result.

## Lists
When you are working with python you have to deal with a bunch of data and we have a way to organize that information on lists. We can store value in a variable as we are doing until now, but on lists, we can store multiple values and access then. We will see the basic of lists and some useful functions.

Let's create a list of our friend's names. We have to give a name to our list and say to python that the variable that we are creating is a list and we do this by "[]" characters. The values inside our list are separated by "," as you can see in the example below. We have a list of three friends' names on it, let's printed and see the result.

 ```python
friends = ["Kevin", "Karen", "Jim"]
print(friends)
```