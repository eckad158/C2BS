# C2BS
ConfluenceToBooksStack

STATUS: Work in Progress

I am currently writing a python application that uses the confluence Rest API to extract the content from a running instance and then imports it to a bookstack instance using its Rest API.

According to https://github.com/BookStackApp/BookStack/issues/43 a real import feature for Bookstack is not planned and will not be implemented. 
So i want to start my own approach to transfer our valuable data to our new Bookstack instance.

## Update 07.02.2022
* Connections to Instances are now working, sample config file created -> has to be filled and named config.properties
* Rest endpoints and libraries need further investigations
* Reading from the REST-APIs is now working.

## Update 01.02.2022
Found two required Libraries and started implementing first Methods:

Confluence API Wrapper
https://atlassian-python-api.readthedocs.io/confluence.html

and 

Bookstack API Wrapper
https://github.com/coffeepenbit/bookstack

