import json
import os
import random
import sys
import pprint
import dry_eye
import audioModule
import councillor
from unidecode import unidecode

import requests
from flask import Flask, request

import config
import modules
import emoticons

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', config.VERIFY_TOKEN)

app = Flask(__name__)

@app.route('/')
def about():
	return 'Just A Rather Very Intelligent System, now on Messenger!'


@app.route('/video/')
def video():
	return dry_eye.main("/home/rock19/Desktop/new/VID_20170928_011356.mp4")
	
@app.route('/audio/')
def audio():
	return audioModule.main("amy.wav")
	
@app.route('/process/')
def process():
	return json.dumps(modules.process_query(request.args.get('q')))


@app.route('/search/')
def search():
	return json.dumps(modules.search(request.args.get('q')))


@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
	if request.method == 'POST':

		data = request.get_json(force=True)
		
		messaging_events = data['entry'][0]['messaging']
		for event in messaging_events:
			sender = event['sender']['id']
			message = None
			
			if 'message' in event and 'text' in event['message']:

				if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
					quick_reply_payload = event['message']['quick_reply']['payload']
					message = modules.search(quick_reply_payload, sender=sender, postback=True)
				
				else:
					text = event['message']['text']

					if(text.encode('unicode-escape') in emoticons.__all__):
				
						x = text.encode('unicode-escape')
						data = emoticons.process(x[2:])

						if data['success']:
							message = json.dumps(data['output'])[10:-2]

							if(x in ['\U0001f620', '\U0002f639', '\U0001f61f', '\U0001f61e']):
								message += '\nYou seem sad, Do you want to take our anonymous depression detection test?'


					else:
						message = modules.search(text, sender=sender)
			
			#modules
			if 'message' in event and 'attachment' in event['message']:

				if 'type' in event['message']['attachment']:

					#video
					if event['message']['attachment']['type'] == 'video':

						if 'payload' in event['message']['attachment'] and 'url' in event['message']['attachment']['payload']:
							message = dry_eye.main(event['message']['attachment']['payload']['url'])

					#audio
					elif event['message']['attachment']['type'] == 'audio':
						message = audioModule.main(event['message']['attachment']['payload']['url'])			
			

			if 'postback' in event and 'payload' in event['postback']:
				postback_payload = event['postback']['payload']
				message = modules.search(postback_payload, sender=sender, postback=True)
			
			if message is not None:
				payload = {
					'recipient': {
						'id': sender
					},
					'message': message
				}

				r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
				                  json=payload)
				
		return ''  # 200 OK

	elif request.method == 'GET':  # Verification
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		else:
			return 'Error, wrong validation token'


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
