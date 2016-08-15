from __future__ import print_function
# from flask import request

import boto3
#import flask
import json
#import request
import sys
import time
import urllib

print('Initializing K\'Thera')

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
	data = {}
	data['event'] = event
	data['dynamodb_results'] = insert_into_dynamodb(
		'kthera_beeswax_feed',
		{
			'request_id': {'N': '1337'},
			'json': {'S': '{"uwot": "m8??"}'}
		}
	)

	return data

def insert_into_dynamodb(table_name, data):
	result = False;
	try:
		# http://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html
		response = dynamodb.put_item(TableName = table_name, Item = data)
		# response = dynamodb.batch_write_item(TableName = table_name, RequestItems = data)
		result = True;
	except Exception as e:
		print(e)
		raise e
	return result;
