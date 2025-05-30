# Secure Cloud-to-Cloud Data Migration

A secure method for cloud-to-cloud data migration using Linux command-line tools, with a focus on data security and the use of open-source solutions.


PHASE 1: Environment Setup</br>
Step 1: Create Cloud Accounts</br>
Sign up for AWS</br>
Sign up for Azure as the destination</br>
Create S3 Bucket in AWS and a Container in Azure</br>
![Screenshot 2025-05-04 150153](https://github.com/user-attachments/assets/2ff013c9-6369-430f-acfc-b8b6b45796fc)
![Screenshot 2025-05-04 150247](https://github.com/user-attachments/assets/9a342c19-1c5e-4d62-b9b5-accf364a2d5e)

Step 2: Install Tools</br>
On Ubuntu (Linux VM or system):</br>
sudo apt update sudo apt install rclone openssl python3 python3-pip -y
![Screenshot from 2025-05-04 14-28-37](https://github.com/user-attachments/assets/93457510-54e4-48b1-b769-92ec7b13e016)</br>
These tools are: </br>
rclone: Transfers files between clouds</br> openssl: Encrypts/decrypts files securely python3 & </br>hashlib: Checks file integrity 

PHASE 2: Secure File Transfer Process </br>
Step 3: Configure rclone (Cloud Connections) rclone config </br>
![Screenshot from 2025-05-04 14-35-36](https://github.com/user-attachments/assets/c71fa428-67e0-4344-8ac8-964d7d175b62)</br>
Press n for new remote </br>
Name it: aws_remote </br>
Choose type: s3 (Amazon S3) </br>
Provide your AWS Access Key & Secret </br>
Use default or select region </br>
Repeat for Azure: </br>
Name it: azure_remote </br>
Log in via browser when asked </br>
![Screenshot from 2025-05-04 14-38-56](https://github.com/user-attachments/assets/9974c47b-1204-46cc-aaef-56daa5a7ca66)



