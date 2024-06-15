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
start_time_batch = time.time()

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

    if (index + 1) % batch_size == 0:
        end_time_batch = time.time()
        time_taken_batch = end_time_batch - start_time_batch
        print(f"\n{'=' * 40}")
        print(f"\nProcessed {index + 1} records | Successfully sent: {success_count} | Failed to send: {failure_count}")
        print(f"Time taken for this batch: {time_taken_batch} seconds")

        success_count = 0
        failure_count = 0
        time.sleep(90)

    print("Ok, continue")
    start_time_batch = time.time()

print("\nProcessing completed and file saved as upload_result.csv")
print(f"Total records processed: {len(df)} | Total successfully sent: {success_count} | Total failed to send: {failure_count}")

df.to_csv('upload_result.csv', index=False)
