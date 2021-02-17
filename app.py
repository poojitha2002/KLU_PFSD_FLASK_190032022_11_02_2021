from flask import Flask,render_template
app=Flask(__name__)

gifts=[
      {'name':'Cards', 'type':'hardcopy',
        'quantity':34,'price':255
      },
       {'name':'idle', 'type':'glass',
        'quantity':3,'price':2552
      },
       {'name':'metal', 'type':'hardcopy',
        'quantity':2,'price':2155
      }
      ]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html",title="GS-Home")
@app.route("/register")
def register():
	return render_template("register.html",title="Join now")
@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/view")
def view():
	#flask requires data to be sent in form of dict only.
	return render_template("view.html",gifts=gifts)
@app.route("/contact-us")
def contactUs():
	return render_template("contact.html")
	
