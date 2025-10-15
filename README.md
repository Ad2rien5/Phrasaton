# Phrasaton  
*v1.0*

## Description

As part of my ongoing exploration of computer science, I set about developing a ChatBot using Python, but with a different approach. Unlike conventional methods, which often rely on specialised artificial intelligence libraries such as SciPy, I decided to take up the challenge and develop my own from scratch.

For me, this project represents a stimulating opportunity to explore new approaches in the field of artificial intelligence and to apply my programming skills. I'm looking forward to its further development and sharing my progress!

## Usage

This application is a Python project for which it is recommended that you create 
your own environment. Then you can install the necessary dependencies. Those are 
located in the *requirement.txt* file. And finally, you can run the *main.py* 
file to launch the app.  
The method for doing this varies depending on your operating system.  

### On Windows :  
```ps
cd {path_to_the_project}\Phrasaton
py -m venv .venv
.venv\bin\activate
pip install -r requirement.txt
py app\src\__main__.py
```  
### On Linux :  
```sh
cd {path_to_the_project}/Phrasaton
python3 -m venv .venv
source .venv\bin\activate
pip install -r requirement.txt
python3 app/src/__main__.py
```  

## Technology Involved

### Python

This language will be used throughout the project, on both the frontend and the backend.  
I chose this language for its flexibility, and also because it has always inspired me a lot and I love discovering new ways of using it.

### Tkinter

This library is used to create interfaces simply and efficiently.

## List of advances and future features

### 1.0
- be functional  
	- uses **one** previous word to find the next one  
	- simple, usable interface  
	- can recognise if a sentence is incorrectly formed  

### 1.1
- implement tests  
	- from this version onwards, each new feature will necessarily be accompanied by multiple tests  

### 1.2
- have a command to retrieve the current database in JSON format  
- have a command to complete a database from a JSON format  
	- checks that the JSON format is correct  
	- adds the data contained in the JSON   
	
### 1.3
- improve the interface  
	- add a menu before arriving on the ChatBot  
- parameter  
	- add a button to save and load JSON  
	- choice of language  
		- French  
		- English  
- improve security against XSS attacks  

### 2.0
- see if a tree-like data architecture makes it more powerful  
- use the previous **two** words to find the next one  
- implement the notion of *subject*  
- implement a data sort  

## Term of Use

You can use this code as you wish as long as you credit me for your product.

## Contributor

Séac'h Adrien