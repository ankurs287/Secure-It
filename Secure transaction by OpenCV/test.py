########### Python 2.7 #############
import httplib, urllib, base64, os, json

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'c8bfa0f50ea84389bdd8da8007e13079',
}

params = urllib.urlencode({
})

# features_used:
# 1. anger
# 2. happiness
# 3. neutral
# 4. surprise
# 5. fear (not implemented yet)

# generate 4 random numbers
from random import randint
f1=randint(1, 4)
f2=randint(1, 4)
f3=randint(1, 4)
f4=randint(1, 4)
print(f1, f2, f3, f4)


for i in range(1):
    # Replace the example URL below with the URL of the image you want to analyze.
    # http://images.clipartpanda.com/happy-man-images-A-Happy-Man.jpg
    # s="opencv1.png"

    body = "{ 'url': 'https://lh6.googleusercontent.com/HRJ1A0oe9HFVAU5QGCgYtLHbRIKPfmBHMBQY7GrW245odJL1i9G36DcluvxkXm7WDK0ABDvk=w1366-h646-rw' }"

    try:
        # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
        #   URL below with "westcentralus".
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

# happy image: https://i.imgur.com/WjfkjdS.jpg


