# Phishing Domain Detection 💳


## 🪄 About

This is an End-to-End Machine Learning project with deployment. The project aims at developing a model and predict whether the domain is real or fake..

The project was created using Python Flask and deployed in Azure App services.

Link: : https://pishing-domain-checking.azurewebsites.net/



## 🏋🏻‍♂️ Motivation

Phishing is a type of fraud in which an attacker impersonates a reputable company or person in order to get sensitive information such as login credentials or account information via email or other communication channels. Phishing is popular among attackers because it is easier to persuade someone to click a malicious link that appears to be authentic than it is to break through a computer's protection measures.
The mail goal is to predict whether the domains are real or malicious.


## 📈 DataSource

Phishing Websites Dataset
Published: 24 September 2020 | Version 1 | DOI:10.17632/72ptz43s9v.1 | Contributor:Grega Vrbančič
# Description
These data consist of a collection of legitimate as well as phishing website instances. Each website is represented by the set of features which denote, whether website is legitimate or not. Data can serve as an input for machine learning process.

In this repository the two variants of the Phishing Dataset are presented.

## Full variant - dataset_full.csv
Short description of the full variant dataset:
Total number of instances: 88,647
Number of legitimate website instances (labeled as 0): 58,000
Number of phishing website instances (labeled as 1): 30,647
Total number of features: 111

## Small variant - dataset_small.csv
Short description of the small variant dataset:
Total number of instances: 58,645
Number of legitimate website instances (labeled as 0): 27,998
Number of phishing website instances (labeled as 1): 30,647
Total number of features: 111

## Google Drive link to access the Project Docs:
https://drive.google.com/drive/folders/1QPPIWe1lj7g9wUU1M0tqJlZntQHBEXdT?usp=sharing

## 🗂️ Project Directory tree


<a><img src='templates/dir_snip1.png' width="30%" height="50%"></a><br>
<a><img src='templates/dir_snip2.png' width="30%" height="50%"></a>

## 💻 Web UI

![image](https://user-images.githubusercontent.com/71118670/214281749-bbf964c0-41cb-43c8-90a1-369daba55a69.png)


## 📺 Demo Video

Demo Video Link: https://youtu.be/qn8MmiEdNao

## 🖥️ Installation

### 🛠️ Requirement packages
* numpy  
* pandas
* matplotlib
* sklearn
* Flask
* gunicorn
* imblearn
* xgboost
* mysql-connector-python
* six
* dill

### ⚙️ SetUp

##Step 1 - Install the requirements
pip install -r requirements.txt

##Step 2 - Run app.py file
python main.py

To download your dataset
https://data.mendeley.com/datasets/72ptz43s9v/1


#Git commands

If you are starting a project and you want to use git in your project

git init

Note: This is going to initalize git in your source code.

OR

#You can clone exiting github repo
git clone <github_url>
Note: Clone/ Downlaod github repo in your system

#Add your changes made in file to git stagging are
git add file_name
Note: You can given file_name to add specific file or use "." to add everything to staging are

#Create commits
git commit -m "message"
git push origin main
Note: origin--> contains url to your github repo main--> is your branch name

#To push your changes forcefully.
git push origin main -f
To pull changes from github repo

git pull origin main
Note: origin--> contains url to your github repo main--> is your branch name

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker


AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
AWS_ECR_LOGIN_URI=
ECR_REPOSITORY_NAME=
BUCKET_NAME=
MONGO_DB_URL=

#Command to re-run the ec2 instance:

cd actions-runner/
./run.sh

#GitHub Setting:

* Add Runner
* Add all the keys in the secret section


#Add Runner into EC2:

√ Connected to GitHub

# Runner Registration

Enter the name of the runner group to add this runner to: [press Enter for Default] 

Enter the name of runner: [press Enter for ip-172-31-32-83] self-hosted

This runner will have the following labels: 'self-hosted', 'Linux', 'X64' 
Enter any additional labels (ex. label-1,label-2): [press Enter to skip] 

√ Runner successfully added
√ Runner connection is good

#After adding the runer into github, use all the command availabe into ec2

#Install Docker into EC2

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker


## 🦾 Tools & Technogies Used

![Technologies used](./templates/technologies.png)

## ✍️ Author

@Amitava Majumder





