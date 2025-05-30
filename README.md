# Secure Cloud-to-Cloud Data Migration

A secure method for cloud-to-cloud data migration using Linux command-line tools, with a focus on data security and the use of open-source solutions.


# PHASE 1: Environment Setup</br>
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

# PHASE 2: Secure File Transfer Process </br>
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

Step 4: Encrypt the File (VERY HIGH SECURITY) 
![Screenshot from 2025-05-04 14-49-30](https://github.com/user-attachments/assets/4420fbe4-17e5-458f-a151-29e4eebb13fa)
This uses AES-256, one of the strongest encryption standards. Without the password, decryption is impossible. 
 
Step 5: Transfer Encrypted File Between Clouds 
Upload to AWS 
![Screenshot from 2025-05-04 14-55-14](https://github.com/user-attachments/assets/14685c93-fc2c-483a-97ae-318ec53279ce)

Transfer from AWS to Azure 
![Screenshot from 2025-05-04 14-58-31](https://github.com/user-attachments/assets/84834ba0-1dd6-4a18-a3b5-89a36d51bafc)

Step 6: Decrypt at Destination 
![Screenshot from 2025-05-04 15-12-13](https://github.com/user-attachments/assets/61db25aa-7e54-432a-ac7d-cc32c757f99e)

Step 7: Verify File Integrity (Python Script)
Create a file verify_hash.py: 
![Screenshot from 2025-05-04 15-28-28](https://github.com/user-attachments/assets/42700151-4840-4ff4-8e8a-aa3c33923595)
![Screenshot from 2025-05-04 15-39-24](https://github.com/user-attachments/assets/099a257f-f3a9-4da1-a523-a9ae10d92cb2)
You can also open the migration_log.txt to see the log: 
![Screenshot from 2025-05-04 16-00-23](https://github.com/user-attachments/assets/e2b7224b-3b42-46af-8168-1f73fd88e5a5)

# PHASE 3: Simulate Hacking Attempt
Attack 1: Wrong Decryption Key 
![Screenshot from 2025-05-04 16-12-23](https://github.com/user-attachments/assets/19b6a330-6699-4839-934f-340ee5c72bf2)
Result: "bad decrypt" error 

Attack 2: File Tampering Attack
![Screenshot from 2025-05-04 17-01-37](https://github.com/user-attachments/assets/1ec58fd3-e942-4835-9fe0-e1d0c935b048)
So, the attack is detected 


