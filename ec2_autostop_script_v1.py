import boto3  # Import AWS SDK for Python

def lambda_handler(event, context):
    # Entry point for the Lambda function
    stop_ec2_instances()  # Call the function to stop EC2 instances

def stop_ec2_instances():
    ec2 = boto3.client('ec2')  # Initialize EC2 client
    # Retrieve all instances in 'running' state
    instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )

    # Extracting instance IDs from the response
    running_instances = [instance['InstanceId'] for reservation in instances['Reservations'] for instance in reservation['Instances']]
    
    if running_instances:
        # If there are running instances, print their IDs and issue a stop command
        print(f"Stopping instances: {running_instances}")
        ec2.stop_instances(InstanceIds=running_instances)
    else:
        # If no running instances are found, log this information
        print("No running instances found.")

# Note: The function logs will be available in AWS CloudWatch under the /aws/lambda/<function-name> log group.

