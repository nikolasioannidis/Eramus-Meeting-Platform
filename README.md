# ERASMUS+ Meeting Platform
#### Video Demo: https://youtu.be/cXfP1BmzKis
#### Description: 
My name is NIKOLAOS IOANNIDIS and this is my final project for CS50x and its called Erasmus+ Meeting Platform and its an online platform for people who join the erasmus project to find each other and link up.
You create your profile by giving some informations like your name, the city, the country, the universiy and etc. you are going for erasmus and you can search for people who are going to the same country and city as you and to the same university.

**database.db:**
It's a database in SQLite that contains 3 tables and 1 index. The first table is **users** where is stored the id, username and password of each user. The second table is an automatically created table to keep track of autoincrement column named id. The third table is **users_info** where is stored the user_id, country, city, uni(university), season, preference, name(first name), last(last name), department. The **index** on username is created so we can retrieve faster the username of the users. 

**helpers.py:**
At the top of the file (lines 1-2) i import from flask redirect so i can redirect the user in an other html page , render_template so i can show to the user the html pages, session so my web app can remember information such as password username etc. of each user. I also import wraps from functools so i can define the login_required function that returns a function that checks if the user has loged in so that he can have access to certain routes. Also there is the apology function that displays an error message, inside that function is also defined the escape function that it simply used to replace special characters in apologies.

#Inside the app.py file:

**app.py:**
At the top of the file (lines 1-6) i import SQL so i can have a database to store the information of the users like i mention before. From flask i import FLASK so i can create my web application i also import redirect so i can redirect the user in an other html page and render_template so i can show to the user the html pages, request so my web app can receive the information the users sent and session so my web app can remember information such as password username etc. of each user. From werkzeug.security i import check_password_hash and generate_password_hash so the password from each user is stored as with hashes for security. Lastly from helpers i import apology in case of any errors and login_required so some features to work after the user has loged in.

From line 8 through 27 i make the file a flask application i make this session to have a default time limit after which it will expire and store the files in my ide account. Then i set cache-control to no-cache so that a browser may cache a response, but must first submit a validation request to an origin server and no-store so browsers aren’t allowed to cache a response and must pull it from the server each time it’s requested and this setting is mostly used for sensitive data.
Lastly open the database file as an SQLite database.

**register:**
In this part i implement the register route. When the request method is GET the html page **register.html** is rendered where i use from bootstrap the from controls that give textual an upgrade. When the method is POST the user puts his username and password and as well as confirmation password and i use session to remember the users info. I save the users password as hashes for security reasons. Lastly if the user doesn't input a field or if the password and confirmation password don't match an error message with a photo of a cat appears from the **oops.html** template and i also check if the username they use is tanken.

**login:**
In this part i implement the login route. When the request method is GET the html page **log_in.html** is rendered and a log in form appears that asks the user to write his/her username and password as well as a short text saying "Don't have an account? Register" and Register is a link that when clicked the user goes to the register form. When the request method is POST the user inputs his/her username and password and the app is checking if the username and password match and after that the user logs in and is redirected to the homepage.

**homepage:**
In this part i implement the homepage of my wep app. At first the web app greets the user with his/her username and the **homepage.html** is rendered where the user can search for people that will go to the same country, city and university as them and in the same semester (winter or summer), i deliberately made it so the user has only two options so they can't write something wrong. When the search button is clicked a list from all the users that are matching the search are shown with their names , last names, the department their studying, emails and their preference that they would like to make friends (extrovert or introvert). If the user doesn't input any of those fields and clicks search an error message will appear from **oops.html** page. For the list of people i use jinja to iterate through the infos table.

**log_out:**
In this part i clear the session and redirect the user to the log in route.

**profile:**
In this part i implement the profile of each user. When the request method is GET a form for the user to input informations about his name, last name , the country he is going to, the city he will be studying , the university , his/her email and department i made them case insensitive. Lastly the season and  preference are made with the option style so the user won't mistype anything. When the request method is POST the information the user has provided are beeing stored and shown to him/her as a list in a table that i used jinja iterate through. Lastly if the user doesn't input any of those informations the error message will appear.

**change password:**
In this part i implement a way so the user can change his password. When the request method is GET the **change_password.html** page is rendered and it is the same html page as log in but without the text about the register. When the request method is POST the user inputs a new password and confirm it and the password in the database is updated.   

**layout.html:**
This html page is the layout of all the html pages. It contains bootstrap and a link to a css stylesheet for the style of the web app. It also contains the meta tag so the web app is compatible with phones. Also in the layout there is the navbar i use so the user can go from one html page to another. Also if the user is not loged in they only see the register and the log in options but when they finally log in the see the options homepage, profile and a dropdown menu named settings where the user can switch to dark mode and back to light mode, change his password and log out. At the bottom of the file the darkMode and lightMode functions are defined with javascript.

**styles.css:**
In this file are implemented the style of the navbar and the dark mode.

**requirements.txt:**
Here are all the libraries we use cs50, Flask, Flask-Session, requests.


