from flask import Flask, render_template, url_for
from CSE_Notice import save_cse_db 
from INFO_IND import save_ind_db
from EMP import save_emp_db

save_cse_db()
save_emp_db()
save_ind_db()