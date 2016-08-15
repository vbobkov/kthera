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

# s3 = boto3.client('s3')
# s3 = boto3.resource('s3')
# firehose = boto3.client('firehose')
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
	# print('{"wtf":"srs"}');
	data = {}
	data['event'] = event
	# data['context'] = context
	# print(data)

	# json_data = json.dumps(data)
	# print('Content-type: text/html\n\n')
	# print('Content-type: application/json\n\n')
	# print(json_data)
	# return json_data

	# log_filename = '1337.txt'
	# data['s3_upload_results'] = upload_to_s3('kthera', 'beeswax_archive/' + log_filename, 'DANKALICIOUS!!!!oneone\nSIKK NO SCOPEZ M9');
	# data['firehose_upload_results'] = upload_to_firehose(
		# 'kthera',
		# [
			# {
				# 'Data': 'DANKALICIOUS!!!!oneone\nSIKK NO SCOPEZ M9\n'
			# },
			# {
				# 'Data': 'DA SIKKEST 720NOSCOPE!!!11oneone\n420BLAZEIT\n\n'
			# }
		# ]
	# )

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

def upload_to_s3(bucket_name, filepath, data):
	result = False;
	try:
		# http://boto3.readthedocs.io/en/latest/reference/services/s3.html
		s3.Bucket(bucket_name).put_object(ACL = 'private', Body = data, Key = filepath)
		result = True;
	except Exception as e:
		print(e)
		print('Error setting object {} in bucket {}.'.format(filepath, bucket_name))
		raise e
	return result

def upload_to_firehose(firehose_name, records):
	result = False;
	# TO DO: figure out why the hell the lambda endpoint is blocking (can only execute one at a time)
	# time.sleep(60)
	try:
		result = True;
		# http://boto3.readthedocs.io/en/latest/reference/services/firehose.html
		response = firehose.put_record_batch(
			DeliveryStreamName = 'kthera',
			Records = records
		)
	except Exception as e:
		print(e)
		raise e
	return result
