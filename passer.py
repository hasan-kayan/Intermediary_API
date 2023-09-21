import os
import boto3
from flask import Flask, request, jsonify
import json

# AWS kimlik bilgilerini tanımlayın
AWS_ACCESS_KEY_ID = 'Your-Access-Key-ID'
AWS_SECRET_ACCESS_KEY = 'Your-Secret-Access-Key'
AWS_REGION = 'Your-Region'

# S3 bucket adını belirtin
S3_BUCKET_NAME = 'Your-S3-Bucket-Name'

# Flask uygulamasını oluşturun
app = Flask(__name__)

# AWS S3 istemcisini oluşturun
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

# Kullanıcı loglarını saklamak için bir dizin oluşturun
LOG_DIRECTORY = 'logs'
if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

# POST isteği işleme
@app.route('/process', methods=['POST'])
def process_data():
    try:
        data = request.json  # Gelen veriyi alın (JSON formatında)
        
        # Gelen veriyi S3 bucket'a kaydetme
        s3.put_object(Bucket=S3_BUCKET_NAME, Key=f'data/{data["user_id"]}.json', Body=json.dumps(data))
        
        # Kullanıcı logunu oluşturma
        log_file = os.path.join(LOG_DIRECTORY, f'{data["user_id"]}_log.txt')
        with open(log_file, 'a') as file:
            file.write(f'User ID: {data["user_id"]}, Data: {data}\n')
        
        return jsonify({'message': 'Data processed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
