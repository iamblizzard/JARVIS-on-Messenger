# -*- coding: utf-8 -*-

import requests
import json
import facebook

url = 'http://localhost:5000/webhook/'
payload = {'key1': 'value1', 'key2': 'value2'}

query = {'hub.verify_token': 'nipun', 'hub.challenge': 'yoyo'}

#r = requests.get(url, params=query)
#r = requests.get("https://graph.facebook.com/v2.6/me?fields=first_name&access_token=EAACEdEose0cBAOkUpVZC4ojeh2iYu4yjP3xYN0kWWZB81pAtt22mpmUEJMh0Tj0ty94PSZCuH4bIUUEwB500GsEJ9sNhW3I2GTrSI0ZBrSDdSZBZBzZAQE4iGjFoOr0OVDDYAa8tGCYvyGLfJabvmZB5OzOZATvDOEcRZA0uKV783n1GJ0eqq5QCgQBZCcwLEb4WMl9uLztBHj01AZDZD")

#print r.json()['id']


payload = {
                    'recipient': {
                        'id': '296803227486360'
                    },
                    "message": {
    					"text": "hello, world!"
  						}
                }

graph = facebook.GraphAPI('EAACEdEose0cBAGvvhfZCf6ogiLRUKt1WLB1XJldOuis1K1T3cqx4PpC6NOA5XxzCCZASRVyby5wZCzmg5ZBMHLDSGxcmDV7IUSrNtJZBqwyL8DZACij81TcTfDuFaFEwTjnBYit7QPb54ck5HB6U5yjbIn8JJs7sAGLOIZBoQEnFdVVZBAFgVZAA4jIJogpgGwfRNtonZCPimLbwZDZD')

#graph.put_object(parent_object='me', connection_name='feed',
 #                 message='Hello, world')

emoji = '😄'.decode('utf-8')

data = {
  "entry":[
    {
      "id":"296803227486360",
      "time":1458692752478,
      "messaging":[
        {
          "sender":{
            "id":"1501992990117759"
          },
          "recipient":{
            "id":"296803227486360"
          },
          "message": {

          		"text": 'yoyo'
    			"attachment":{
      						"type":"video",
      							"payload":{
        							"url":"/home/rock19/Desktop/new/VID_20170928_011356.mp4" 
      									}
    								}
  						}
  		  }
          
 
      ]
    }
  ]
}


r = requests.post('http://localhost:5000/webhook/', 
	data=json.dumps(data), headers = {'content-type':'application/json'})


#r = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=EAAb0lnhRQZCwBAJCIQxCbzl5brnOtsRyCtQtsJtuGStZBOk2seGhVvnfysQZALGIO1OZAZCY0Pi71x9TkeqniicmAmkEQtHcWpgbiynqBqXwZCLOS7cPVRxlcOcHxlORgcBZCDY8OzOcZAZBtXG9ipZAGxlMCYukLYFiet0LAVZC2jwVgZDZD', 
	
#	data=json.dumps(payload), headers = {'content-type':'application/json'})



print r.text
