from flask import Flask, render_template,request, redirect, url_for, session
app=Flask(__name__)
app.secret_key="secret"

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("member"))
    else:
        return render_template("index.html")

users = {
    "test":{
        "password":"test"
    }    
}



@app.route("/signin", methods=['POST'])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username != "" and password != "":
        if username in users and password == users[username]["password"]:
            session["username"] = username   
            return redirect(url_for("member"))
        else:
            return redirect(url_for("invalid_account"))
    else:
        return redirect(url_for("empty"))
@app.route("/member")
def member():    
    if "username" not in session:
        return redirect(url_for("index"))
    else:
        return render_template("member.html")

@app.route("//error?message=empty")
def empty():
    return render_template("empty.html")
@app.route("/error?message=invalid_username_or_password")
def invalid_account():
    return render_template("invalid_account.html")

@app.route("/signout", methods=['GET'])
def signout():
    session.pop("username",None)    
    return redirect(url_for("index"))

@app.route("/square", methods=['POST'])
def square():    
    integer = int(request.form["integer"])
    if integer >= 0 :
        return render_template("square.html",integer=integer)
@app.route("/square/<int:Number>")
def square_dynamic(Number):
    integer = Number    
    return render_template("square.html", integer=integer)

if __name__=="__main__":
    app.run(port=3000)