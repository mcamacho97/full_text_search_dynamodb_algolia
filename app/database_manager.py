import boto3
import os

TABLE_NAME = os.environ['DYNAMO_DB_TABLE_NAME']
client = boto3.client('dynamodbs')


def save_person(person):
    return client.put_item(
        TableName=TABLE_NAME,
        Item=person
    )


