from flask import Flask,render_template, request 
import numpy as np
import pickle
from markupsafe import escape
app = Flask(__name__)
model = pickle.load(open('data.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
            year = float(request.form['year'])
            emp_length_int = int(request.form['emp_length_int'])
            home_ownership_cat = request.form['home_ownership_cat']
            annual_inc = int(request.form['annual_inc'])
            income_cat = request.form['income_cat']
            loan_amount = int(request.form['loan_amount'])
            term_cat = request.form['term_cat']
            application_type_cat = request.form['application_type_cat']
            purpose_cat = request.form['purpose_cat']
            interest_payment_cat = request.form['interest_payment_cat']
            interest_rate = float(request.form['interest_rate'])
            grade_cat = request.form['grade_cat']
            dti = float(request.form['dti'])
            total_pymnt = float(request.form['total_pymnt'])
            total_rec_prncp = float(request.form['total_rec_prncp'])
            recoveries = float(request.form['recoveries'])
            installment = float(request.form['installment'])
            
              # Prepare the data for prediction
            data = np.array([year, emp_length_int, home_ownership_cat, annual_inc, income_cat, loan_amount, term_cat, application_type_cat, purpose_cat, interest_payment_cat,interest_rate, grade_cat, dti, total_pymnt, total_rec_prncp, recoveries, installment])

            # Make the prediction using the model
            prediction = model.predict([data])
 
            
            if(prediction== 0 ):
                prediction="GOOD LOAN"
            else:
                prediction="BAD LOAN"
                
            return render_template("prediction.html", prediction_text="your loan is {}".format(prediction))    
    else:
      return render_template("prediction.html")
  
  
   
     
if __name__ == "__main__":
    app.run(debug = True)