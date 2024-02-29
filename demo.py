import boto3

# get the list of ec2 instances from the region eu-central-1 with instance state as running
""" ec2 = boto3.resource('ec2', region_name='eu-central-1')
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)
    print(instance.state)
    print(instance.public_dns_name)
    print(instance.tags)
    print(instance.key_name)
    print(instance.vpc_id)
    print(instance.subnet_id) """

        
    


# #get the list of s3 buckets
# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)
    

#create an ec2 instance with linux 2023 ami in the region eu-central-1 
ec2 = boto3.resource('ec2', region_name='eu-central-1')
# The code snippet you provided is using the `boto3` library in Python to create a new EC2 instance in
# the region `eu-central-1` with specific configurations. Here is a breakdown of the parameters used
# in the `ec2.create_instances` method:
instances = ec2.create_instances(
    ImageId='ami-0a23a9827c6dab833',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    SecurityGroupIds=['sg-0b87859cdb902c597'],
    SubnetId='subnet-0fd788bcc8e87df5c') 
    
        