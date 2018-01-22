# Intelligent-Task-Manager

Dies ist ein Projekt zur intelligenten Verteilung und Verwaltung von Tasks auf verschiedenen Rechnern. Das Projekt findet im Rahmen des SWE Projektes des Dualen Studiengans "Matse" an der FH-Aachen statt.

## Dependencies
- Python3
- Flask
	- `pip install Flask`
- MongoDB

## Virtual Env
Before programming you need to source the venv.
cd into the source folder and:
On linux execute `source venv/bin/activate`.
On windows execute `venv\bin\activate`.

## Folder structure
folder              | use case
--------------------|--------------------------
src                 | contains the program
src/Webserver       | is the flask Webserver that is executed to start the intelligent task manager
src/Webserver/Client| the client package, contains all functions and classes by from the client
src/Webserver/Server| the server package, contains all functions and classes by from the server
