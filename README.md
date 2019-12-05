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
