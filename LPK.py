import streamlit as st

Soal = st.selectbox(
    'Pilih soal',
    ('Soal 1', 'Soal 2', 'Soal 3'))
if Soal == "Soal 1":
    st.write("titran pada standardisasi alkalimetri adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1 = st.button("HCL")
        opsi2 = st.button("KMNO4")
    with col2:
        opsi3 = st.button("AgNO3")
        opsi4 = st.button("NaOH")
    if opsi1:
        st.write("Salah")
    elif opsi2:
        st.write("Salah")
    elif opsi3:
        st.write("salah")
    elif opsi4:
        st.write("Benar")
        st.balloons()
elif soal == "Soal 2":
    st.write("indikator dalam standardisasi NaOH adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("SM")
        opsi2= st.button("MM")
    with col2:
        opsi3= st.button("PP")
        opsi4= st.button("fenolftalein")
    if opsi1:
        st.write("salah")
    elif opsi2:
        st.write("salah")
    elif opsi3:
        st.write("benar")
        st.balloons()
    elif opsi4:
        st.write("salah")
elif soal == "Soal 3":
    st.write("Alkil halida-alkil halida yang dapat digunakan untuk membuat 2-metil-3-siklobutilpentana dengan cara Corey-House adalah(alkil halida sesuai tahapannya)...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("1-bromo-1-siklobutilpropana dan 2-bromopropana")
        opsi2= st.button("Metilbromida dan 2-bromo-3-siklobutilpentana")
    with col2:
        opsi3= st.button("2-bromo-3-siklobutilpentana dan metilbromida")
        opsi4= st.button("2-bromopropana dan 1-bromo-1-siklopropilpropana")
    if opsi1:
        st.write("salah")
    elif opsi2:
        st.write("salah")
    elif opsi3:
        st.write("benar")
        st.balloons()
    elif opsi4:
        st.write("salah") 
        
if soal == "Soal 4":
    st.write("Campuran reagen berikut yang menghasilkan reagen uji Tollens adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("AgNO3 + NaOH + NH4OH")
        opsi2= st.button("Etanol + Air + HCl")
    with col2:
        opsi3= st.button("CuSO4 + NaOH + NaK-Tartrat")
        opsi4= st.button("CuSO4 + Na2CO3")
    if opsi1:
        st.write("benar")
    elif opsi2:
        st.write("salah")
    elif opsi3:
        st.write("salah")
        st.balloons()
    elif opsi4:
        st.write("salah")
