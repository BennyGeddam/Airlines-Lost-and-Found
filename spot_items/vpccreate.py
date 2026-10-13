import boto3

    # Creating  new VPC
ec2 = boto3.client('ec2')

vpc_response = ec2.create_vpc(CidrBlock='172.30.0.0/16')
vpc_id = vpc_response['Vpc']['VpcId']
ec2.get_waiter('vpc_available').wait(VpcIds=[vpc_id])

print(f"VPC ID: {vpc_id}")
