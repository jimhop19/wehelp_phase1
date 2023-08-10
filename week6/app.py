from flask import Flask, render_template,request, redirect, url_for, session
app=Flask(__name__)
app.secret_key="secret"
import mysql.connector
mydb = mysql.connector.connect(
    host="127.0.0.1",
    username="root",
    password="12345678",    
    db='website'
)
cursor = mydb.cursor()
import json



@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("member"))
    else:
        return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    signup_name = request.form["signup_name"]
    signup_username = request.form["signup_username"]
    signup_password = request.form["signup_password"]
    if check_username_in_list(signup_username,usernameList) == False:
        signup_to_database(signup_name,signup_username,signup_password)
        return redirect("/")
    else:
        return redirect("/error?message=samename")

def signup_to_database(signup_name,signup_username,signup_password):    
    cursor.execute("INSERT INTO member(name, username, password) VALUES(%s,%s,%s);",(signup_name,signup_username,signup_password))
    mydb.commit()


cursor.execute("SELECT username From member")
usernameList = cursor.fetchall()
def check_username_in_list(username, usernameList):        
    for item in usernameList:
        if username == item[0]:
            return True
    return False


@app.route("/signin", methods=['POST'])
def signin():
    username = request.form["username"]
    password = request.form["password"]    
    cursor.execute("SELECT username From member")
    usernameList = cursor.fetchall()
    if username != "" and password != "":
        if check_username_in_list(username,usernameList) == True:
            cursor.execute("SELECT * FROM member WHERE username = %(username)s", {"username" : username})
            profile_in_database = cursor.fetchall()
            if username == profile_in_database[0][2] and password == profile_in_database[0][3]:       
                session["username"] = username
                session["name"] = profile_in_database[0][1]
                session["member_id"] = profile_in_database[0][0]           
                return redirect(url_for("member"))
            else:
                return redirect("/error?message=invalid")
        else :
            return redirect("/error?message=invalid")    
         
    elif username == "" or password == "":
        return redirect("/error?message=empty")
   
            
@app.route("/member")
def member():    
    cursor.execute("SELECT member.name,content FROM message LEFT JOIN member ON message.member_id = member.id ",None)
    messageBoard = cursor.fetchall()
    messageJson = []
    for x in range(len(messageBoard)):
        curlyBrace = {}
        curlyBrace[messageBoard[x][0]] = messageBoard[x][1]
        messageJson.append(curlyBrace)    
    
    
    if "username" not in session:
        return redirect(url_for("index"))
    else:          
        return render_template("member.html",name = session["name"],messageToJS = messageJson)
    
@app.route("/createMessage", methods=['POST'])
def createMessage():
    leaveMessage = request.form["leaveMessage"]
    memberId = session["member_id"]    
    cursor.execute("INSERT INTO message(member_id, content) VALUES(%s, %s);",(memberId,leaveMessage))
    mydb.commit()
    return redirect("/member")

@app.route("/error", methods=['GET','POST'])
def error():
    message = request.args.get("message")
    if message == "invalid":
        errorMessage = "Username or password is not correct"
        return render_template("error.html",errorMessage = errorMessage)
    elif message == "empty":
        errorMessage = "Please enter username and password"
        return render_template("error.html",errorMessage = errorMessage)
    elif message == "samename":
        errorMessage = "Username is already in use"
        return render_template("error.html",errorMessage = errorMessage)
        

@app.route("/signout", methods=['GET'])
def signout():
    session.pop("username",None) 
    session.pop("name",None)
    session.pop("member_id",None)   
    return redirect(url_for("index"))




if __name__=="__main__":
    app.run(port=3000)