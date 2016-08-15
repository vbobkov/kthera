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

s3 = boto3.client('s3')
# s3 = boto3.resource('s3')

def lambda_handler(event, context):
	data = {}
	data['event'] = event
    log_filename = '1337.txt'
    data['s3_upload_results'] = upload_to_s3('kthera', 'beeswax_archive/' + log_filename, 'DANKALICIOUS!!!!oneone\nSIKK NO SCOPEZ M9');

	# json_data = json.dumps(data)
	# print('Content-type: text/html\n\n')
	# print('Content-type: application/json\n\n')
	# print(json_data)
	# return json_data

	return data

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