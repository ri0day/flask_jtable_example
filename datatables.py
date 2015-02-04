from flask import Flask ,render_template,request,jsonify
import sqlite3
app = Flask(__name__)
db_file = '/Users/min/Downloads/DataTables-1.10.4-trial/hostdb.db'
db = sqlite3.connect(db_file,check_same_thread = False)
db.row_factory = sqlite3.Row
cu = db.cursor()

def generate_output(modify_sql,output_sql):
	cu.execute(modify_sql)
	db.commit()
	cu.execute(output_sql)
	result = cu.fetchall()
	final_result =[]
	for r in result:
		final_result.append(dict(zip(r.keys(),r)))
	d={}
	d['draw'] = 2
	d['recordsTotal'] = 1 
	d["recordsFiltered"] = 1
	d['data'] = final_result
	return jsonify(d)


@app.route('/dt2',methods=['GET', 'POST'])
def dt2():
	if request.method == "GET":
		sql_text = "select * from hostinfov2"
		cu.execute(sql_text)
		result = cu.fetchall()
		recordsTotal = len(result)
		recordsFiltered = recordsTotal
		final_result =[]
		for r in result:
			final_result.append(dict(zip(r.keys(),r)))
		d={}
		d['draw'] = 2
		d['recordsTotal'] = recordsTotal 
		d["recordsFiltered"] = recordsFiltered
		d['data'] = final_result
		return jsonify(d)
		
	elif request.method == "POST": 
		hostname = request.form.get('data[hostname]','Null')
		ip = request.form.get('data[ip]','Null')
		location = request.form.get('data[location]','Null')
		tags = request.form.get('data[tags]','Null')
		hwinfo = request.form.get('data[hwinfo]','Null')
		sn = request.form.get('data[sn]','Null')
		 
		if request.form.get('action') == "edit":
			rowid = int(request.form.get('id','1'))
			update_row_sql_text = "update  hostinfov2 set hostname='%s', ip='%s', location='%s', tags='%s', hwinfo='%s', sn='%s' where DT_RowId = %d"%\
			(hostname,ip,location,tags,hwinfo,sn,rowid)
			return_data_sql_text="select * from hostinfov2 where DT_RowId =%d"%(rowid)
			print "update_sql: %s"%(update_row_sql_text)
			return generate_output(update_row_sql_text,return_data_sql_text)

		elif request.form.get('action') == "create":
			cu.execute('select max(DT_RowId) from hostinfov2')
			max_from_db = int(cu.fetchone()[0])
			insert_number = max_from_db + 1
			add_row_sql_text = "insert into hostinfov2 values (%d ,'%s','%s','%s','%s','%s','%s')"%\
			(insert_number,hostname,ip,location,tags,hwinfo,sn)
			print add_row_sql_text
			return_data_sql_text="select * from hostinfov2 where DT_RowId =%d"%(insert_number)
			return generate_output(add_row_sql_text,return_data_sql_text)

		elif request.form.get('action') == "remove":
			rowid = int(request.form.get('id[]'))
			delete_row_sql = 'delete from hostinfov2 where DT_RowId = %d'%(rowid)
			print delete_row_sql
			cu.execute(delete_row_sql)
			db.commit()
			return '[]'
	else:
		return '''Don't be foo ,bro '''


@app.route('/simple2.html')
def show2():
	return render_template('simple2.html')
app.run(debug=True,host = '0.0.0.0' ,port =80)
