from flask import Flask
app=Flask(__name__)
@app.route("/user/sig")
def signin():
	username="Udrasht"
	password="123"
	payload={
	"username":username,
	"password":password
	}

	resp=requests.post("http://127.0.0.1:5000/user/signin",json=payload).content.decode()
	print(resp)