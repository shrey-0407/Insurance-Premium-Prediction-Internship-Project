from flask import Flask

import sys
from insurance.logger import logging
from insurance.exception import InsuranceException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        insurance = InsuranceException(e,sys)
        logging.info(insurance.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."

if __name__=="__main__":    
    app.run()