
from flask_app import app
app.config['SECRET_KEY'] = "Portfolio_website"

if __name__ == "__main__":
    app.run(debug=False, port=8060)