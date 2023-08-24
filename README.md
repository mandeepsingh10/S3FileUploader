# S3FileUploader
This project utilizes a combination of Python, shell scripts, and GitHub Action workflows to facilitate the uploading of files to S3 Buckets.

## Uploading Files to S3 Buckets using S3Fileuploader

Please refer to the detailed step-by-step instructions below for using this repository to upload files to Amazon S3.

## Steps:

1. **Clone the Repository**
- Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your-username/your-repo.git

2. **Create a New Feature Branch**
    ```bash
   git checkout -b UploadFilesToStaging-TicketId 

3. **Create a Data Folder** 
- In the root directory of the repository, create a folder named data.

4. **Add Your Files**
- Place the files you want to upload in the data folder.

5. **Create {env}.vars File** 
- Depending on the environment you're uploading to (e.g. dev, staging, sandbox, prod) create a file named {env}.vars in the root directory. For example, if uploading to staging, create staging.vars.
- Examples are included in the repo, please refer to the examples directory to check the variable names for each environment.

6. **Update {env}.vars File**
- Edit the {env}.vars file and update the bucket name and S3 upload location with your specific values. Let's say you want to upload files to staging environment.
    ```bash
    StagingBucketName=Enter_Bucket_Name_here
    StagingS3UploadLocation=Enter_S3_Upload_Path_here

7. **Commit and Push Changes**

8. **Create a Pull Request**

9. **Get the PR reviewed and approved** 

10. **Merge the Feature Branch**


## GitHub Actions Workflow

- We have two GitHub Action workflows.

    1. **S3Uploader**
    - After merging, the GitHub Actions workflow (S3Uploader.yml) will automatically run. This workflow will use the information in {env}.vars to upload files to Amazon S3.
    2. **Cleanup**
    - After the S3Uploader workflow is completed, the cleanup.yml workflow will automatically run. This cleanup workflow deletes the data folder and the *.vars files in the main branch that were added when the feature branch was merged. 
    - This ensures that the Main branch is in the correct state for the next batch of file uploads.

## Important Notes

- Please be aware that the specified S3UploadLocation—the path to which you intend to upload files from the data directory—will be automatically created in the target bucket if it doesn't already exist. Therefore, it's crucial to thoroughly review and confirm the accuracy of the upload path before proceeding with committing any changes.


