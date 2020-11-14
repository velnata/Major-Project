import streamlit as st
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df=pd.read_table('/content/train.csv')
x =df.iloc[:,1].values #Message input
y = df.ilox[:,0].values#output message
st.title('Sentiment Analysis of Hotel-Review')
st.subheader('TFIDF Vectorization')
st.write('This project is based on Logistic Regression')

model = Pipeline([('vectorizer',tvec),('classifier',clf2)])
model.fit(IV_train, DV_train)
message= st.text_area("Enter the text")
op = model.predict([message])
if st.button("Predict"):
  st.title(op)