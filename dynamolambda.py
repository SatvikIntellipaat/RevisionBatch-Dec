import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.client('dynamodb')
    print(event)

    table_name = "Cart"

    if(event['requestContext']['http']['method'] == 'PUT'):
        return put_data(event,table_name,dynamodb)

    response =  dynamodb.scan( TableName=table_name)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

def put_data(event,table_name,dynamodb):
    body = json.loads(event['body'])
    pid = body.get('product_id')
    name = body.get('product_name')

    print(pid)
    print(name)
    try: 
        dynamodb.put_item(
            TableName=table_name,
            Item={
                'product_id': {'S': pid},
                'product_name': {'S': name}
                }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item added successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 300,
            'body': json.dumps({'error': str(e)})
        }