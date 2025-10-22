import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
st.title('World Cities')
df=pd.read_csv('worldcities.csv')
population_filter=st.slider('Minimal Population (Million):',0.0,48.0,3.6)
capital_filter=st.sidebar.multiselect('Capital Selector',df.capital.unique(),df.capital.unique())
form=st.sidebar.form('country_form')
country_filter=form.text_input('Country Name(enter All to reset)','All')
form.form_submit_button('Apply')
df=df[df.population>=population_filter]
df=df[df.capital.isin(capital_filter)]
if country_filter!='All':
    df=df[df.country==country_filter]
st.map(df)
st.subheader('City Details:')
st.write(df[['city', 'country', 'population']])
st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)