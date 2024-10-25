# import streamlit as st
# import ollama
# import time
# if __name__ =='__main__':
    
#     # Título da aplicação
#     st.title("Aplicação de Perguntas Dinâmicas")

#     # Input do usuário
#     pergunta = st.text_input("Digite sua pergunta:")

#     # Exibe a pergunta conforme o usuário digita

#     # Defina uma resposta automática para exibir com a pergunta
#     if pergunta:
#         response = ollama.chat(model="llama3.1",messages=[{'role': 'user','content': pergunta}]) 
#         st.write("...gerando sua mensagem..")
#         time.sleep(1)
#         resposta = f"Resposta: {response['message']['content']}"
#         st.write(f"Resposta: {resposta}")

import streamlit as st
import subprocess
import json

# Função para chamar o modelo do Ollama via subprocess
def perguntar_ollama(pergunta):
    # Comando para fazer a consulta ao modelo no Ollama
    command = ['ollama', 'generate', '--model', 'llama2', '--prompt', pergunta]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    
    # Processa a resposta do Ollama
    resposta = result.stdout
    return resposta

# Título da aplicação
st.title("Integração com Ollama no Streamlit")

# Input do usuário
pergunta = st.text_input("Digite sua pergunta:")

# Exibe a pergunta e chama o modelo Ollama para gerar a resposta
if pergunta:
    st.write(f"Pergunta: {pergunta}")
    
    # Chama a função para obter a resposta do Ollama
    resposta = perguntar_ollama(pergunta)
    
    # Exibe a resposta
    st.write(f"Resposta: {resposta}")