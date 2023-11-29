# Weather Station


## Intro Project

This project has been set up to prepare for a working assignment which will use the Python Django framework,
Python package Numpy and the Python Package Pandas in the context of hydrology. Greating an entire
hydrological models seems a lit to ambitous, so as a result has been decided to create a simple weather
station application, where can be practiced with all relevant technologies.

The goal of this project was to build a simple web application where users can fill in their own personal 
weather observations. This data can then be used to perform various operations on such as statistical
analyses, and compare their data to data input by other users. This
application works with users accounts and the data should be saved in a database.  

### Current Features
- Users can register and login (session management to be implemented)
- Accounts are managed by built in functionality of Django
- Users can get a quick analysis of a csv data sheet (examples are in data folder)
- Data is cleaned before analysis are run
- Users can log temperature and windspeed data to database (currently SQLite)
- Users can get a comparison of their data to the data logged in the database
- Users can get a correlation between two timeseries for temperature & windspeed


## Details Software Stack/ Architecture
- The application has been set up with a Client Layer, an API layer, a Domain layer and a Persistence layer
- Domain is implemented in Python, an interface is used to encourage modularity
- Test set up initialized using Django testing
- The Backend has been implemented using the Django framework Django REST framework
- The frontend is implemented either using a separate Vite server hosting a React Frontend
- The built in database SQLite is used for the persistence layer



## Technical learninggoals (tools, frameworks, etc.):
- Getting experience with the Django Framework
- Getting more experience with a Python project
- Getting experience with the numpy & pandas packages 

## Start Frontend server

The Frontend server can be activated by running the following command in the client folder:
```
npm run dev
```
This will start a vite-server hosting the react frontend on the following adress:

http://localhost:5173/

## Start Backend server
The Backend server can be activated by running the following command in the django folder:
```
python manage.py runserver

```
This will start a Django development server hosting the djangobackend on the following adress:

http://127.0.0.1:8000/

However communication with this backend is handled by the front end which uses a proxy server to talk to the backend server.


## Tests
Tests can be run by using the command from the djangobackend/dataprocessing directory, 
here "dataprocessing" can be changed for another app name

```
python manage.py test dataprocessing.tests
```

## Initial planning in MoSCoW format

### Musts
- Users can fill in temperature data
- Basic statistical information will be given to the users
- Data will be stored in the database
- Data should be validated on realistic ranges (such as no temperature above 55 C in NL )

### Shoulds 
- Weather trends should be visualised
- Fancy visualizations
- More advanced analyses regressions etc.
- Users can input csv files
- Users should be able to customize a short user profile
- Generate general weather report

### Coulds
- Make a map visualization that shows the locations of all visualisations
- Users can add comments to their visualisations
- Download historical data to validate data
- Download weather reports
- Users can make their own accounts


### Woulds/Wont's:
- Sharing data reports on social media
- Implement real time weather status
- Implement machine learning predictions









