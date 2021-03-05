from flask import Flask, jsonify, request 
import csv

app = Flask(__name__)

@app.route('/comp')

def comp(): 
	num1=request.args.get('num1')
	num2=request.args.get('num2')
	if num1 == num2:
		return jsonify({'data': "Exact Match - YES"})
	elif num1 != num2:
		num1=num1.replace(" ","")
		num2=num2.replace(" ","")
		if (num1[::-1][:10]==num2[::-1][:10]): #indian mobile numbers
			return jsonify({'data': "Intelligent Match - YES"})
		else:
			return jsonify({'data': "NO"})
if __name__ == '__main__': 
    app.run(debug = True)
