import boto3

# setting up the SNS in the 'us-east-1' region
    # making sure we have our SNS topic ready
          # storing the topic's ARN
                # making a message based on lost item details
                        # sending the message to SNS topic
                              # useing the ARN
                                # giving back the message ID
sns = boto3.client('sns', region_name='us-east-1')
response = sns.create_topic(Name='item-r')
topic_arn = response['TopicArn']

def send_notification(item_details):
    message = f"New Lost Item Report Received:\nDescription: {item_details['description']}\nTitle: {item_details['title']}\nLocation: {item_details['location']}\nDate Lost: {item_details['lost_date']}"

    response = sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject='Lost And Found Alert'
    )
    return response['MessageId']
