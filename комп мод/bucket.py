import boto3

def s3_client():
    session = boto3.session.Session()
    return session.client(
        service_name='s3',
        endpoint_url="https://storage.yandexcloud.net"
    )

buck = 'eminbucket'
key = 'ex.txt'

def s3_getAllFiles(buck: str):
    s = s3_client()
    for key in s.list_objects(Bucket=buck)['Contents']:
        print(key['Key'])

def s3_upload(file:str, buck:str, key:str):
    s = s3_client()
    s.upload_file(file, buck, key) 

def s3_get(buck:str, key:str):
    s = s3_client()
    get_obj = s.get_object(Bucket=buck, Key=key)
    print(get_obj['Body'].read())

def s3_delete(buck:str, key:str):
    s = s3_client()
    forDeletion = [{'Key':'object_name'}, {'Key': key }]
    response = s.delete_objects(Bucket=buck, Delete={'Objects': forDeletion})

s3_delete(buck, key)