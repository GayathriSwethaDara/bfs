from flask import *
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb://localhost:27017")
db=client['USERS']
userdetails=db.VALUES

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/home')
def home1():
    return render_template("home.html")

@app.route('/balance')
def balance1():
    return render_template("balance.html")

@app.route('/deposit')
def deposit1():
    return render_template("deposit.html")

@app.route('/withdraw')
def withdraw1():
    return render_template("withdraw.html")

@app.route('/feedback')
def feedback1():
    return render_template("feedback.html")

@app.route('/contact')
def contact1():
    return render_template("contact.html")

@app.route('/payment')
def payment1():
    return render_template("payment.html")

app.route('/payment1')
def payment11():
    return render_template("payment1.html")

app.route('/payment2')
def payment2():
    return render_template("payment2.html")

@app.route('/register')
def registration():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/hloan1')
def hloan1():
    return render_template("hloan1.html")
@app.route('/hloan')
def hloan():
    return render_template("hloan.html")
@app.route('/house')
def house():
    return render_template("house.html")

@app.route('/eloan1')
def eloan1():
    return render_template("eloan1.html")
@app.route('/eloan')
def eloan():
    return render_template("eloan.html")
@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/vloan1')
def vloan1():
    return render_template("vloan1.html")
@app.route('/vloan')
def vloan():
    return render_template("vloan.html")
@app.route('/vehicle')
def vehicle():
    return render_template("vehicle.html")

@app.route('/gloan1')
def gloan1():
    return render_template("gloan1.html")
@app.route('/gloan')
def gloan():
    return render_template("gloan.html")
@app.route('/gold')
def gold():
    return render_template("gold.html")

@app.route("/registered",methods=['GET','POST'])
def onsubmit():
    fname = request.form.get('fn')
    lname = request.form.get('ln')
    mob = request.form.get('mb')
    db= request.form.get('dob')
    gender = request.form.get('r')
    email = request.form.get('e')
    username = request.form.get('uname')
    password = request.form.get('password')
    a = {"First Name": fname, "Last Name": lname, "Mobile Number": mob, "Date of Birth":db,"Gender":gender, "Email":email,"Username":username, "Password":password}
    userdetails.insert_one(a)
    return render_template('about.html')

@app.route('/logged', methods=['POST'])
def loggedin():
    usname = request.form.get('uname')
    pw = request.form.get('password')
    signin_user = userdetails.find_one({'Username': usname})
    signin_pw = userdetails.find_one({'Password': pw})
    if signin_user and signin_pw:
        return render_template("about.html")
    else:
        return render_template("register.html")

@app.route("/deposited",methods=['GET','POST'])
def deposit():
    accno =request.form.get('an')
    amount =request.form.get('bd')
    c = {"Account Number":accno, "Amount":amount}
    userdetails.insert_one(c)
    depo_user = userdetails.find_one({'Account Number':accno})
    if depo_user:
        return render_template("about.html")
    else:
        return render_template("deposit.html")

@app.route("/withdrawed",methods=['GET','POST'])
def withdraw():
    accno =request.form.get('an')
    amount =request.form.get('wd')
    c = {"Account Number":accno, "Amount":amount}
    userdetails.insert_one(c)
    withdraw_user = userdetails.find_one({'Account Number':accno})
    if withdraw_user:
        return render_template("about.html")
    else:
        return render_template("withdraw.html")

@app.route("/balanced",methods=['GET','POST'])
def bal():
        return render_template("balance.html")


if __name__=="__main__":
    app.run()