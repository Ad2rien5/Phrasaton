# Phrasaton  
*v1.0*

## Description

As part of my ongoing exploration of computer science, I set about developing a 
ChatBot using Python, but with a different different approach. Unlike 
conventional methods, which often often rely on specialised artificial 
intelligence libraries such as SciPy, I decided to take up the challenge and 
develop my own from scratch.

For me, this project represents a stimulating opportunity to explore new 
approaches in the field of artificial intelligence and to put my apply my 
programming skills. I'm looking forward to its further development and share my 
progress!

## Usage

To use this program, you need to complete several steps. Firstly, you need to 
install the necessary dependencies. These dependencies are written in the 
*requirement.txt* file. Next, you need to show Python where the various 
Phrasaton modules are located. Finally, you need to run the main.py file.

To do all this, you can use these commands :

```shell
pip install -r requirement.txt
pip install -e .
python3 app/src/__main__.py
```

## Technology Involved

### Python

This language will be used throughout the project, on both the frontend and the 
backend.  
I chose this language for its flexibility, and also because it has always 
inspired me a lot and I love discovering new ways of using it.

### Tkinter

This library is used to create interfaces simply and efficiently.

## List of advances and future features

### 1.0
- be functional  
	- uses **one** previous word to find the next one
	- simple, usable interface
	- can recognise if a sentence is incorrectly formed

### 1.1
- implemente tests
	- from this version onwards, each new feature will necessarily be 
  accompanied by multiple tests

### 1.2
- have a command to retrieve the current database in Json format
- have a command to complete a database from a Json format
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
- improve security against XSS attack

### 2.0
- see if a tree-like data architecture makes it more powerful
- use the previous **two** words to find the next one
- implement the notion of *subject*
- implement a data sort

## Term of Use

You can use this code as you wish as long as you credit me in your product.

## Contributor

Séac'h Adrien

---

# Phrasaton  
*v1.0*

## Description
Dans le cadre de mon exploration continue dans le domaine de l'informatique, 
j'ai entrepris de développer un ChatBot en utilisant Python, mais avec une 
approche différente. Contrairement aux méthodes conventionnelles qui font 
souvent appel à des bibliothèques spécialisées en intelligence artificielle 
comme SciPy, j'ai décidé de relever le défi en développant le mien à partir 
de zéro.

Ce projet représente pour moi une opportunité stimulante d'explorer de 
nouvelles approches dans le domaine de l'intelligence artificielle et de 
mettre en pratique mes compétences en programmation. Je suis impatient de 
poursuivre son développement et de partager mes progrès !

## Utilisation

Pour utiliser ce programme, il faut effectuer plusieurs étapes. Tout d'abord, 
il faut installer les dépendances nécessaires au fonctionnement. Ces 
dépendances sont inscrites dans le fichier *requirement.txt*. Puis, il faut 
montrer à Python où se situe les différents modules de Phrasaton. Et enfin, 
il faut lancer le fichier *__main__.py*.

Pour effectuer tout cela, vous pouvez utiliser ces commandes :
```shell
pip install -r requirement.txt
pip install -e .
python3 app/src/__main__.py
```

## Technologie utilisée
### Python 
Ce langage sera utilisé dans tout le projet que ce soit le frontend ou le 
Backend.  
J'ai choisi ce langage pour sa flexibilité, aussi, car ce langage m'a toujours 
beaucoup inspiré et que j'adore découvrir de nouvelle manière de l'utiliser.  

### Tkinter
Cette bibliothèque sert à faire les interfaces de manière simple et efficace.

## Liste des avancées et des futures fonctionnalités

### 1.0  
 - être fonctionnel  
    - utilise **un** mot précédent pour trouver le suivant
    - interface simple et utilisable
    - sait reconnaître si une phrase est mal formée

### 1.1
 - créer des jeux de test (rattraper le retard)
    - à partir de cette version, chaque arrivée de nouvelle fonctionnalité 
   sera forcément accompagnée de jeux de test

### 1.2  
 - posséder une commande pour récupérer la base de donnée actuelle au format 
Json  
 - posséder une commande pour compléter une base de donnée à partir d'un 
format Json
    - vérifie si le format du JSON est correcte
    - ajoute les données contenues dans le JSON

### 1.3  
 - améliorer l'interface 
    - ajouter un menu avant d'arriver sur le ChatBot
 - paramètre 
    - ajouter et loader des JSON
    - choix du langage
        - français
        - anglais
        
 - plus de sécurité anti XSS 

### 2.0
 - voir si une architecture des données sous forme d'arbre rend ça plus 
puissant
 - utilise les **deux** mots précédents pour trouver le suivant
 - implémentation de la notion de *sujet*
 - implémentation d'un trie des données pour les ranger

## Terme d'utilisation  
Vous pouvez utiliser ce code comme vous l'entendez à partir du moment que vous 
me créditez dans votre produit.

## Contributeur  
Séac'h Adrien