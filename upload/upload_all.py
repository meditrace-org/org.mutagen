import pandas as pd
import requests
import json
import time

url = 'http://localhost:5142/api/v1/processing/upload'

df = pd.read_csv('yappy_hackaton_2024_400k.csv')
df['is_sent'] = False

def send_post_request(data):
    try:
        response = requests.post(url, json=data)
        if response.status_code == 202:
            return True
        else:
            print(f"Failed request: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Request failed: {e}")
        return False

success_count = 0
failure_count = 0
batch_size = 10000

for index, row in df.iterrows():
    data = {
        "video_link": str(row['link']),
        "description": str(row['description']) if pd.notna(row['description']) else ""
    }

    if send_post_request(data):
        df.at[index, 'is_sent'] = True
        success_count += 1
    else:
        failure_count += 1

    if (index + 1) % batch_size == 0 or (index + 1) == len(df):
        print(f"\nProcessed {index + 1} records | Successfully sent: {success_count} | Failed to send: {failure_count}")

    if (index + 1) % batch_size == 0:
        print(f"\n{'=' * 40}")
        print(f"Processed {index + 1} records, pausing for 60 seconds...")
        print(f"{'=' * 40}\n")
        time.sleep(60)

df.to_csv('upload_result.csv', index=False)

print("\nProcessing completed and file saved as output.csv")
print(f"Total records processed: {len(df)} | Total successfully sent: {success_count} | Total failed to send: {failure_count}")
