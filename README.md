# Shutdown Ec2 instances using AWS Lambda and python code

This python "Lambda_function.py code will shurdown running or pending ec2 instances in a region. 

## AWS python library boto3

the AWS SDK for Python (Boto3) will help call upon the aws services in your code and retrieve information or launch action. 

## the code

this code is devided in to tree python function.

1 - Get_Running_Instances.
  - 
  This function will get the ec2 instances that are in the state Running or pending.
  You can change the filters like explained in the comment to retrive the instances with a specific tag.
  [{'Name': 'tag-key', 'Values': ['Role','Name',]}, {'Name': 'tag-value', 'Values': ['*test*', '*TEST*',]},]
  the filters can be combined or used separately. 
  The function will return a list with all the running instances ids.

2 - Get_Running_Instances.
  -
  This function will shutdown the instances returned from the first function 
  and wait till the state of the instances change to shutdown before return an OK message.
  If the list returned is empty the function will do nothing.
  If your objectif is not to shutdown the instance but to terminated them or to start them, 
  you can change the stop_instances(InstanceIds=ids) with start_instance(InstanceIds=ids) to start the instances 
  or terminate_instances(InstanceIds=ids) to terminate them.
  Don’t forget to change the get_waiter methodes to check the new status ('instance_started', 'instance terminated').
      
3 - the lambda_handler.
  -
  launch the fonction Stop_Instances() in the lambda function.
  The Handler parameter for the Lambda function need to be "lambda_function.lambda_handler".
  Timeout need to be more than 1 min, so that our function can run properly 
  if you have an important number of instances to be shutdown, add more time to the Timeout parameter 
