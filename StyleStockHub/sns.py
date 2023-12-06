import boto3

# Replace these values with your AWS credentials
aws_access_key_id = 'AKIAXMBMCIMY2HQEDM54'
aws_secret_access_key = '4HdrlfkViWXg9xojo74oelkxFa9Z55luR00btjKj'
region_name = 'us-east-1'

# Create an SNS client
sns_client = boto3.client('sns', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Create an SNS topic
topic_response = sns_client.create_topic(Name='MySNSTopic')
topic_arn = topic_response['TopicArn']

# Subscribe an email endpoint to the topic
subscription_response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='nelaturiankitha@gmail.com'
)

# Wait for user to confirm subscription (check email and click the confirmation link)

# Publish a message to the topic
message = 'Check your CPU'
publish_response = sns_client.publish(
    TopicArn=topic_arn,
    Message=message,
    Subject='Test Message'
)

print(f"Message published with MessageId: {publish_response['MessageId']}")
