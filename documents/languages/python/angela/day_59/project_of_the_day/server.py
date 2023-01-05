from flask import Flask, render_template
import requests 

app = Flask(__name__)

response = requests.get("https://api.npoint.io/d9fb8e234a2738238e84")
api_data = response.json()
titles, subtitles, bodies = [api_data[i]["title"] for i in range(3)], [api_data[i]["subtitle"] for i in range(3)], [api_data[i]["body"] for i in range(3)]


@app.route("/")
def home():
    return render_template("index.html", titles=titles, subtitles=subtitles, bodies=bodies)

@app.route("/index.html")
def home_again():
    return render_template("index.html", titles=titles, subtitles=subtitles, bodies=bodies)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def content():
    return render_template("contact.html")

@app.route("/post/<int:number>")
def post_number(number):
    if number == 1:
        return render_template("post.html", n=1, titles=titles, subtitles=subtitles, bodies=bodies)
    elif number == 2:
        return render_template("post.html", n=2, titles=titles, subtitles=subtitles, bodies=bodies)
    elif number == 3:
        return render_template("post.html", n=3, titles=titles, subtitles=subtitles, bodies=bodies)


if __name__ == "__main__":
    app.run(debug=True)
