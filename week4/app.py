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
            return redirect("/error?message=invalid")
    elif username == "" or password == "":
        return redirect("/error?message=empty")

            
@app.route("/member")
def member():    
    if "username" not in session:
        return redirect(url_for("index"))
    else:
        return render_template("member.html")

@app.route("/error", methods=['GET','POST'])
def error():
    message = request.args.get("message")
    if message == "invalid":
        errorMessage = "Username or password is not correct"
        return render_template("error.html",errorMessage = errorMessage)
    elif message == "empty":
        errorMessage = "Please enter username and password"
        return render_template("error.html",errorMessage = errorMessage)
        

@app.route("/signout", methods=['GET'])
def signout():
    session.pop("username",None)    
    return redirect(url_for("index"))


@app.route("/square/<int:Number>", methods=['GET','POST'])
def square_dynamic(Number):
    if Number >0 :
        return render_template("square.html")
    else:
        return redirect(url_for("index"))

if __name__=="__main__":
    app.run(port=3000)