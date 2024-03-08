![image](https://github.com/yene2024/holbertonschool-AirBnB_clone/assets/142119219/356b83b1-b150-416e-b90e-7c96795c640d)

# AirBnB clone - The console

## Description

This project is the begining of Holberton School Air BnB Clone. We've begun by creating the console that carries out funcitons on the currently available objects.

## Resources

### Read or watch:

    cmd module
    cmd module in depth
    packages concept page
    uuid module
    datetime
    unittest module
    args/kwargs
    Python test cheatsheet
    cmd module wiki page
    python unittest

## General
# Command Line Interpreter for Airbnb Clone - The Console
This command line interpreter is designed for an Airbnb clone application. It allows users to interact with the application's backend through a console, where they can create and manage instances of the application's classes.

## How to Use

To start the console, run the script console.py. This will start the command line interpreter, and the prompt (hbnb) will be displayed. This prompt indicates that the console is ready to accept user input.

The following commands are available:

    create: Creates a new instance of a class.
    show: Prints the string representation of an instance.
    destroy: Deletes an instance based on the class name and ID.
    all: Prints all string representations of all instances, or all instances of a particular class.
    update: Updates an instance based on the class name and ID.
    count: Counts the instances of a class.
    EOF: Exits the console.
    quit: Exits the console.

The syntax for each command is as follows:

    create <class name>: Creates a new instance of the specified class.
    show <class name> <instance id>: Prints the string representation of the specified instance.
    destroy <class name> <instance id>: Deletes the specified instance.
    all: Prints the string representations of all instances.
    all <class name>: Prints the string representations of all instances of the specified class.
    update <class name> <instance id> <attribute name> "<attribute value>": Updates the specified instance with the specified attribute value.
    count <class name>: Counts the instances of the specified class.

## Requirements
### Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle (version 2.8.*)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    You have to use the unittest module
    All your test files should be python files (extension: .py)
    All your test files and folders should start by test_
    Your file organization in the tests folder should be the same as your project
    e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
    All your tests should be executed by using this command: python3 -m unittest discover tests
    You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## More Info
### Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

![image](https://github.com/yene2024/holbertonschool-AirBnB_clone/assets/142119219/64ec91a9-6c13-46aa-bcb3-044eda5be7e3)
