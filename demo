from flask import Flask, jsonify, request 
import csv
import re
app = Flask(__name__)

@app.route('/comp')

def comp():
	num1=request.args.get('num1')
	num2=request.args.get('num2')

	if num1 == num2:
		return jsonify({'data': "Exact Match - YES"})

	else:
		num1=num1.replace(" ","")
		num2=num2.replace(" ","")
		ind= "(\+)?(0|91)?[7-9][0-9]{9}"
		aus="((\+61|61|061)?(02|03|04|07|08)[0-9]{8})|((\+61|61|061)?(2|3|4|7|8)[0-9]{8})"

		ind_n1 = re.match(ind,num1)
		ind_n2 = re.match(ind,num2)
		aus_n1 = re.match(aus,num1)
		aus_n2 = re.match(aus,num2)

		if ind_n1 and ind_n2:
			if num1 == num2:
				return jsonify({'data': "Intelligent Match - YES"})
			elif num1 != num2:
				if (num1[::-1][:10]==num2[::-1][:10]): #indian mobile numbers
					return jsonify({'data': "Intelligent Match - YES"})
				else:
					return jsonify({'data': "NO"})
			else:
				return jsonify({'data': "NO"})

		elif aus_n1 and aus_n2:
			if num1 == num2:
				return jsonify({'data': "Intelligent Match - YES"})
			elif num1 != num2:
				if (num1[::-1][:8]==num2[::-1][:8]):
					return jsonify({'data': "Intelligent Match - YES"})
				else:
					return jsonify({'data': "NO"})
			else:
				return jsonify({'data': "NO"})
    
		else:
			return jsonify({'data': "NO"})
if __name__ == '__main__': 
    app.run(debug = True)