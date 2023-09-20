# Import necessary modules
import socket  # Import the socket module for networking operations
import json    # Import the json module for JSON data handling
import boto3   # Import the boto3 module for AWS services integration

# AWS S3 configuration
s3_bucket_name = 'your-s3-bucket-name'  # Replace with your S3 bucket name
s3_object_key = 'data.json'             # Name of the object to store in S3

# Server settings
host = '0.0.0.0'  # Listen on all network interfaces (accept connections from any IP)
port = 12345      # Listen for incoming connections on port 12345

# Start the AWS S3 client
s3_client = boto3.client('s3')  # Initialize the AWS S3 client for interacting with S3 services

# Begin listening for data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Create a socket object using IPv4 addressing and TCP protocol
    s.bind((host, port))  # Bind the socket to the specified host and port
    s.listen()            # Begin listening for incoming connections
    print(f"Listening on: {host}:{port}")
    conn, addr = s.accept()  # Accept an incoming connection and get the client's address
    with conn:
        print(f"Connected by: {addr}")  # Print the address of the connected client
        data = b""  # Initialize an empty binary data variable to store incoming data
        while True:
            chunk = conn.recv(1024)  # Receive data in chunks of 1024 bytes
            if not chunk:
                break
            data += chunk  # Append received data to the data variable

        # Parse incoming data as JSON
        try:
            json_data = json.loads(data.decode('utf-8'))  # Parse the received data as JSON
            print("Received JSON data:", json_data)      # Print the received JSON data
            
            # Upload JSON data to S3
            s3_client.put_object(
                Bucket=s3_bucket_name,                  # Specify the S3 bucket name
                Key=s3_object_key,                      # Specify the object key (filename) in S3
                Body=json.dumps(json_data),             # Convert JSON data to a string
                ContentType='application/json'          # Set the content type as JSON
            )
            print(f"Data saved to {s3_bucket_name}/{s3_object_key}.")  # Print a success message
        except Exception as e:
            print("JSON parsing or S3 upload error:", str(e))  # Handle JSON parsing or S3 upload errors
