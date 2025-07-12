from sklearn.datasets import load_diabetes
import sklearn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

df = load_diabetes()
# print(df)
data = pd.DataFrame(df.data)
# print(data)
data.columns = df.feature_names
# print(data.head())
data["future"] = df.target
# print(data.head())
X = data.iloc[:,:-1] #dependent
Y = data.iloc[:,-1] #independent

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
lin_reg = LinearRegression()
mse = cross_val_score( lin_reg , X , Y , scoring="neg_mean_squared_error" , cv=5)
# print(mse)
mean_mse = np.mean(mse)
print("Linear Regression",mean_mse)


# ==================RIDGE REGRESSION================
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
ridge = Ridge()
params = { "alpha" : [1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20] }
ridge_reg = GridSearchCV(ridge , params , scoring="neg_mean_squared_error" , cv=5)
ridge_reg.fit(X,Y)
print("Ridge Regression alpha",ridge_reg.best_params_)
print("Ridge Regression score",ridge_reg.best_score_)


from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
lasso = Lasso()
params = { "alpha" : [1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20] }
lasso_reg = GridSearchCV(ridge , params , scoring="neg_mean_squared_error" , cv=5)
lasso_reg.fit(X,Y)
print("Lasso Regression alpha",lasso_reg.best_params_)
print("Lasso Regression score",lasso_reg.best_score_)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.33,random_state=42)

y_pred_lasso = lasso_reg.predict(X_test)
y_pred_ridege = ridge_reg.predict(X_test)
from sklearn.metrics import r2_score
r2score_lasso = r2_score(y_pred_lasso,Y_test)
r2score_ridge = r2_score(y_pred_ridege,Y_test)
print("lasso r2score",r2score_lasso)
print("Ridge r2score", r2score_ridge)


# =====================Logistic Regression=================
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
dff = load_breast_cancer()
LX = pd.DataFrame(dff['data'],columns=dff['feature_names'])
# print(LX)
LY = pd.DataFrame(dff['target'],columns=['target'])
# print(LY)
LX_train,LX_test,LY_train,LY_test = train_test_split(LX,LY,test_size=0.33,random_state=42)
Lparams = [{'C':[1,5,10]},{'max_iter':[100,150]}]
model_name = LogisticRegression(solver='liblinear')  
model = GridSearchCV(model_name,param_grid=Lparams,scoring='f1',cv=5)
# model.fit(LX_train,LY_train)
model.fit(LX_train, LY_train.values.ravel())
print("Logistic Regression alpha",model.best_params_)
print("Logistic Regression score",model.best_score_)

y_pred_logis = model.predict(LX_test)
print("logistic predict",y_pred_logis)
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
confusion = confusion_matrix(LY_test,y_pred_logis)
accuracy = accuracy_score(LY_test,y_pred_logis)
classification = classification_report(LY_test,y_pred_logis)
print("confusion matrix logistic regression ",confusion)
print("accuracy scorelogistic regression ",accuracy)
print("classification report logistic regression ",classification)