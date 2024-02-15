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
    MultiAZ=False,  # Set to True for Multi-AZ deployment
    PubliclyAccessible=True,  # Set to False if you don't want public access
    Tags=[
        {
            'Key': 'Name',
            'Value': 'YourDatabase'
        },
    ],
)

# Print the response
print(response)