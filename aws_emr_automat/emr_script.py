import boto3
import subprocess


connection = boto3.client(
    'emr',
    region_name='REGION_ID',
    aws_access_key_id='ACCESS_KEY_ID',
    aws_secret_access_key='SECRET_ACCESS_KEY',
)

cluster_id = connection.run_job_flow(
    Name='CLUSTER_NAME',
    LogUri='S3_URI',
    ReleaseLabel='emr-5.33.0',
    Applications=[
        {
            'Name': 'Spark'
        },
    ],
    Instances={
        'InstanceGroups': [
            {
                'Name': "Master nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 1,
            },
            {
                'Name': "Slave nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 2,
            }
        ],
        'Ec2KeyName': 'EC2_KEY_NAME',
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Ec2SubnetId': 'subnet-SUBNET_ID',
    },
    Steps=[
                {
            'Name': 'setup - copy files',   
                    'ActionOnFailure': 'CANCEL_AND_WAIT',
                    'HadoopJarStep': {
                        'Jar': 'command-runner.jar',
                        'Args': ['aws', 's3', 'cp', 'S3_URI_SPARK_JOB/sparkjob.py', '/tmp/']
                    }
        },
        {
            'Name': 'spark job',   
                    'ActionOnFailure': 'CANCEL_AND_WAIT',
                    'HadoopJarStep': {
                        'Jar': 'command-runner.jar',
                        'Args': ['spark-submit', '/tmp/sparkjob.py']
                    }
        }
    ],

    VisibleToAllUsers=True,
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    Tags=[
        {
            'Key': 'tag_name_1',
            'Value': 'tag_value_1',
        },
        {
            'Key': 'tag_name_2',
            'Value': 'tag_value_2',
        },
    ],
)

print ('cluster created with the step...', cluster_id['JobFlowId'])

subprocess.Popen(["python", "FULLPATH/to/emrlaunchmail.py"])