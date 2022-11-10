from flask import Flask,request
app=Flask(__name__)
@app.route("/")
def home():
	return "hello"

@app.route("/user/signup")
def signup():
	return "signup"

@app.route("/user/signin")
def signin():
	if(request.method=='POST'):
		req=request.get_json()
		username=req['username']
		password=req['password']
		check_user=User.query.filter_by(username=username).first()
		
	return "signin"


@app.route("/user/signout")
def signout():
	return "signout"
if "__main__"==__name__:
	app.run(host="127.0.0.1",port="5000",debug=True)
