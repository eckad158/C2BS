# C2BS
ConfluenceToBooksStack

STATUS: Work in Progress

I am currently writing a python application that uses the confluence Rest API to extract the content from a running instance and then imports it to a bookstack instance using its Rest API.

According to https://github.com/BookStackApp/BookStack/issues/43 a real import feature for Bookstack is not planned and will not be implemented. 
So i want to start my own approach to transfer our valuable data to our new Bookstack instance.

## Update 01.02.2022
Found two required Libraries and started implementing first Methods:

Confluence API Wrapper
https://atlassian-python-api.readthedocs.io/confluence.html

and 

Bookstack API Wrapper
https://github.com/coffeepenbit/bookstack

