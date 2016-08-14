from __future__ import print_function
# from flask import request

import boto3
#import flask
import json
#import request
import sys
import urllib

print('Loading function')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    # print("value1 = " + event['key1'])
    # print("value2 = " + event['key2'])
    # print("value3 = " + event['key3'])
    # return event['key1']  # Echo back the first key value
    # raise Exception('Something went wrong')

    # print(event);
    # print(context);
    # print(request);

	# print('{"wtf":"srs"}');
	data = {}
	data['event'] = event
	# data['context'] = context

	# json_data = json.dumps(data)
	# print('Content-type: text/html\n\n')
	# print('Content-type: application/json\n\n')
	# print(json_data)
	# return json_data

	return data