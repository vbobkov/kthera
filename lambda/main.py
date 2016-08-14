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
s3 = boto3.resource('s3')

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

	log_filename = '1337.txt'

	data['s3_log'] = upload_to_s3('kthera', 'beeswax_archive/' + log_filename, 'DANKALICIOUS!!!!oneone\nSIKK NO SCOPEZ M9');

	return data

def upload_to_s3(bucket_name, filepath, content):
	result = False;
	# TO DO: figure out why the hell the lambda endpoint is blocking (can only execute one at a time)
	# time.sleep(10)
	try:
		# http://boto3.readthedocs.io/en/latest/reference/services/s3.html
		s3.Bucket(bucket_name).put_object(ACL = 'private', Body = content, Key = filepath)
		result = True;
	except Exception as e:
		print(e)
		# print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
		print('Error setting object {} in bucket {}.'.format(filepath, bucket_name))
		raise e
	return result