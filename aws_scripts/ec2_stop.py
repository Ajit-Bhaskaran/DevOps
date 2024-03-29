import boto3
ec2 = boto3.client('ec2') #creates ec2 client
response = ec2.describe_instances() #describes ec2 instances in your account

for reservation in response['Reservations']: 
    for instance in reservation['Instances']:   # going through reservations and instances to find running instances
        if instance['State']['Name'] == 'running' and instance['InstanceId'] != 'YOUR-INSTANCE-ID': #prevents your instance from stopping
            print(instance['InstanceId']) #Prints running instances id
            response2 = ec2.stop_instances(
            InstanceIds=[instance['InstanceId'], #stops the running instances from above
        ],
)

print(response2) #prints status code 200, instances being stopped