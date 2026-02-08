from flask import Flask,request,render_template,jsonify,url_for
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from src.pipelines.prediction_pipeline import prediction,customData

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def form_page():
    if (request.method == 'POST'):
        carat = float(request.form.get('carat', 0))
        cut = request.form.get('cut')
        color = request.form.get('color')
        clarity = request.form.get('clarity')
        depth = float(request.form.get('depth', 0))
        table = float(request.form.get('table', 0))
        x = float(request.form.get('x', 0))
        y = float(request.form.get('y', 0))
        z = float(request.form.get('z', 0))

        data_obj = customData(carat, cut, color, clarity, depth, table, x, y, z)
        scaled_data = data_obj.get_data_in_df()

        predicts = prediction()
        pred = predicts.predict(scaled_data)

        result = round(pred[0], 2)
        return render_template("result.html", result=result)

    else:
        return render_template('form.html')
    

    
if __name__ == "__main__":
    app.run(debug=True)

