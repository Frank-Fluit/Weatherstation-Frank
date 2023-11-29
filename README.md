# Weather Station


## Intro Project

This project has been set up to prepare for a working assignment which will use the Python Django framework, Python package Numpy and te Python Package Panda's in the context of hydrology. Greating an entire hydrological models seems a lit to ambitous, so as a result has been decided to create a simple weather station application, where can be practiced with all relevant technologies.

The goal of this project is to build a simple web application where users can fill in their own personal weather observations. This data can then be used to perform various operations on such as statistical analyses, generating visualizations, and compare their data to data input by other users. This application should work with users accounts and the data should be saved in a database.  
### Current Features
- Users can register and login (session management to be implemented)
- Users can get a quick analysis of a csv data sheet (examples are in data folder)
- Users can log temperature and windspeed data to database (currently SQLite)
- Users can get a comparison of their data to the data logged in the database
- Users can get a correlation between two timeseries for temperature & windspeed


## Details Software Stack/ Architecture

- Domain is implemented in Python, an interface is used to encourage modularity
- Test set up initialized using Django testing
- The Backend has been implemented using the Django framework with support for MSQL databases & Django REST framework
- The frontend is implemented either using a separate Vite server hosting a React Frontend






## Persoonlijk Leerdoelen (proces)
- Meer zelfstandig werken?
- Het grote plaatje in het oog blijven houden


## Technisch Leerdoel (tools, frameworks, etc.):
- Ervaring opdoen met het Django framework
- Ervaring opdoen met een Python project
- Ervaring opdoen met numpy & pandas packages 

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


## tests
tests can be run by using the command from the djangobackend/dataprocessing directory, 
where "dataprocessing" can be changed for another app name

```
python manage.py test dataprocessing.tests
```

## initial planning in MoSCoW format

### Musts
Users can fill in temperature data
Basic statistical information will be given to the users
Data will be stored in the database
Data should be validated on realistic ranges (such as no temperature above 55 C in NL )

### Shoulds 
Weather trends should be visualised
Fancy visualizations
More advanced analyses regressions etc.
Users can input csv files
Users should be able to customize a short user profile
Generate general weather report

### Coulds
Make a map visualization that shows the locations of all visualisations
Users can add comments to their visualisations
Download historical data to validate data
Download weather reports
Users can make their own accounts


### Woulds/Wont's:
Sharing data reports on social media
implement real time weather status
implement machine learning predictions









