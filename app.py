import smtplib
from flask import Flask , render_template ,request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index')
def index_index():
	return render_template('index.html')

@app.route('/sql-services')
def sql_services():
	return render_template('sql-services.html')

@app.route('/nosql-services')
def nosql_services():
	return render_template('nosql-services.html')

@app.route('/bigdata-consulting')
def bigdata_consulting():
	return render_template('bigdata-consulting.html')

@app.route('/data-analytics')
def data_analytics():
	return render_template('data-analytics.html')

@app.route('/data-architecture')
def data_architecture():
	return render_template('data-architecture.html')

@app.route('/why-gajadata')
def why_gajadata():
	return render_template('why-gajadata.html')

@app.route('/clients')
def clients():
	return render_template('clients.html')

@app.route('/careers')
def careers():
	return render_template('careers.html')


@app.route('/contact',methods=['GET'])
def contact():
	return render_template('contact.html')

@app.route('/contact',methods=['POST'])
def contact_post():
	email=request.form['email']
	name=request.form['name']
	subject=request.form['subject']
	data=request.form['data']
	sender = 'contact@gajadata.com'
	receivers = ['contact@gajadata.com']


	message = """Subject: Contact Page Enquiry

	Hi,Someone from gajdata.com contact page sent you mail:

	Name:"""+name+"""
	Email:"""+email+"""
	Subject: """+subject+"""
	Description:"""+data+"""


	Mail sent using Gajadata Python App
	"""

	try:
		s = smtplib.SMTP()
		s.connect('smtp.gmail.com',587)
		s.starttls()
		s.login('contact@gajadata.com', 'darkshadow')
		if name and email and data:
			s.sendmail(sender, receivers, message)
			return "sent"
		else:
			raise
	except:
		return "error"



@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
