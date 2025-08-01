# -*- coding: utf-8 -*-
"""WINE_QUALITY.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Vgr3f5LYElEsG8Bj00BMmDqTYoEDPdQ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

from google.colab import files
uploaded = files.upload()

import io

wine_data = pd.read_csv(io.BytesIO(uploaded['winequality-red.csv']))
wine_data.head()

wine_data.isnull().sum()

print(f"The shape of the dataset is {wine_data.shape}")
print(f"The size of the dataset is {len(wine_data)}")

wine_data.describe()

wine_data.info()

plt.scatter(wine_data["fixed acidity"], range(0,len(wine_data)))

wine_data["fixed acidity"].plot(kind="hist")

plt.figure(figsize=(20,7))
sns.heatmap(wine_data.corr(),annot=True)

"""### Preprocessing the data"""

wine_data.columns[:-1]

from sklearn.preprocessing import MinMaxScaler
minmaxscaler = MinMaxScaler()

minmaxscaler.fit(wine_data[wine_data.columns[:-1]])

scaled = minmaxscaler.transform(wine_data[wine_data.columns[:-1]])
scaled

scaled_data = pd.DataFrame(scaled, columns=wine_data.columns[:-1])
scaled_data.head()

### The quality

def resolve_quality(value):
  if value>=6:
    return 1
  else:
    return 0

quality = wine_data["quality"].apply(lambda x: resolve_quality(x))

quality = pd.DataFrame(quality)
quality.head()

wine_data_preprocessed = pd.concat([scaled_data, quality],axis=1)
wine_data_preprocessed.head()

"""### Train Test Split"""

from sklearn.model_selection import train_test_split

X = wine_data_preprocessed.drop("quality",axis=1)
y = wine_data_preprocessed["quality"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

print(f"The length of X_train is {len(X_train)} and the length of y_train is {len(y_train)}")
print(f"The length of x_test is {len(X_test)} and the length of y_Test is {len(y_test)}")

"""#### HELPER FUNCTION FOR ACCURACY CHECKK"""

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
def evaluate_model(y_test, predictions):
  print("The confucion Matrix - ")
  print(confusion_matrix(y_test,predictions))
  print('\n')

  print("Classification report - ")
  print(classification_report(y_test,predictions))
  print('\n')

  print("Accuracy Score - ")
  print(accuracy_score(y_test,predictions))
  print('\n')

"""# 1.Logistic Regression Model - 72.083 % Accuracy

"""

from sklearn.linear_model import LogisticRegression

log_model = LogisticRegression()

log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)

evaluate_model(y_test, log_preds)

len(log_preds)

"""# Decission Tree Model - 75.625"""

from sklearn.tree import DecisionTreeClassifier

dtree_classifier = DecisionTreeClassifier()
dtree_classifier.fit(X_train,y_train)

dtree_preds = dtree_classifier.predict(X_test)

evaluate_model(y_test, dtree_preds)

"""# Random Forest Model - 81%"""

from sklearn.ensemble import RandomForestClassifier

rnd_clf = RandomForestClassifier(n_estimators=500,max_leaf_nodes=16,n_jobs=-1)
rnd_clf.fit(X_train, y_train)

rnd_preds = rnd_clf.predict(X_test)

evaluate_model(y_test, rnd_preds)

#Without unwanted hyperparameters
rnd_clf_2 = RandomForestClassifier(n_estimators=500)
rnd_clf_2.fit(X_train, y_train)
rnd_preds_2 = rnd_clf_2.predict(X_test)

evaluate_model(y_test, rnd_preds_2)

# less estimators
rnd_3 = RandomForestClassifier(n_estimators=128)
rnd_3.fit(X_train, y_train)
rnd_3_preds = rnd_3.predict(X_test)

evaluate_model(y_test, rnd_3_preds)

"""#### Now with even lesser number of estimatorrs"""

rnd_4 = RandomForestClassifier(n_estimators=64)
rnd_4.fit(X_train, y_train)
rnd_4_preds = rnd_4.predict(X_test)

evaluate_model(y_test, rnd_4_preds)

"""###### last expiriment with lots of estimators"""

rnd_5 = RandomForestClassifier(n_estimators=2000)
rnd_5.fit(X_train, y_train)
rnd_5_preds = rnd_5.predict(X_test)

evaluate_model(y_test, rnd_5_preds)

"""### MODEL 3 IS OUR BESTT MODEL

# USING DEEP LEARNING

### NEURAL NETWORK CLASSIFICATION MODEL - 75%
"""

# Set the random seed
tf.random.set_seed(42)

# Create the Model
model_1 = tf.keras.Sequential([
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1,activation="relu")
])

# Compile the model
model_1.compile(loss=tf.keras.losses.binary_crossentropy,
                optimizer=tf.keras.optimizers.SGD(),
                metrics=["accuracy"])

# Fit in the model
history_1 = model_1.fit(X_train,
                        y_train,
                        epochs=100)

model_1_preds = model_1.predict(X_test)
model_1.evaluate(X_test, y_test)

model_2 = tf.keras.Sequential([
    tf.keras.layers.Dense(100,activation="relu"),
    tf.keras.layers.Dense(10 ,activation="relu"),
    tf.keras.layers.Dense(1  ,activation="sigmoid")
])

model_2.compile(loss=tf.keras.losses.binary_crossentropy,
                optimizer=tf.keras.optimizers.Adam(lr='0.001'),
                metrics=["accuracy"])

history_2 = model_2.fit(X_train, y_train, epochs=100)

model_2.evaluate(X_test, y_test)

## Making a more complex model
model_3 = tf.keras.Sequential([
    tf.keras.layers.Dense(100,activation="relu"),
    tf.keras.layers.Dense(50,activation="relu"),
    tf.keras.layers.Dense(10,activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

model_3.compile(loss=tf.keras.losses.binary_crossentropy,
                optimizer=tf.keras.optimizers.Adam(lr='0.001'),
                metrics=["accuracy"])

history_3 = model_3.fit(X_train,
                        y_train,
                        epochs=300,
                        batch_size=32)

model_3.evaluate(X_test, y_test)

