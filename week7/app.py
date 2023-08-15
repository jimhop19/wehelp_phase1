from flask import Flask, render_template,request, redirect, url_for, session
app=Flask(__name__)
app.secret_key="secret"
import mysql.connector
mydb = mysql.connector.pooling.MySQLConnectionPool(
    host="127.0.0.1",
    username="root",
    password="12345678",    
    db='website'
)

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
    mydbConnection = mydb.get_connection()
    cursor = mydbConnection.cursor()  
    cursor.execute("INSERT INTO member(name, username, password) VALUES(%s,%s,%s);",(signup_name,signup_username,signup_password))
    mydbConnection.commit()
    mydbConnection.close()
    

mydbConnection = mydb.get_connection()
cursor = mydbConnection.cursor()
cursor.execute("SELECT username From member")
usernameList = cursor.fetchall()
mydbConnection.close()


def check_username_in_list(username, usernameList):        
    for item in usernameList:
        if username == item[0]:
            return True
    return False


@app.route("/signin", methods=['POST'])
def signin():
    username = request.form["username"]
    password = request.form["password"] 
    mydbConnection = mydb.get_connection()
    cursor = mydbConnection.cursor()   
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
    mydbConnection.close()
    
   
            
@app.route("/member")
def member():           
    mydbConnection = mydb.get_connection()
    cursor = mydbConnection.cursor()    
    cursor.execute("SELECT member.name,content,message.id FROM message LEFT JOIN member ON message.member_id = member.id ",None)
    messageBoard = cursor.fetchall()
    messageJson = []
    for x in range(len(messageBoard)):
        curlyBrace = {}
        curlyBrace["name"] = messageBoard[x][0]
        curlyBrace["content"] = messageBoard[x][1]
        curlyBrace["id"] = messageBoard[x][2]
        messageJson.append(curlyBrace)
    mydbConnection.close()        
    
    if "username" not in session:
        return redirect(url_for("index"))
    else:          
        return render_template("member.html",name = session["name"],messageToJS = messageJson)
    
@app.route("/api/member", methods=['GET','PATCH'])
def apiMember():
    if request.method == "GET":            
        username = request.args.get("username")    
        mydbConnection = mydb.get_connection()
        cursor = mydbConnection.cursor()
        cursor.execute("SELECT username From member")
        usernameList = cursor.fetchall()
        mydbConnection.close()
        if check_username_in_list(username,usernameList):
            mydbConnection = mydb.get_connection()
            cursor = mydbConnection.cursor()
            cursor.execute("SELECT id, name , username FROM member WHERE username = %s", (username,))    
            searchResult = cursor.fetchall()
            mydbConnection.close()
            searchResultJson = {}
            searchResultJson["id"]= searchResult[0][0]
            searchResultJson["name"] = searchResult[0][1]
            searchResultJson["username"] = searchResult[0][2]
            jsonToJS = {}
            jsonToJS["data"] = searchResultJson
        else:
            jsonToJS = {}
            jsonToJS["data"] = None        
        return (jsonToJS)
    
    if request.method == "PATCH":
        newName = request.get_json()
        currentUsername = session["username"]        

        try:
            mydbConnection = mydb.get_connection()
            cursor = mydbConnection.cursor()
            cursor.execute("UPDATE member SET name = %s WHERE username = %s",(newName["name"],currentUsername))
            mydbConnection.commit()
            session["name"] = newName["name"]               
            return {"ok":True}
        except:
            return {"error":True}
        finally:
            mydbConnection.close()
    
        
    
    
@app.route("/createMessage", methods=['POST'])
def createMessage():
    leaveMessage = request.form["leaveMessage"]
    memberId = session["member_id"]    
    mydbConnection = mydb.get_connection()
    cursor = mydbConnection.cursor()  
    cursor.execute("INSERT INTO message(member_id, content) VALUES(%s, %s);",(memberId,leaveMessage))
    mydbConnection.commit()    
    mydbConnection.close()
    
    return redirect("/member")
    

@app.route("/deleteMessage", methods = ["POST"])
def deleteMessage():
    messageId = request.get_json("/deleteMessage")["id"]  
    mydbConnection = mydb.get_connection()
    cursor = mydbConnection.cursor()    
    cursor.execute("DELETE FROM message WHERE id = %(id)s ", {"id":messageId})
    mydbConnection.commit()
    mydbConnection.close()
    
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
    return redirect("/")




if __name__=="__main__":
    app.run(port=3000)
       