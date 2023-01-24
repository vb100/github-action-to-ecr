# Phishing Domain Detection 💳


## 🪄 About

This is an End-to-End Machine Learning project with deployment. The project aims at developing a model and predict whether the domain is real or fake..

The project was created using Python Flask and deployed in Azure App services.

Link: : https://pishing-domain-checking.azurewebsites.net/



## 🏋🏻‍♂️ Motivation

Phishing is a type of fraud in which an attacker impersonates a reputable company or person in order to get sensitive information such as login credentials or account information via email or other communication channels. Phishing is popular among attackers because it is easier to persuade someone to click a malicious link that appears to be authentic than it is to break through a computer's protection measures.
The mail goal is to predict whether the domains are real or malicious.


## 📈 DataSource

In the dataset we have 25 columns which reflect various attributes of the customer. The target column is default.payment.next.month which tells whether a person will default or not. In this dataset, we have information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card holders from April 2005 to September 2005.

Datasource Link: https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

## 🗂️ Project Directory tree


<a><img src='templates/dir_snip1.png' width="30%" height="50%"></a><br>
<a><img src='templates/dir_snip2.png' width="30%" height="50%"></a>

## 💻 Web UI

<a><img src='templates/Home.png' width="60%" height="45%"></a>

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

@Ravi Teja Mandarapu





