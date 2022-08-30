# sqlalchemy-challenge
Module 10 Challenge

# Description
The challenge combines everything learned up to this point and begins to layer on top of it advanced data storage and retrieval using SQLAlchemy and the concept object-relational mapper (ORM). ORM has many advantages to raw SQL queries. With an ORM, the user can write one code to update and maintain. The code points to one reference. Another advantage of an ORM is its ability to adapt to the different vendor specific relational database management systems, reducing syntax errors. ORMs shield from SQL injection attacks, increasing the security of a framework. The code becomes more resilient and robust. But one major disadvantage is that an ORM can slow things down quite a bit, especially when working with a large framework that is perfomance sensitive.

Using climate data from weather stations in Hawaii, the challenge walks through various climate analysis and exploration. In this repository, there are three Jupyter notebooks, one Python script and a Resources folder. In the Resources folder, two raw CSV data files and a SQLITE file that contains a weather table and a weather station table. Using Python and SQLAlchemy, the first part of the challenge involves climate analysis and exploration. The climate_starter notebook performs queries to complete precipitation and station analysis with Pandas and Matplotlib.

The second part of the challenge introduces the Flask module. Using Flask, the app.py script designs a climate API based on the queries from the first part to return precipitation, station and temperature information. The user can also query the API with a date and/or date range to return the minimum, maximum and average temperature in that period. The challenge also includes two bonus temperature analyses for specific vacation dates to give the user an idea of what to expect when visting Hawaii.

# Visuals

Precipitation Chart from 2016-08-23 to 2017-08-23

![image](https://user-images.githubusercontent.com/107419765/187490095-07e9b5b6-1b6e-460d-9043-f79671b77953.png)

Temperature Frequency from 2016-08-23 to 2017-08-23

![image](https://user-images.githubusercontent.com/107419765/187490191-bd9a41aa-06ac-49be-b04b-9bd6ab565085.png)

Average Temperature during Vacation Dates (2017-08-01 to 2017-08-07)

![image](https://user-images.githubusercontent.com/107419765/187490373-cc727b45-49b9-403e-8d5e-67deb71cf3c1.png)

Precipitation during Vacation Dates (2017-08-01 to 2017-08-07)

![image](https://user-images.githubusercontent.com/107419765/187490544-39f4641d-5824-4322-83e1-29d4b3715dbc.png)
