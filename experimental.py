import csv
import json
import boto3

# AWS kimlik bilgilerini tanımlayın
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = 'bPCc+'
AWS_REGION = 'eu-central-1'

# S3 bucket adını belirtin
S3_BUCKET_NAME = ''

# CSV dosyasının adı ve yolu
CSV_FILE_PATH = './data/user.csv'

# AWS S3 istemcisini oluşturun
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

# CSV dosyasını açın ve her bir satırı işleyin
with open(CSV_FILE_PATH, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Kullanıcı kimliğini oluşturun (örneğin, isim ve soyadın birleşimi)
        user_id = f'{row["Name"]}_{row["Surname"]}'.replace(" ", "_").lower()

        # Kullanıcı verilerini JSON formatına dönüştürün
        user_data = {
            "Name": row["Name"],
            "Surname": row["Surname"],
            "Email": row["Email"]
        }
        user_json = json.dumps(user_data, indent=4)

        # JSON verisini S3 bucket'a yükleyin
        s3.put_object(Bucket=S3_BUCKET_NAME, Key=f'users/{user_id}.json', Body=user_json)

print("CSV verileri JSON formatında S3 bucket'a yüklendi.")