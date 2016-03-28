import sqlite3
from flask import  Flask ,render_template,request,jsonify
from sql_helper import generate_add_host_sql,generate_update_host_sql,generate_list_host_sql,generate_delete_host_sql

db_file = 'v3.db'
db = sqlite3.connect(db_file,check_same_thread = False)
db.row_factory = sqlite3.Row
cu = db.cursor()
app = Flask(__name__)

@app.route('/jtable.html',methods=['GET'])
def show():
    return render_template('jtable.html')


@app.route('/listhost',methods=['POST'])
def lst_tab():
    total_rows = 'select count(DT_RowId) from hostinfo;'
    total_rows_number = cu.execute(total_rows).fetchall()[0][0]
    sql = generate_list_host_sql(request)
    cu.execute(sql)
    result = cu.fetchall()
    final_result =[]
    for r in result:
        final_result.append(dict(zip(r.keys(),r)))
    d={}
    d['Result'] = 'OK'
    d['Records'] = final_result
    d['TotalRecordCount'] = total_rows_number
    return jsonify(d)
     

@app.route('/deletehost',methods=['POST'])
def del_host():
    sql = generate_delete_host_sql(request)
    try:
        cu.execute(sql)
    except:
        return({"Result":"None"})
    return jsonify({"Result":"OK"})

@app.route('/createhost',methods=['POST'])
def create_host():
    d ={}
    d['Result'] = 'OK'
    d['Record'] = dict(zip(request.form.keys(),request.form.values()))
    sql = generate_add_host_sql(request)
    try:
        cu.execute(sql)
    except:
        d['Result'] = 'None'
    return jsonify(d)

@app.route('/updatehost',methods=['POST'])
def update_host():
    sql = generate_update_host_sql(request)
    try:
        cu.execute(sql)
    except:
        return jsonify({"Result":"None"})
    return jsonify({"Result":"OK"})

app.run(host='0.0.0.0',debug=True)
