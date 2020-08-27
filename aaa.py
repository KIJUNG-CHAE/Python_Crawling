from flask import Flask, render_template, url_for
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection.crawling_db
db.cse_collection.find({})

app = Flask(__name__)
 
@app.route('/', methods=['GET','POST'])
def Scrapping_notices():
    pusanits = db.ind_collection.find({})
    notices = db.cse_collection.find({})
    emps = db.emp_collection.find({})
    smt_notices = db.smt_collection.find({})
    return render_template('bbb.html', scp_notices=notices, scp_pusanits=pusanits, scp_emps=emps, scp_smts=smt_notices)

if __name__ == '__main__':
    app.run()
