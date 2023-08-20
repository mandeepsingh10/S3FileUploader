import boto3
import sys
import os

def upload_files_in_directory(bucket_name, aws_key, aws_access_key, aws_access_secret, local_path):
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_access_secret,
    )
    client = session.client('s3')
    
    files_found = False  # Flag to check if any files are found

    for root, _, files in os.walk(local_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_key = os.path.relpath(local_file_path, local_path)

            print(f"Uploading {local_file_path} to S3://{bucket_name}/{s3_key}")
            response = client.upload_file(
                Filename=local_file_path,
                Bucket=bucket_name,
                Key=os.path.join(aws_key, s3_key)
            )
            
            files_found = True  # Set the flag to true if any files are found

    if not files_found:
        print('No files found in directory')
    else:
        print('Done uploading all files')

def main():
    if len(sys.argv) < 6:
        print('Error: Required 5 arguments.')
        sys.exit(1)

    bucket_name = sys.argv[1]
    aws_key = sys.argv[2]
    aws_access_key = sys.argv[3]
    aws_access_secret = sys.argv[4]
    local_path = sys.argv[5]

    upload_files_in_directory(bucket_name, aws_key, aws_access_key, aws_access_secret, local_path)

if __name__ == "__main__":
    main()
