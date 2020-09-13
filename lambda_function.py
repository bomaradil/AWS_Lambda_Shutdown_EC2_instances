# Shutdown Ec2 instances using AWS Lambda and python code
#This Python code will shutdown running or pending ec2 instances in that region 

#import the aws library boto3
import boto3

def Get_Running_Instances():
    """
    function to get ec2 instances that are in state Running or pending
    and return a list with all the instances id
    """
    ec2 = boto3.resource('ec2') 
    #call the features resource from the boto3 library
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['pending', 'running',]},])
    #filter the instances returned using the state name
    #you can also filter using Tags by adding the filters: 
    #[{'Name': 'tag-key', 'Values': ['Role','Name',]}, {'Name': 'tag-value', 'Values': ['*test*', '*TEST*',]},]
    return [instance.id for instance in instances]
    #return a liste with the ids of the instances
    
def Stop_Instances(ids=Get_Running_Instances()):
    """
    shutdown the Ec2 instances that has been returned by the function Get_Running_Instances
    """
    ec2 = boto3.client('ec2')
    #call the features client from the boto3 library
    if not ids:
        #if the list of Ec2 instances returned is empty.
        print("No Instance in the state Running or pending")
    else:
        ec2.stop_instances(InstanceIds=ids)
        #stop the instances using their id
        ec2.get_waiter('instance_stopped').wait(InstanceIds=ids)
        #wait for the state of the instances to change to stopped.
        print('instance {} was shutdown'.format(ids))

def lambda_handler(event, context):
    """
    launch the function Stop_Instances() in the lambda function 
    Handler for the Lambda function "lambda_function.lambda_handler"
    Timeout need to be more than 1 minute, so that our function can run perfectly 
    if you have an important number of instances to be shutdown, change the parameter of timeout
    """
    Stop_Instances()

