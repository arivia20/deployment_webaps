import streamlit as st

Soal = st.selectbox(
    'Pilih soal',
    ('Soal 1', 'Soal 2', 'Soal 3'))
if Soal == "Soal 1":
    st.write("titran dari standardisasi NaoH adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1 = st.button("NaoH")
        opsi2 = st.button("HCL")
    with col2:
        opsi3 = st.button("AgNO3")
        opsi1 = st.button("KMNO4")
    if opsi1:
        st.write("benar")
        st.balloons()
    elif opsi2:
        st.write("Salah")
    elif opsi3:
        st.write("salah")
        st.balloons()
    elif opsi1:
        st.write("Salah")
   
