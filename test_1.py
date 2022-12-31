from flask_sqlalchemy import SQLAlchemy
from flask import Flask


# https://www.golinuxcloud.com/flask-sqlalchemy/

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
app.config["SQLALCHEMMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Form(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

@app.route("/")
def main():
    #teams = Form.query.all()

    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)