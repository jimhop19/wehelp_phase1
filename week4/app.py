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
            
@app.route("/member")
def member():    
    if "username" not in session:
        return redirect(url_for("index"))
    else:
        return render_template("member.html")

@app.route("/error", methods=['GET','POST'])
def error():    
    return render_template("error.html")

@app.route("/signout", methods=['GET'])
def signout():
    session.pop("username",None)    
    return redirect(url_for("index"))

# @app.route("/square", methods=['POST'])
# def square():    
#     integer = int(request.form["integer"])
#     if integer >= 0 :
#         return render_template("square.html",integer=integer)
@app.route("/square/<int:Number>", methods=['GET','POST'])
def square_dynamic(Number):
    if Number >0 :
        return render_template("square.html")
    else:
        return redirect(url_for("index"))

if __name__=="__main__":
    app.run(port=3000)