import csv
import json
import boto3

# AWS kimlik bilgilerini tanımlayın
AWS_ACCESS_KEY_ID = 'Your-Access-Key-ID'
AWS_SECRET_ACCESS_KEY = 'Your-Secret-Access-Key'
AWS_REGION = 'Your-Region'

# S3 bucket adını belirtin
S3_BUCKET_NAME = 'Your-S3-Bucket-Name'

# CSV dosyasının adı ve yolu
CSV_FILE_PATH = 'user.csv'

# AWS S3 istemcisini oluşturun
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

# CSV dosyasını açın ve her bir satırı işleyin
with open(CSV_FILE_PATH, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Her bir kullanıcıyı JSON formatına dönüştürün
        user_json = json.dumps(row)
        
        # JSON verisini S3 bucket'a yükleyin
        s3.put_object(Bucket=S3_BUCKET_NAME, Key=f'users/{row["user_id"]}.json', Body=user_json)

print("CSV verileri JSON formatında S3 bucket'a yüklendi.")
