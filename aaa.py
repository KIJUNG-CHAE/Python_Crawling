from flask import Flask, render_template, url_for
from CSE_Notice import get_notices
from INFO_IND import get_busanits
from EMP import get_emps
# from STU_Notice import get_stu_notices

app = Flask(__name__)
 
@app.route('/', methods=['GET','POST'])
def Scrapping_notices():
    pusanits = get_busanits()
    notices = get_notices()
    emps = get_emps()
    # stu_notices = get_stu_notices()
    return render_template('bbb.html', scp_notices=notices, scp_pusanits=pusanits, scp_emps=emps) # scp_stu_notices = stu_notices

if __name__ == '__main__':
    app.run()
