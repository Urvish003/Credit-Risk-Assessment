import pandas as pd
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix , ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score, accuracy_score
from joblib import dump, load
warnings.filterwarnings("ignore")

u1 = pd.read_csv("credit_risk_dataset.csv")
pd.set_option('display.max_rows',32581)
u1.head()

u1.isnull().sum()
u1.fillna(u1.mean(),inplace=True)

u1['target'] = LabelEncoder().fit_transform(u1['cb_person_default_on_file'])

u1=pd.get_dummies(u1,columns=['person_home_ownership','loan_intent'],prefix='',prefix_sep='')
u1 = u1.drop(columns=['loan_grade', 'cb_person_default_on_file'], axis=1)
x=u1.drop(columns='target')
X_train,X_test,y_train,y_test=train_test_split(x,u1['target'],random_state=51,test_size=0.20)

model=LogisticRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)


target_names = ['0', '1']
print(classification_report(y_test,pred, target_names=target_names))
#print(u1.columns)

#Save the model to disk
dump(model, 'model.joblib')