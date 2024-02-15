import boto3


# Initialize the RDS client
rds_client = boto3.client('rds', region_name='us-east-1')

# Define parameters for the RDS instance
db_instance_identifier = 'CLI-generated-MysqlDB'
db_instance_class = 'db.t2.micro'
engine = 'mysql'
db_name = 'CLI_generated'
master_username = 'admin'
master_password = 'qJtAafmubZcaULFyxUHb'
allocated_storage = 20

# Create the RDS instance
response = rds_client.create_db_instance(
    DBInstanceIdentifier=db_instance_identifier,
    DBInstanceClass=db_instance_class,
    Engine=engine,
    DBName=db_name,
    MasterUsername=master_username,
    MasterUserPassword=master_password,
    AllocatedStorage=allocated_storage,
    MultiAZ=False,  
    PubliclyAccessible=True,  
    Tags=[
        {
            'Key': 'Name',
            'Value': 'cli generated'
        },
    ],
)

waiter = rds_client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=db_instance_identifier)    


# Retrieve DB instance details including endpoint
describe_response = rds_client.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)

# Print the DB endpoint
endpoint = describe_response['DBInstances'][0]['Endpoint']['Address']
print("RDS DB instance created successfully. Endpoint:", endpoint)
 