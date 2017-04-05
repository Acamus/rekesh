# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection	
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load Bank Transcation dataset
#url
url = "txnDetails.csv"
names = ['Customer_ID', 'Txn_Date','Txn_Amount', 'Credit/Debit']
txn_dataset = pandas.read_csv(url, names=names)
print(txn_dataset.shape)

# converting date from string to date times
#txn_dataset['Txn_Date']  = txn_dataset['Txn_date'].apply(dateutil.parser.parse, dayfirst=True)

#how many txn per day
txn_per_day=txn_dataset['Customer_ID'].value_counts()
print(txn_per_day.head(10))
plt.hist(txn_per_day)
#plt.show()
print(txn_dataset['Txn_Amount'].max())



print("start of before nov group")
#group by <date
before_nov=txn_dataset[txn_dataset['Txn_Date']<="8/11/2016"].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
before_nov.to_csv(path='before8Nov.csv',sep=',',index=['Customer_ID','Txn_Date','Credit/Debit'],index_label=['Customer_ID','Txn_Date','Credit/Debit'])
after_nov=txn_dataset[txn_dataset['Txn_Date']>"8/11/2016"].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
after_nov.to_csv(path='after8Nov.csv',sep=',',index=['Customer_ID','Txn_Date','Credit/Debit'],index_label=['Customer_ID','Txn_Date','Credit/Debit'])

beforeUrl="before8Nov.csv"
before_names=['Customer_ID','Txn_Date','Credit/Debit','Txn_Amount']
before_txn_dataset=pandas.read_csv(beforeUrl,names=before_names)
afterUrl="after8Nov.csv"
after_names=['Customer_ID','Txn_Date','Credit/Debit','Txn_Amount']
after_txn_dataset=pandas.read_csv(afterUrl,names=after_names)

#gettiing all values req
get_credit_before=before_txn_dataset[before_txn_dataset['Credit/Debit']=="Cr"].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
get_debit_before=before_txn_dataset[before_txn_dataset['Credit/Debit']=="Dr"].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
get_credit_after=before_txn_dataset[before_txn_dataset['Credit/Debit']=="Cr"].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()
get_debit_after=before_txn_dataset[before_txn_dataset['Credit/Debit']=="Dr"].groupby(['Customer_ID','Txn_Date','Credit/Debit'])['Txn_Amount'].sum()

#writing it to file
get_credit_before=pandas.to_csv(path='credit_before8Nov.csv',spe=',')
get_debit_before=pandas.to_csv(path='debit_before8Nov.csv',spe=',')
get_credit_after=pandas.to_csv(path='credit_after8Nov.csv',spe=',')
get_debit_after=pandas.to_csv(path='debit_after8Nov.csv',spe=',')


print(after_nov.head(10))
#print(before_nov.head[4])

#groups
g_customer=len(txn_dataset.groupby(['Credit/Debit']).groups['Cr'])
#print(g_customer.head(3))

# get the sum of transcations credited for every month for each customer 
a = txn_dataset[txn_dataset['Credit/Debit']=="Dr"].groupby(['Customer_ID','Txn_Date'])['Txn_Amount'].sum()
#a.to_csv(path='a.csv',sep=',')
print(a.shape)
#print(a.head(40))

#plt.hist(txn_dataset[txn_dataset["Credit/Debit"]=='Cr ' and txn_dataset["Txn_Date"]<='08/11/2016'])
#plt.show()

# get the sum of transcations debited for every month for each customer
#print(txn_dataset[txn_dataset['Credit/Debit']=="Dr"].groupby('Customer_ID')['Txn_Amount'].sum())

