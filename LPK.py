import streamlit as st
import time
import streamlit as st
import streamlit as st
from PIL import Image
st.title('LPK kuyy!')
st.header('Kelompok 3')
st.subheader('1A')
image = Image.open('IMG_20230506_184224.jpg')

st.image(image, caption='STEVANNY A.S,LULU LUTHFI H.A,EKKE ROSE M.,KANIA MIEILANI,PANDAN TSIQQA A.')

with st.spinner('Wait for it 01.00'):
    time.sleep(5)
st.success('selamat mengerjakan!')

import streamlit as st

st.header('QUIZ Analisis Titrimetri & kimia Organik')
st.caption('yuk belajaR')

score = 0

questions = ("Titran pada standarisasi alkalimetri adalah...",
             "Indikator dalam standarisasi NaOH adalah...")
             
options = (("A.HCL","B.KMnO4","C.AgNO3","D.NaOh"),
          ("A.SM","B.MM","C.PP","D.BTB"))
          
answers = ("D","C")
guesses = []
score = 0
question_num = 0
        
for question in questions:
          tombol = st.button("next")
          print(question)
          for option in options[question_num]:
              print(option)
              
          answer = input("Enter(A,B,C,D):").upper()
          guesses.append(guess)
          if guess == answers [question_num]:
              score += 1
              print ("BENAR!")
          else: 
              print ("SALAH!")
              print(f"{answers[question_num]} adalah jawaban yang benar!")
          question_num += 1
