#!python
import boto3
import botocore
import pdfkit
import os
# Checks if the file exists


# Main function. Entrypoint for Lambda
def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    destination_bucket='ca.ualberta.edrms.pdfout'
    #extract the filename without the extension
    filename = os.path.splitext(key)[0]
    print filename
    #create the temproary file path
    tempfilepath = os.path.join("/tmp/"+filename+".pdf")
    #create the outputfile name
    outputfilename = os.path.join(filename+".pdf")
    #Create boto3 Object to destination bucket
    s3source = boto3.resource('s3')
    obj=s3source.Object(bucket, key)
    pdfkit.from_string(obj.get()["Body"].read(),tempfilepath)
    s3destination = boto3.resource('s3')
    data = open(tempfilepath,'rb')
    s3destination.Bucket(destination_bucket).put_object(Key=outputfilename, Body=data)
    os.remove(tempfilepath)




