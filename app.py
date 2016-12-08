from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "hello it is working"

if __name__ == "__main__":
	app.run()





