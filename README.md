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

1. Creating conda environment
 ``` 
 conda create -p venv python==3.7 -y 
 ```

2. For activating environment
```
"conda activate venv/"
```
3. For installing packages in requirements.txt
```
pip install -r requirements.txt
```

4. To add files to git
```
git add <file_name> => for adding single file to git.
git add . => for adding all the files to your local git.
```
5. To check the git status
```
git status
```
6. To create version/commit all the changes to git

```
git commit -m "Message"
```
7. To send version/changes to github.
```
git push origin main
```

## 📒 Notebooks

1. EDA&Feature_engineering.ipynb

    In this Notebook, I have performed complete End-to-End Machine Learning process from DataIngestion to Data Evaluation
    * Steps Performed:
        1. Data Ingestion
        2. EDA
        3. Feature Engineering
        4. Feature Selection
        5. Sampling
        6. Model Training
        7. Best model using(AUC-ROC) curve
<br>
2. CreditCard_DefaultPrediction.ipynb

    This is the main syntax for the project i.e, main steps to be implemented in the project.


## 🦾 Tools & Technogies Used

![Technologies used](./templates/technologies.png)

## ✍️ Author

@Amitava Majumder





