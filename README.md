0x00. AirBnB clone - The console

Description
This repositoy contains the first AirBnB clone project tasks The Console.
During this first part, I was able to answer the following questions:

    How to create a Python package
    How to create a command interpreter in Python using the cmd module
    What is Unit testing and how to implement it in a large project
    How to serialize and deserialize a Class
    How to write and read a JSON file
    How to manage datetime
    What is an UUID
    What is *args and how to use it
    What is **kwargs and how to use it
    How to handle named arguments in a function

Files description

AUTHORS: This file has a list of individuals that contributed content to the repository.

console.py: It contains a command line interpreter limited to a specific use-case. In in my case, I was managing the objects of the project using this console.

models: This folder contains all the Class modules of the project, and a folder called engine.

tests: This folder contains all the UNITTEST of every module stored in the models folder and the TEST of the console.py file.

Features

Programming language: python3
Style: All modules use the PEP 8 style
Documentation: All modules have documentation, including the functions, classes,etc.
Usage
The console (console.py) works like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  destroy  show  all  update

(hbnb)
(hbnb)
(hbnb) quit
$
But also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  destroy  show  all  update
$

Author
Name	                                GitHub username
Wycliffe Omondi                        odhiambow2354

                      


