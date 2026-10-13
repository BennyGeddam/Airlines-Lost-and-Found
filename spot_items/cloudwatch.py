import boto3
# Creatating CloudWatch client
  # Creating alaram name CPUALERT
    #threshold up to: 1%
      # Evaluation Period:300 seconds-5 minutes
session = boto3.Session(
    region_name='us-east-1'
)


cloudwatch = session.client('cloudwatch')


cloudwatch.put_metric_alarm(
    AlarmName='CPUALERT',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period=300,
    Threshold=1,
    ComparisonOperator='GreaterThanOrEqualToThreshold',
    EvaluationPeriods=2,
    AlarmActions=['arn:aws:sns:us-east-1:975049949964:item-r'],
    Dimensions=[{'Name': 'InstanceId', 'Value': 'i-0d889824288843aef'}],
)

print("CloudWatch alarm created or updated successfully.")
