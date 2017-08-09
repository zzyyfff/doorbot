# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:54:02 2017

@author: jonathan
"""
import os
from flask import Flask, request, Response
from slackclient import SlackClient
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)
 
app = Flask(__name__)
slack_client = SlackClient(os.environ.get('SLACK_TOKEN', None))
twilio_client = Client()

@app.route('/twilio', methods=['POST'])
def twilio_post():
    response = MessagingResponse()
    message = request.form['Body']
    slack_client.api_call("chat.postMessage", channel="#thedoor",
                          text=message, username='doorbot',
                          icon_emoji=':robot_face:')
#    message="Recieved!"
#    response.message(message)
    return str(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

