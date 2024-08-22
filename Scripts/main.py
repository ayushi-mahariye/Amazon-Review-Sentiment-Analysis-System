import streamlit as st
import pandas as pd
import plotly.express as px
from google_auth_oauthlib.flow import InstalledAppFlow
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googleapiclient.discovery import build
mymodel=SentimentIntensityAnalyzer()
st.set_page_config(page_title="Amazon Review Analysis System",page_icon="https://st4.depositphotos.com/5266903/21366/v/450/depositphotos_213664560-stock-illustration-emotion-charts-flat-icon.jpg")

st.sidebar.image("https://cdn.brandmentions.com/blog/wp-content/uploads/2019/05/sentiment-analysys-brandmentions.png")
choice=st.sidebar.selectbox("My Menu",("Home","Analyze Sentiment","Visualize the Result"))
if(choice=="Home"):
    st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>AMAZON REVIEW SENTIMENT ANALYSIS SYSTEM </b></p>',unsafe_allow_html=True)

    st.image("https://miro.medium.com/v2/1*_JW1JaMpK_fVGld8pd1_JQ.gif")


elif(choice=="Analyze Sentiment"):
     st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>ANALYZE SENTIMENT</b></p>',unsafe_allow_html=True)

     url=st.text_input("Enter Google Sheet URL")
     r=st.text_input("Enter Range")
     c=st.text_input("Enter Column")
     btn=st.button("Analyze")
     if btn:
         if 'cred' not in st.session_state:
            f=InstalledAppFlow.from_client_secrets_file('Key.json',['https://www.googleapis.com/auth/spreadsheets'])
            st.session_state['cred']=f.run_local_server(port=0)
         service=build('Sheets','v4',credentials=st.session_state['cred']).spreadsheets().values()
         #Retreive the data from Google Sheets.
         d=service.get(spreadsheetId=url,range=r).execute()
         mycolumns=d['values'][0]
         mydata=d['values'][1:]
         df=pd.DataFrame(data=mydata,columns=mycolumns)
         l=[]
         for i in range(0,len(df)):
             k=df._get_value(i,c)
             pred=mymodel.polarity_scores(k)
             if(pred['compound']>0.5):
                 l.append("positive")
             elif(pred['compound']<-0.5):
                 l.append("Negative")
             else:
                 l.append("Neutral")
         df['Sentiment']=l
         st.dataframe(df)
         df.to_csv("Review3.csv",index=False)
         st.header("This data has been saved by the name of review.csv")
elif(choice=="Visualize the Result"):
     st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>VISUALIZE THE RESULT</b></p>',unsafe_allow_html=True)

     choice2=st.selectbox("Choose Visualization",("None","Pie","Histogram"))
     if(choice2=="Pie"):
         st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>Pie Chart</b></p>',unsafe_allow_html=True)
         df=pd.read_csv("Review3.csv")
         posper=len(df[df['Sentiment']=='Positive'])/len(df)*100
         negper=len(df[df['Sentiment']=='Negative'])/len(df)*100
         neuper=len(df[df['Sentiment']=='Neutral'])/len(df)*100
         fig=px.pie(values=[posper,negper,neuper],names=['Positive','Negative','Neutral'])
         st.plotly_chart(fig)
     elif(choice2=="Histogram"):
          st.markdown('<p style="font-family:serif; color:#FFFFFF;font-size:40px;text-align:center;text-decoration: underline;"><b>Histogram</b></p>',unsafe_allow_html=True)

          t=st.text_input("Chooose any Categorical Column")
          if t:
              df=pd.read_csv("Review3.csv")
              fig=px.histogram(x=df['Sentiment'],color=df[t])
              st.plotly_chart(fig)



