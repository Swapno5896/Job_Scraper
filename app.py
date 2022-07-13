from flask import Flask,request, render_template
from flask_cors import CORS, cross_origin
import requests
from html_read import scrap
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
@cross_origin()
def homePage():
        return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
@cross_origin()
def result():
    if request.method == 'POST':
        Skill = request.form['skill']
        location = request.form['location']
        workExp = request.form['workExp']
        unFamilarSkill = request.form['unFamilarSkill']
        # print(Skill,location,workExp)
        inputData = scrap(Skill,location,workExp,unFamilarSkill)
        print(inputData)

    return render_template('result.html', inputData=inputData)
if __name__ =='__main__':
    app.run()