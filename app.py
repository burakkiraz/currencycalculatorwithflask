from flask import Flask,render_template,request
import requests

api_key = ""
#in order to get a free api_key go to https://fixer.io/signup/free and sign up for free plan. Then, you can get an api_key for free

url = "http://data.fixer.io/api/latest?access_key="+api_key

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") 
        secondCurrency = request.form.get("secondCurrency") 

        amount = request.form.get("amount") 
        response = requests.get(url)
        infos = response.json()

        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue / firstValue) * float(amount)

        cureencyInfo = dict()
        cureencyInfo["firstCurrency"] = firstCurrency
        cureencyInfo["secondCurrency"] = secondCurrency
        cureencyInfo["amount"] = amount
        cureencyInfo["result"] = result

        return render_template("index.html",info = cureencyInfo)

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
