import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np


st.set_page_config(layout='wide')

data=pd.read_csv('zameen-updated.csv')
data['date_added']=pd.to_datetime(data['date_added'])
data['country']='Pakistan'


st.sidebar.title('Zameen.com')

# Function for the data of entire country
def country():
    con=st.sidebar.selectbox('Select country',list(np.sort(np.append(data['country'].unique(),'-'))))
    if con == '-':
        data
    else:
        data[data['country']==con]


# Function to filter the data on the base of cities
def city():
    citys=st.sidebar.selectbox('Select City', list(np.sort(np.append(data['city'].unique(),'-'))))
    if citys=='-':
        city.data1=data
    else:
        city.data1=data[data['city']==citys]


# Function to fiter the data on the base of specific location in city
def location():
    data=city.data1
    loc=st.sidebar.selectbox('Select location',list(np.sort(np.append(data['location'].unique(),'-'))))
    if loc == '-':
        location.data2=city.data1
    else:
        location.data2=data[data['location']==loc]


# Function to filter the data on the base of Kanal and Marla
def area_type():
    data=location.data2
    a_t=st.sidebar.selectbox('Select Area Type', list(np.sort(np.append(data['Area Type'].unique(),'-'))))
    if a_t== '-':
        area_type.data3=location.data2
    else:
        area_type.data3=data[data['Area Type']==a_t]


# Function to filter data for sale and rent purpose
def purpose():
    data=area_type.data3
    pur=st.sidebar.selectbox('Select Purpose', list(np.sort(np.append(data['purpose'].unique(),'-'))))
    if pur== '-':
        purpose.data4=area_type.data3
    else:
        purpose.data4=data[data['purpose']==pur]


# Function to filter data on base of property type
def property_type():
    data=purpose.data4
    p_t=st.sidebar.selectbox('Select Property Type', list(np.sort(np.append(data['property_type'].unique(),'-'))))
    if p_t:
        property_type.data5=purpose.data4
    else:
        property_type.data5=data[data['property_type']==p_t]

country()
city()
location()
area_type()
purpose()
property_type()




plot = st.sidebar.button('Plot Graph')
if plot:
    fig = px.scatter_mapbox(property_type.data5, lat="latitude", lon="longitude",color='province_name',
                        zoom=4, size_max=35,mapbox_style="carto-positron", width=1200, height=700, hover_name='city')

    st.plotly_chart(fig, use_container_width=True)

st.sidebar.write(' ')
st.sidebar.write(' ')
st.sidebar.write('Contact us for Data Science ,Data Collection and Data Visualization Services')
st.sidebar.subheader('WhatsApp')
st.sidebar.code('03269189901')
st.sidebar.subheader('Email')
st.sidebar.code('asaddevaloper2252@gmail.com')