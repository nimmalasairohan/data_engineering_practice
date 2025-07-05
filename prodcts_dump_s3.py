import requests
import json
import logging
import boto3
from datetime import datetime

now = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
s3_key = f"raw/products/products_{now}.json"
s3 = boto3.client('s3')
bucket='rohandataengineeringpracticev1'
# ----------------- LOGGING -----------------
logging.basicConfig(
    filename=r"C:\Users\User\Documents\practice\data_engineering_project\data_extraction_v1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_api_product_data():
 
    
    try:    
            
          
            url = 'https://dummyjson.com/products'
            response = requests.get(url)
            

            if response.status_code == 200:
                data = response.json()
                return data
            if response.status_code == 200:
                logging.info(f"Fetched products ")
                               
                
                
            else:
                logging.warning(f"Failed to fetch for : {response.status_code}")
    except Exception as e:
            logging.error(f"Error fetching products for : {e}")
            return data
    
def upload_to_s3(data, bucket, key):
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(fetch_api_product_data()),
        ContentType='application/json'
    )
     



upload_to_s3(fetch_api_product_data(),bucket,s3_key)
print("dofccfbhhhfe")
#good
