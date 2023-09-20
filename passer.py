import socket
import json
import boto3

# AWS S3 configuration
s3_bucket_name = 'your-s3-bucket-name'  # Replace with your S3 bucket name
s3_object_key = 'data.json'  # Name of the object to store in S3

# Server settings
host = '0.0.0.0'  # Listen on all interfaces
port = 12345  # Listen for connections on this port

# Start the AWS S3 client
s3_client = boto3.client('s3')

# Begin listening for data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f"Listening on: {host}:{port}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by: {addr}")
        data = b""
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            data += chunk

        # Parse incoming data as JSON
        try:
            json_data = json.loads(data.decode('utf-8'))
            print("Received JSON data:", json_data)
            
            # Upload JSON data to S3
            s3_client.put_object(
                Bucket=s3_bucket_name,
                Key=s3_object_key,
                Body=json.dumps(json_data),
                ContentType='application/json'
            )
            print(f"Data saved to {s3_bucket_name}/{s3_object_key}.")
        except Exception as e:
            print("JSON parsing or S3 upload error:", str(e))
