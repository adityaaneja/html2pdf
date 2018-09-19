Quick and dirty lambda function to convert HTML to PDFs.
Uses wkhtml2pdf

- The code boto3 to to work with s3 buckets
- The context passes the name of the source bucket and the filename with the html extension
- The lambda function is called on the S3_put event
- destination_bucket is where the processed PDF file is placed

