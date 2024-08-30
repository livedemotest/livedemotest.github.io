from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.route("/")
def index_get():
    return render_template("index.html")

@app.route("/about")
def about_get():
    return render_template("about.html")

@app.route("/contact")
def contact_get():
    return render_template("contact.html")

@app.route("/portfolio")
def portfolio_get():
    return render_template("portfolio.html")

@app.route("/blog-details")
def blog_details_get():
    return render_template("blog-details.html")

@app.route("/resume")
def resume_get():
    return render_template("resume.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
