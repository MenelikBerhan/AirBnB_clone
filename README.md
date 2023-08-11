# AirBnB clone project

## Description

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## Environment

- **OS:** Ubuntu 14.04 LTS
- **language:** Python 3.4.3
- **style:** PEP 8 (v. 1.7.0)
- **web server:** nginx/1.4.6
- **web server gateway:** gunicorn (version 19.7.1)
- **database:** MySQL 5.7.8-rc
- **documentation:** Swagger (flasgger==0.6.6)

## Installation

To use the console, clone the repository and start it with the following command:

```
git clone https://github.com/MenelikBerhan/AirBnB_clone.git
cd AirBnB_clone
```

## Usage

To use the console in interactive mode, run the executable without any arguments:

```
./console.py
```

To use the console in non-interactive mode, pipe any command into it:

```
echo "help" | ./console.py
```

The following commands are available:

- **create**: Creates a new instance of a class, saves it (to the JSON file) and prints the id.
- **show**: Prints the string representation of an instance based on the class name and id.
- **destroy**: Deletes an instance based on the class name and id (save the change into the JSON file).
- **all**: Prints all string representation of all instances based or not on the class name.
- **update**: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

## Examples

```
(hbnb) create BaseModel
(hbnb) show BaseModel 1234-1234-1234
(hbnb) destroy BaseModel 1234-1234-1234
(hbnb) all
(hbnb) all BaseModel
(hbnb) update BaseModel 1234-1234-1234 email "
(hbnb) quit
```

## Authors

- [**Toby Salau**](https://github.com/Toby2507)
- **Menelik Berhanu**
