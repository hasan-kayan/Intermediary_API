import boto3
import pandas as pd
import json
import os

# AWS S3 configuration
s3_bucket_name = 'your-s3-bucket-name'  # Replace with your S3 bucket name

# Initialize the AWS S3 client
s3_client = boto3.client('s3')

# Read the user data from the CSV file
csv_file_path = 'user_data.csv'  # Replace with the path to your CSV file
user_data_df = pd.read_csv(csv_file_path)

# Create a directory to store JSON files
json_dir = 'user_json_data'
os.makedirs(json_dir, exist_ok=True)

# Iterate through each row of the CSV data and save as JSON
for index, row in user_data_df.iterrows():
    user_data = {
        'Name': row['Name'],
        'Surname': row['Surname'],
        'Email': row['Email']
    }

    # Generate a unique JSON file name based on the user's name
    json_file_name = f'{row["Name"]}_{row["Surname"]}.json'

    # Save the user data as JSON
    with open(os.path.join(json_dir, json_file_name), 'w') as json_file:
        json.dump(user_data, json_file)

    # Upload the JSON file to S3
    s3_client.upload_file(
        os.path.join(json_dir, json_file_name),
        s3_bucket_name,
        f'user_data/{json_file_name}'  # Specify the S3 path where JSON files will be stored
    )

print(f'All user data JSON files uploaded to {s3_bucket_name}/user_data/')
