import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import preprocessor, helper
import plotly.express as px

# load/read data
cam_list = pd.read_csv('cam_list_3.0.csv')

# load preprocessor.py
cam_list = preprocessor.preprocess(cam_list)

# sidebar ui
st.sidebar.title('Military Coup De Tat Analysis')

# sidebar components
user_menu = st.sidebar.radio(
    'Select an Option', (
        'Successful Coups Per Country', 'Combat Per Country', 'Coups Per Region','Countries Where Military Coups Have Occurred', 
        'Region', 'SuccessFull Coups', 'Combat', 
    ))

if user_menu == 'Combat Per Country':
    st.title('Combat Per Country during Military Coups')
    cc = helper.CountryCombat(cam_list)
    st.table(cc)

if user_menu == 'Successful Coups Per Country':
    st.title('Successful Millitary Coups per Country')
    sc = helper.SuccessfulCountry(cam_list)
    st.table(sc)

if user_menu == 'Coups Per Region':
    st.title('Coups Per Region')
    rcp = helper.RegionPerCoup(cam_list)
    st.table(rcp)


if user_menu == 'Countries Where Military Coups Have Occurred':
    st.sidebar.header('Visualizations')
    
    selected_top_20 = st.sidebar.checkbox('Countplot')
    selected_top_pie = st.sidebar.checkbox('Pie Plot')
    selected_top_barh = st.sidebar.checkbox('Bar Plot')
    
    if selected_top_20:
        st.subheader('CountPlot visualization of the Number of Military Coups per Country')
        fig, ax = plt.subplots(figsize=(50,20))
        
        # plotting/visualization
        ax = sns.countplot(
        x='country',
        data=cam_list,
        order=cam_list['country'].value_counts().index[0:20])
    
        ax.set_xlabel('Country')
        ax.set_ylabel('No. of Military Coups per Country')
        ax.set_title('Visualization of the Number of Military Coups of the Top 20 Countries')
        st.pyplot(fig)
    
    elif selected_top_pie:
        st.subheader('Pie Plot visualization of the Number of Military Coups of the Top 10 Countries')
        fig, ax = plt.subplots(figsize=(40,10))
        
        ax = cam_list.country.value_counts()[:10].plot(
            kind='pie', autopct='%.2f%%', pctdistance=0.4, labeldistance=0.7, 
            explode=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
        ax.set_title('Pie Plot visualization of the Number of Military Coups per Country')
        st.pyplot(fig)
    
    elif selected_top_barh:
        st.subheader('Bar Plot visualization of the Number of Military Coups of the Top 10 Countries')
        fig, ax = plt.subplots(figsize=(50,20))
        
        ax = cam_list.country.value_counts()[:10].plot(
            kind='barh', color=['green','darkblue']
        )
        ax.set_title('Bar Plot visualization of the Number of Military Coups of the Top 10 Countries')
        st.pyplot(fig)
    
    else:
        st.title('Countries Where Military Coups Have Occurred')
        countries_occurred = helper.CountriesWhereMilitaryCoupsHaveOccured(cam_list)
        st.table(countries_occurred)

if user_menu == 'Region':
    st.sidebar.header('Visualizations')
    
    selected_top_countplot = st.sidebar.checkbox('Countplot')
    selected_top_pie = st.sidebar.checkbox('Pie Plot')
    selected_top_barh = st.sidebar.checkbox('Bar Plot')
    
    if selected_top_countplot:
        st.subheader('CountPlot visualization of the Number of Countries Per Region where Military Coups have Occurred')
        fig, ax = plt.subplots(figsize=(50,20))
        
        # plotting/visualization
        ax = sns.countplot(
            x='region',
            data=cam_list,
            order=cam_list['region'].value_counts().index[0:20]
            )
        ax.set_xlabel('region')
        ax.set_ylabel('Count of Military Coups Per Region')
        ax.set_title('Number of Countries Per Region where Military Coups have Occurred')
        st.pyplot(fig)
    
    elif selected_top_pie:
        st.subheader('Pie Plot visualization of the Number of Countries Per Region where Military Coups have Occurred')
        fig, ax = plt.subplots(figsize=(50,20))
        
        ax = cam_list.region.value_counts().plot(
            kind='pie', autopct='%.2f%%', pctdistance=0.4, labeldistance=0.7, explode=[0.01, 0.01, 0.01, 0.01, 0.01])
        
        ax.set_title('Pie Plot visualization of the Number of Countries Per Region where Military Coups have Occurred')
        st.pyplot(fig)
    
    elif selected_top_barh:
        st.subheader('Bar Plot visualization of the Number of Countries Per Region where Military Coups have Occurred')
        fig, ax = plt.subplots(figsize=(50,20))
        
        ax = cam_list.region.value_counts().plot(
            kind='barh', color=['green','darkblue']
        )
        ax.set_title('Bar Plot visualization of the Number of Countries Per Region where Military Coups have Occurred')
        st.pyplot(fig)
    
    else:
        st.title('Regions Where Military Coups have Occurred plus the Number of Countries in that Region')
        regi = helper.Region(cam_list)
        st.table(regi)

if user_menu == 'SuccessFull Coups':
    st.sidebar.header('Visualizations')
    
    selected_top_countplot = st.sidebar.checkbox('Countplot')
    selected_top_pie = st.sidebar.checkbox('Pie Plot')
    selected_top_barh = st.sidebar.checkbox('Bar Plot')
    
    if selected_top_countplot:
        st.subheader('CountPlot visualization of the Successful or Not Successful Military Coups')
        fig, ax = plt.subplots(figsize=(50,20))
        
        # plotting/visualization
        # Count Plot of successful coups

        ax = sns.countplot(
            x='successful',
            data=cam_list,
            order=cam_list['successful'].value_counts().index[0:2]
        )
        ax.set_xlabel('SuccessFul Coups')
        ax.set_ylabel('No. of coups')
        ax.set_title('Successful or Not Successful Military coups')
        
        st.pyplot(fig)
    
    elif selected_top_pie:
        st.subheader('Pie Plot visualization of the Total Number of Successful or Not Successful Military Coups')
        fig, ax = plt.subplots(figsize=(50,20))
        
        ax = cam_list.successful.value_counts().plot(
            kind='pie', autopct='%.2f%%', pctdistance=0.4, labeldistance=0.7, 
            explode=[0.01, 0.01], colors=['violet','green']
        )
        
        ax.set_title('Pie Plot visualization of the Total Number of Successful or Not Successful Military Coups')
        st.pyplot(fig)
    
    elif selected_top_barh:
        st.subheader('Bar Plot visualization of the Total Number of Successful or Not Successful Military Coups')
        fig, ax = plt.subplots(figsize=(50,20))
        
        ax = cam_list.successful.value_counts().plot(
            kind='barh', color=['green','darkblue']
        )
        
        ax.set_title('Bar Plot visualization of the Total Number of Successful or Not Successful Military Coups')
        st.pyplot(fig)
    
    else:
        st.title('Total Number of Successful or Not Successful Military Coups')
        sc = helper.SuccessfulCoups(cam_list)
        st.table(sc)

if user_menu == 'Combat':
    st.sidebar.header('Visualizations')
    
    selected_top_countplot = st.sidebar.checkbox('Countplot')
    selected_top_pie = st.sidebar.checkbox('Pie Plot')
    selected_top_barh = st.sidebar.checkbox('Bar Plot')
    
    if selected_top_countplot:
        st.subheader('CountPlot visualization of Combat during Military Coups')
        fig, ax = plt.subplots(figsize=(50,20))
        
        # plotting/visualization
        # Count Plot of combat during coups

        ax = sns.countplot(
            x='combat',
            data=cam_list,
            order=cam_list['combat'].value_counts().index[0:2]
        )
        ax.set_xlabel('combat or no combat')
        ax.set_ylabel('Count of combat during coups')
        ax.set_title('Combat during coups')
        
        st.pyplot(fig)
    
    elif selected_top_pie:
        st.subheader('Pie Plot visualization of Combat during Military Coups')
        fig, ax = plt.subplots(figsize=(50,20))
        
        ax = cam_list.combat.value_counts().plot(
            kind='pie', autopct='%.2f%%', pctdistance=0.4, 
            labeldistance=0.7, explode=[0.01, 0.01], colors=['yellow','green'])
        
        ax.set_title('Pie Plot visualization of Combat during Military Coups')
        
        st.pyplot(fig)
    
    elif selected_top_barh:
        st.subheader('Bar Plot visualization of Combat during Military Coups')
        fig, ax = plt.subplots(figsize=(50,20))
        
        ax = cam_list.combat.value_counts().plot(
            kind='barh', 
            color=['green','darkblue']
        )
        
        ax.set_title('Bar Plot visualization of Combat during Military Coups')
        st.pyplot(fig)
    
    else:
        st.title('Combat during Military Coups')
        co = helper.Combat(cam_list)
        st.table(co)