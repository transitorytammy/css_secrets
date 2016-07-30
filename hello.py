from flask import Flask, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'chefology'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('name')
    origin = request.args.get('origin')
    bio = request.args.get('bio')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from chef where name = '" + username +"'")

    data = cursor.fetchone()
    if data is None:
        return "No chef found"
    else:
        return "Chef found " + username

if __name__ == "__main__":
    app.run()
