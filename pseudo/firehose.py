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

firehose = boto3.client('firehose')

def lambda_handler(event, context):
	data = {}
	data['event'] = event

    data['firehose_upload_results'] = upload_to_firehose(
        'kthera',
        [
            {
                'Data': 'DANKALICIOUS!!!!oneone\nSIKK NO SCOPEZ M9\n'
            },
            {
                'Data': 'DA SIKKEST 720NOSCOPE!!!11oneone\n420BLAZEIT\n\n'
            }
        ]
    )

	return data

def upload_to_firehose(firehose_name, records):
	result = False;
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
