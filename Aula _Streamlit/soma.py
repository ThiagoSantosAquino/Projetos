import streamlit as st

'''
#programar para calcular o indice de massa corportal

Digite dois números para realizar a soma
'''

with st.form('Calcular'):
    n1 = st.number_input('Digite o valor da sua altura')
    n2 = st.number_input('Digite o valor de dua massa corporal')
    button = st.form_submit_button('Calcular')

imc = (n2/(n1*n1))

if button:
    st.write(f'Seu IMC atual é :{imc} !')
    if imc>=25 and imc<= 29:
       st.write("Voce está como o peso ideal")
    elif imc>=30:
       st.write('Você encontra-se com sobrepeso. Consulte um Endocrinologista!')
    else:
       st.write('Você está Subnutrido!')

