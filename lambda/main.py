from __future__ import print_function
# from flask import request

import base64
import boto3
#import flask
import json
# import request
# import requests
import sys
import threading
import time
import urllib

print('Initializing K\'Thera')

# s3 = boto3.client('s3')
firehose = boto3.client('firehose')
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
	start = time.time()
	data = {}
	# data['event'] = event
	# data['context'] = context
	# data['body'] = event
	# data['body'] = event['body']
	# data['body'] = event['body'] + '\n===\n'
	# data['body'] = base64.b64decode(event['body']) + '\n===\n'
	# decoded_body = base64.b64decode(data['body'])
	# decoded_body = base64.b64decode(data['body']).decode("utf-8", "ignore")
	# data['firehose_upload_results'] = upload_to_firehose('kthera', [{'Data': 'DANKALICIOUS!!!!oneone\nSIKK NO SCOPEZ M9\n'}, {'Data': 'DA SIKKEST 720NOSCOPE!!!11oneone\n420BLAZEIT\n\n'}])
	# data['dynamodb_results'] = insert_into_dynamodb('kthera_beeswax_feed', {'request_id': {'N': '1337'}, 'json': {'S': '{"uwot": "m8??"}'}})

	data['body'] = event['body']
	data['decoded_body'] = base64.b64decode(data['body'])

	start2 = time.time()
	dynamodb_augmentor_settings = get_augmentor_settings_from_dynamodb()
	end2 = time.time()
	start3 = time.time()
	data['dynamodb_augmentor_settings'] = json.loads(dynamodb_augmentor_settings['Item']['augmentor_settings']['S'])
	end3 = time.time()

	start4 = time.time()
	# data['firehose_upload_results'] = upload_to_firehose('kthera', [{'Data': data['decoded_body']}])
	firehose_thread = threading.Thread(target = upload_to_firehose, args = ('kthera', [{'Data': data['decoded_body']}]))
	# firehose_thread.daemon = True
	firehose_thread.start()
	end4 = time.time()

	# return data['dynamodb_augmentor_settings']

	end = time.time()
	data['et'] = end - start
	data['et2'] = end2 - start2
	data['et3'] = end3 - start3
	data['et4'] = end4 - start4
	# return data['body']
	# return data['decoded_body']
	return data

def get_augmentor_settings_from_dynamodb():
	return get_from_dynamodb('kthera_beeswax_feed', 'request_id', 'N', '-1')

def get_from_dynamodb(table_name, key_name, key_type, key):
	return dynamodb.get_item(TableName = table_name, Key = {key_name: {key_type: key}})

def get_from_dynamodb_batch(table_name, keys):
	return dynamodb.batch_get_item(TableName = table_name, RequestItems = keys)

def insert_into_dynamodb(table_name, data):
	result = False
	try:
		# http://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html
		response = dynamodb.put_item(TableName = table_name, Item = data)
		# response = dynamodb.batch_write_item(TableName = table_name, RequestItems = data)
		result = True
	except Exception as e:
		print(e)
		raise e
	return result

def upload_to_firehose(firehose_name, records):
	result = False
	# TO DO: figure out why the hell the lambda endpoint is blocking (can only execute one at a time)
	# time.sleep(60)
	try:
		result = True
		# http://boto3.readthedocs.io/en/latest/reference/services/firehose.html
		response = firehose.put_record_batch(
			DeliveryStreamName = 'kthera',
			Records = records
		)
	except Exception as e:
		print(e)
		raise e
	return result
