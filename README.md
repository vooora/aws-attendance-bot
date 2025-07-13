# aws-attendance-bot
## AWS BITSian Fingerprint Attendance System + Chatbot

### Technologies Used
<a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a>

### Purpose
At BITS Pilani, exam attendance is typically recorded manually, even though every classroom is equipped with fingerprint scanners. 

This project leverages that unused infrastructure to automate not just attendance tracking, but also monitor student behavior during exams. For example, it can log when a student leaves the room for a restroom break and when they return, or track how early students are leaving the exam. Such insights allow teachers further insights on their exam quality. 

A speaker at a conference I attended highlighted the convenience querying databases using natural language. Inspired by the talk, this project brings that vision to life in a scalable system, and tailored for modern exam monitoring.

### Technical Details

Student fingerprints are securely stored in an **S3 bucket** with **lifecycle policies** for managing old data. During the exam, students scan their fingerprints, which are matched using Amazon Rekognition. The corresponding timestamps are logged in an **AWS RDS database**. 

Teachers can retrieve this data effortlessly by asking questions like “Who was absent for the exam?” or “How many students left early?” in plain English. Powered by AWS Lex and OpenAI's LLM, the system translates these natural language queries into SQL in real time. All operations are handled via **AWS Lambda**, with performance and logs monitored through **Amazon CloudWatch**.

Below is the architecture of the project.

<img width="1600" height="1170" alt="image" src="https://github.com/user-attachments/assets/79987d4e-6046-4152-b155-5622976110c1" />


