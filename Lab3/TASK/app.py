from flask import Flask,render_template,request
import joblib

app=Flask(__name__)
model=joblib.load("news_model.joblib")
@app.route("/",methods=["GET","POST"])

def home():
    prediction=""
    if request.method=="POST":
        text=request.form["news"]
        prediction=model.predict([text])[0]
    return render_template(
        "index.html",
        prediction=prediction
    )

app.run(debug=True)