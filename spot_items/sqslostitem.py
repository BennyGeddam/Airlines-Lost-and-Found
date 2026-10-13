import boto3
# setting SQS client.
    # description.
        # SQS clien setup.
            # checking 'mysqs' queue exists.
                # function to send a message based on item details to the SQS queue.
                    # message with details of lost.
                        # sends the message to the SQS queue and gets the ID of the sent message.

sqs = boto3.client('sqs')

response = sqs.create_queue(QueueName='mysqs')
queue_url = response['QueueUrl']

def send_message_to_sqs(item_details):
    message = f"New Lost Item Report Received:\nDescription: {item_details['description']}\nTitle: {item_details['title']}\nLocation: {item_details['location']}\nDate Lost: {item_details['lost_date']}"
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    return response['MessageId']
