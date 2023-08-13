# HBNB - The Console

**The ALX AirBnB Clone project**

This project aims to build a clone of the AirBnB website. The primary objectives are:

1. Create a program that serializes and deserializes objects into JSON files, allowing data to persist between sessions.
2. Develop a console to manage stored data, enabling the creation, deletion, and updating of instances of various classes.

## Table of Contents

- [Authors](#authors)
- [Pep8](#pep8)
- [Unit Testing](#unit-testing)
- [Make BaseModel](#make-basemodel)
- [Update BaseModel w/ kwargs](#update-basemodel-w-kwargs)
- [Create FileStorage class](#create-filestorage-class)
- [Console 0.0.1](#console-001)
- [Console 0.1](#console-01)
- [Create User class](#create-user-class)
- [More Classes](#more-classes)
- [Console 1.0](#console-10)
- [General Use](#general-use)
- [Contributors](#contributors)

## Authors

- wycliffe Omondi <odhiambow2354@gmail.com>
- Aicha BIRAT     <aichabirat2001@outlook.fr>

## Pep8

All the code in the repository is PEP8 compliant.

## Unit Testing

Unit testing files for the program are located in the `/tests` directory.

## Make BaseModel

The `BaseModel` class is designed to be inherited by every model class in the project. It contains a few useful methods.

## Update BaseModel w/ kwargs

Added functionality to recreate an instance of a class using a dictionary passed with kwargs.

## Create FileStorage class

The `FileStorage` class handles the JSON serialization and deserialization of a file. It reloads the content of the file for use within the program across multiple sessions.

## Console 0.0.1

The initial version of the console program is introduced. It provides basic functionality to quit, handle empty lines, and manage EOF in the input field.

## Console 0.1

The console is updated with methods for creating, destroying, showing, and updating individual objects stored within the file storage system.

## Create User class

The `User` class is introduced, and the console and file storage system are dynamically updated to work with the `User` class.

## More Classes

Additional classes, such as `Place`, `City`, `Amenity`, `State`, and `Review`, are introduced to store various information through the file storage system.

## Console 1.0

The console is updated to work dynamically with all the classes introduced in previous tasks. File storage is also updated to support these changes.

## General Use

1. Clone this repository.
2. Locate the "console.py" file and run it as follows:

   ```bash
   /AirBnB_clone$ ./console.py

