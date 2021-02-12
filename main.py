from wsgiref import simple_server
from flask import Flask, request, render_template
#import pickle
#import json
#import numpy as np
"""
*****************************************************************************
*
* filename:       main.py
* version:        1.0
* author:         HARISH
* creation date:  12-feb-2021
*
* change history:
*
* who             when           version  change (include bug# if apply)
* ----------      -----------    -------  ------------------------------
* HARISH          12-Feb-2021    1.0      initial creation
*
*
* description:    flask main file to run application
*
****************************************************************************
"""

app = Flask(__name__)

def get_predict_number(one, two, three, four, five, six, seven, eight, nine, ten):

    """
    * method: get_predict_profit
    * description: method to predict the results
    * return: prediction result
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * HARISH          12-FEB-2021    1.0      initial creation
    *
    * Parameters
    *
    """

    if int(one) == 5 and int(two) == 10 and int(three) == 15 and int(four) == 20 and int(five) == 25 and int(six) == 30 and int(seven) == 35 and int(eight) == 40 and int(nine) == 45 and int(ten) == 50:
        str1 = 0
    else:
        str1 = 1


    return str1


@app.route('/')
def index_page():
    """
    * method: index_page
    * description: method to call index html page
    * return: index.html
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * HARISH          23-JAN-2021    1.0      initial creation
    *
    * Parameters
    *   None
    """
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """
    * method: predict
    * description: method to predict
    * return: index.html
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * HARISH          20-JAN-2021    1.0      initial creation
    *
    * Parameters
    *   None
    """
    if request.method == 'POST':
        one = request.form['5 X 1 = ']
        two = request.form["5 X 2 = "]
        three = request.form["5 X 3 = "]
        four = request.form["5 X 4 = "]
        five = request.form["5 X 5 = "]

        six = request.form['5 X 6 = ']
        seven = request.form["5 X 7 = "]
        eight = request.form["5 X 8 = "]
        nine = request.form["5 X 9 = "]
        ten = request.form["5 X 10 = "]

        output = get_predict_number(one, two, three, four, five, six, seven, eight, nine, ten)
        #return render_template('index.html',show_hidden=True, prediction_text='This Project is done by Harish Musti and temparature must be  {}'.format(output))
        return render_template('result.html', prediction=output)

if __name__ == "__main__":
    #app.run(debug=True)
    host = '0.0.0.0'
    port = 5030
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
