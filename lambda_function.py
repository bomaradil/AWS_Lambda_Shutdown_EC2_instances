#shutdown Ec2 instances
import boto3

def Get_Running_Instances():
    """
    fonction to get ec2 instances that are in state Running or pending
    return a list of all the instance filter
    """
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['pending', 'running',]},])
    #you can also filter using Tags by adding the filters: 
    #[{'Name': 'tag-key', 'Values': ['Role','Name',]}, {'Name': 'tag-value', 'Values': ['*test*', '*TEST*',]},]
    return [instance.id for instance in instances]
    
def Stop_Instances(ids=Get_Running_Instances()):
    """
    shutdown the Ec2 instances that has been returned by the fonction Get_Running_Instances
    """
    ec2 = boto3.client('ec2')
    if not ids:
        #if the list of Ec2 instances is empty no action needed
        print("No Instance in the state Running or pending")
    else:
        ec2.stop_instances(InstanceIds=ids)
        ec2.get_waiter('instance_stopped').wait(InstanceIds=ids)
        #wait for the instances to have the state stopped.
        print('instance {} was shutdown'.format(ids))

def lambda_handler(event, context):
    Stop_Instances()
