from flask import Flask, render_template, current_app as current_app

app=Flask(__name__)

@app.route('/dynamic')
def dynamic():
	
	greeting="Team Edge is in the house!"
	
	return render_template('dynamic.html', greeting=greeting)

if __name__=='__main__':
        app.run(debug=True,host='0.0.0.0')