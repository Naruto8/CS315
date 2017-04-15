# CS315
this is a project which has been done as a part of the course CS315

we have implemented a basic tool to stream random tweets from twitter, and store it in a mysql database.
this data can now be used further to carry out various twitter data analysis queries to extract valuable information from it.

the collect_tweet.py file listens to twitter stream , selects tweets randomly and stores it in a mysql database (testdb in this case). this python script will stream tweets into the database in real time. so to gather sufficient information about tweets and also the users who have posted said tweets, the script needs to be run for an extended period of time.

the create.sql file needs to be run after creating the database "testdb" and creating a user to use the database as specified in "user & db info".
steps to use:-

1) create a New MySQL User and Database
create database testdb;
create user 'testuser'@'localhost' identified by 'password';
grant all on testdb.* to 'testuser';

2) login using testuser
mysql -u testuser -p

3) run create.sql

4) run collect_tweet.py
wait for some time ( usually a couple of hours to get ample data)
