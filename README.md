# Intelligent-Task-Manager

Dies ist ein Projekt zur intelligenten Verteilung und Verwaltung von Tasks auf verschiedenen Rechnern. Das Projekt findet im Rahmen des SWE Projektes des Dualen Studiengans "Matse" an der FH-Aachen statt.

## Dependencies
- Python3
- Python Modules:
	- Flask
		- `pip install Flask`
	- requests
		- `pip install requests`
	- PyMongo
		- `pip install pymongo`
- MongoDB

## Folder structure
folder              | use case
--------------------|--------------------------
src                 | contains the program
src/Webserver       | is the flask Webserver that is executed to start the intelligent task manager
src/Webserver/Client| the client package, contains all functions and classes by from the client
src/Webserver/Server| the server package, contains all functions and classes by from the server
