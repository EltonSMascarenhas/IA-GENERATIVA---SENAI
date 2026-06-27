# procoding 
# vou  usar a biblioteca
import streamlit as st

st.title('CALCULADORA...')

n1  = st.number_input('numero:', )
n2  = st.number_input('numero:', value = 0.0)

soma, sub, div, mult = st.columns(4)

if soma.button('Soma'):
    calcular   =  n1  + n2 
    st.success(calcular)
elif sub.button('subtração'):    
    calcular   =  n1  - n2 
    st.success(calcular)    
elif div.button('Divisão'):    
    calcular   =  n1  / n2 
    st.success(calcular)       
elif mult.button('Multiplicação'):    
    calcular   =  n1  * n2 
    st.success(calcular)      


#-------------------------------------------------------------------------------

st.title('Desafio 1: O Cartão de Visitas Digital')

st.header('Cartão de Visita')

st.text('Isso é um texto')

st.markdown('Este é o paragrafo do comentario')


#-------------------------------------------------------------------------------

st.title('Desafio 2: Formulario de Cadastro de Usuário')

nome = st.text_input ('Escreva seu nome')
idade = st.number_input ('Digite a sua Idade', value = 0)

aceito = st.checkbox('Aceito os termos')

if aceito:
    #st.write('')
    if st.button('Enviar Formulario'):
        st.success('dados enviados com Sucesso...')
        
           
#--------------------------------------------------------------------------------

st.title ('Desafio 3: Seletor de Cursos')

#st.text ()
nome = st.text_input('Nome Completo')
idade = st.number_input('Digite a sua idade', value=0)    
