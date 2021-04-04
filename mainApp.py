from flask import Flask, jsonify, request, make_response, render_template
import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

app = Flask(__name__)

logisticModel = joblib.load("modelWeights/CompleteTextLogistics.sav")
mnbModel = joblib.load("modelWeights/CompleteTextMultinomialNB.sav")
pol = SentimentIntensityAnalyzer()


# ----------- Image for Prediction -------------------------------------
picFolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = picFolder
predictionPics = [
    os.path.join(app.config['UPLOAD_FOLDER'], 'GreenTick.png'),
    os.path.join(app.config['UPLOAD_FOLDER'], 'redCross.png')
]

# ----------------------------  Reading Weights ----------------------------------


def RealOrFake(title=None, article=None):
    return (mnbModel.predict(title+article)[0], logisticModel.predict(title+article)[0])


# ----------------------------  Polarity of News ----------------------------------
def PolarityCount(title, article):
    p = pol.polarity_scores(title)
    art = pol.polarity_scores(article)
    title = {
        'Task': 'Polarity of News',
        'Positive': p['pos'],
        'Negative': p['neg'],
        'Neutral': p['neu'],
    }
    article = {
        'Task': 'Polarity of News',
        'Positive': art['pos'],
        'Negative': art['neg'],
        'Neutral': art['neu']
    }

    return (title, article)


# ----------------------------  Home Page ----------------------------------
@app.route("/")
def homePage():
    return render_template('index.html')

# ----------------------------  Prediction Page ----------------------------------


@app.route("/verify", methods=["POST"])
def verify():
    try:
        if request.method == 'POST':
            title = [str(request.form['title'])]
            article = [str(request.form['article'])]

    except(Exception)as e:
        return ""+str(e)
    else:
        output = RealOrFake(title, article)
        out = []
        if(output[0] == 1):
            out.append(predictionPics[0])
        else:
            out.append(predictionPics[1])
        
        if(output[1] == 1):
            out.append(predictionPics[0])
        else:
            out.append(predictionPics[1])


        data = PolarityCount(title, article)
        return render_template('prediction.html', titlePolarity=data[0], articlePolarity=data[1], output=out)


# --------------------------------- JSON PREDICTION -------------------------
@app.route("/json", methods=['GET', 'POST'])
def jsonFile():
    if(request.is_json):
        req = request.get_json()
        title = [str(req.get("title"))]
        article = [str(req.get("article"))]

        if(req != None):
            response = {
                "prediction": " "+RealOrFake(title, article)
            }
            return make_response(jsonify(response), 200)
        else:
            response = {
                "prediction": "Please Write something"
            }
            return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify({"prediction": "No Json Received"}), 400)


if __name__ == "__main__":
    app.run(debug=True)
