from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import  apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")


@app.route("/register", methods=["GET", "POST"])
def register():
    password = request.form.get("password")
    username = request.form.get("username")
    confirm_password = request.form.get("confirm_password")
    if request.method == "GET":
        return render_template("register.html")
    else:
        # If user doesnt provide username
        if not username:
            return apology("Must provide username")         
        
        # If user doesnt provide password
        if not password:
            return apology("Must povide password") 
        
        # If user doesnt provide confirmation password
        if not confirm_password:
            return apology("Please enter the password again")
        
        # If confirmation password and password doesnt match
        if password != confirm_password:
            return apology("Password and confimation password must match")

        # Save info of user in db  
        hash = generate_password_hash(password)
        try:
            new_user = db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hash)
        except:
            return apology("This username is already in use")
        # Remember user
        session["user_id"] = new_user

        # Redirect to log in
        return redirect("/log_in")   

@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    """Log user in"""
      # Forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("log_in.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            return apology("Please enter username")
            
        if not password:
            return apology("Please enter password")
            
        
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("Invalid password or username")
        
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        return redirect("/")


@app.route("/",  methods=["GET", "POST"])
@login_required
def homepage():
    if request.method == "GET":
        user_id = session["user_id"]
        user = db.execute("SELECT username FROM users WHERE id=?", user_id)
        users = user[0]["username"]
        return render_template("homepage.html", users=users)
    
    else:
        user_id = session["user_id"]
        user = db.execute("SELECT username FROM users WHERE id=?", user_id)
        users = user[0]["username"]
        country = request.form.get("country")
        Country = country.upper()
        if not country:
            return apology("Please provide the country you will be studying")
        city = request.form.get("city")
        City = city.upper()
        if not city:
            return apology("Please provide the city you will be studying")
        university = request.form.get("university")
        University = university.upper()
        if not university:
            return apology("Please provide the university you will be studying")
        season = request.form.get("season")
        if not season:
            return apology("Please provide the season you will be studying")
        infos = db.execute("SELECT name, last, email, department, preference, text FROM users_info WHERE user_id != ? AND country=? AND city=? AND uni=? AND season=?", user_id, Country, City, University, season)
        return render_template("homepage.html", infos=infos, users=users)

 
@app.route("/log_out")
def log_out():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/log_in")


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Profile"""
    user_id = session["user_id"]
    if request.method == "GET":
        
        # Get all the data from users_info
        user_info = db.execute("SELECT * FROM users_info WHERE user_id=?", user_id)

        return render_template("profile.html", user_info=user_info)
    
    else:
        name= request.form.get("name")

        last = request.form.get("last")

        country = request.form.get("country")

        Country = country.upper()

        city = request.form.get("city")
        City = city.upper()

        uni = request.form.get("university")
        Uni = uni.upper()

        season = request.form.get("season")

        preference = request.form.get("preference")

        email = request.form.get("email")
        Email = email.upper()

        department = request.form.get("department")
        Department = department.upper()

        # If user doesnt povide information
        if not name:
            return apology("Plase provide your name")
        if not last:
            return apology("Please provide your last name")
        if not country:
            return apology("Please provide the country you will be studying")
        if not city:
            return apology("Please provide the city you will be stydying")
        if not uni:
            return apology("Please provide the university you will be stydying")
        if not season:
            return apology("Please provide the season you will be stydying")
        if not preference:
            return apology("Please tell us how you want to make friends")
        if not email:
            return apology("Please provide your email")
        if not department:
            return apology("Please provide the department you will be studying")
        

        # Insert the data to the database
        db.execute("INSERT INTO users_info(user_id, country, city, uni, season, preference, name, last, email, department) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", user_id, Country, City, Uni, season, preference, name, last, Email, Department)
        return redirect("/profile")


@app.route("/change password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "GET":
        return render_template("change_password.html")
    else:
        user_id = session["user_id"]
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # Check if the 2 passwords match
        if password != confirmation:
            return apology("Confirmation password and password must match")
        # Check if new pasword is provided
        if not password:
            return apology("Must provide new password")
        hash = generate_password_hash(password)
        db.execute("UPDATE users SET hash=? WHERE id=?", hash, user_id)
        return redirect("/log_in")


        

        









