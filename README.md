Twitter
=======

information cascades analysis for Twitter Network


====
The program is written in python, and includes following components (each file is a component which defines a class):

1. twitterSqlCon.py:  interface to the mysql database.  responsible for basic simple such as table creation, query; and other extended tasks like cascades retrieve.
2. twitter.py:  the main program
3. tree.py:  cascade tree 


====
Dataset:

the raw data is in active_follower_real_sql.sql, distinct_users_from_search_table_real_main and link_status_search_with_ordering_real.csv. 
digg.sql is the exported sql file for the whole database which includes three tables: 

active_follower_real:  following relationship
links:  tweet weblink
users:  user profile
tweets: raw tweets


