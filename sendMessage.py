import boto3

sns = boto3.client('sns',region_name = "us-east-1" )

response = sns.publish(
    TopicArn = "arn:aws:sns:us-east-1:124058707612:satvik-sns",
    Message='Welcome to session',
    Subject='Session',
)

print("Message has been sent sucessfully")