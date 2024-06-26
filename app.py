from flask import Flask,render_template,request
import pickle
import numpy as np
app= Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method=='POST':


        Gend=request.form['Gender']
        if Gend=="Male":
            Gender=1
        elif Gend=="Female":
            Gender=0

        Age=int(request.form['Age'])
        EstimatedSalary=int(request.form['EstimatedSalary'])
      
        newdata=np.array([[Gender,Age,EstimatedSalary]])

        model=pickle.load(open('model.pkl','rb'))
        Purchased = model.predict(newdata)
        

        
        
        return render_template('prediction.html',Purchased[0])


if __name__=='__main__':
    app.run()
