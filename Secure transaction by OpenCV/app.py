from flask import Flask , render_template, request

def check(findex):
	import requests
	headers={}
	fi=str(findex)
	s="i("+fi+").jpg"
	with open(s, 'rb') as f:
	   headers['Ocp-Apim-Subscription-Key'] = 'c8bfa0f50ea84389bdd8da8007e13079'
	   headers['Content-Type'] = 'application/octet-stream'
	   req = requests.post('https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize', headers=headers, data=f)
	return req.json()

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print "here res"
      print request
      
      # check happy : 1
      check1=check(1)[0]["scores"]["happiness"]
      print check1

      # check neutral : 2
      check2=check(2)[0]["scores"]["neutral"]
      print check2

      # check angry : 3
      check3=check(3)[0]["scores"]["anger"]
      print check3

      flag={}
      flag["y"]=0
      if(check1>=0.6 and check2>=0.6 and check3>=0.6):
      	flag["y"]=1
      return render_template("result.html", result = flag)

if __name__ == "__main__":
    app.run(debug = True)