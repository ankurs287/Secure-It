import requests
headers={}
with open('one.jpg', 'rb') as f:
   headers['Ocp-Apim-Subscription-Key'] = 'c8bfa0f50ea84389bdd8da8007e13079'
   headers['Content-Type'] = 'application/octet-stream'
   req = requests.post('https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize', headers=headers, data=f)
print req.json()[0]["scores"]["happiness"]