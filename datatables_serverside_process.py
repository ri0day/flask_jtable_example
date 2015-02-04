from flask import Flask ,render_template,request,jsonify
import sqlite3
app = Flask(__name__)
db_file = '/Users/min/Downloads/DataTables-1.10.4-trial/hostdb.db'
db = sqlite3.connect(db_file,check_same_thread = False)
#db.row_factory = sqlite3.Row
cu = db.cursor()


def generate_ouput(sql_text,draw,is_first_page):
	cu.execute('select count(ip) from hostinfov2')
	recordsTotal = cu.fetchone()[0]
	cu.execute(sql_text)
	result = cu.fetchall()
	recordsFiltered = len(result)
	if is_first_page is True:
		result = result[:10]
	d={}
	d['draw'] = draw
	d['recordsTotal'] = recordsTotal 
	d["recordsFiltered"] = recordsFiltered
	d['data'] = result
	return jsonify(d)
	
@app.route('/dt')
def dts():
	draw = request.args.get('draw')
	offset = request.args.get('start')
	limit = request.args.get('length')
	search_text = request.args.get('search[value]')
	if not search_text and offset != '0':
		sql_text = "select hostname,ip,location,tags,hwinfo,sn from hostinfov2 limit %s offset %s"%(limit,offset) 
		return generate_ouput(sql_text,draw,is_first_page=False)

	elif search_text:
		sql_text = "select hostname,ip,location,tags,hwinfo,sn from hostinfov2 where hostinfov2 match '%s*'"%(search_text) 
		return generate_ouput(sql_text,draw,is_first_page=False)
	else:
		sql_text = "select hostname,ip,location,tags,hwinfo,sn from hostinfov2"
		return generate_ouput(sql_text,draw,is_first_page=True)

@app.route('/simple.html')
def show():
	return render_template('simple.html')

app.run(debug=True,host = '0.0.0.0' ,port =80)
