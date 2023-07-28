import boto3
import sys

instance_id = '' #adicione o id da instancia desejada

ec2_client = boto3.client('ec2', region_name='') #verifique o region_name onde sua instancia roda

action = sys.argv[1]

def action_instance(action):
    if action == 'start':
        response = ec2_client.start_instances(
        InstanceIds=['']
    )
        for info in response['StartingInstances']:
            current_state = info['CurrentState']['Name']
            previous_state = info['PreviousState']['Name']
            print(f'Resultado: Status anterior: {previous_state} - Status atual: {current_state}')
    elif action == 'stop':
        response = ec2_client.stop_instances(
        InstanceIds=['']
    )
        for info in response['StoppingInstances']:
            current_state = info['CurrentState']['Name']
            previous_state = info['PreviousState']['Name']
            print(f'Resultado: Status anterior: {previous_state} - Status atual: {current_state}')
    else:
        print('Ação não encontrada')

action_instance(action)