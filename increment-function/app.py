import json, boto3

client = boto3.client('dynamodb')
TableName = 'cloud-resume'


def lambda_handler(event, context):
    response = client.update_item(
        TableName='cloud-resume',
        Key={
            'ID': {'S': 'visitor_count'}
        },
        UpdateExpression='ADD quantity :inc',
        ExpressionAttributeValues={":inc": {"N": "1"}},
        ReturnValues='UPDATED_NEW'
    )

    value = response['Attributes']['quantity']['N']

    return {
        'statusCode': 200,
        'body': value
    }
