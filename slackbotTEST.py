# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:54:02 2017

@author: jonathan
"""
import os
from slackclient import SlackClient

slack_token = os.environ['SLACK_TOKEN']

sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#thedoor",
  text="Hello from Python! :tada:"
)

