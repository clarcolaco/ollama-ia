import ollama
import time
if __name__ =='__main__':
    
    
    response = ollama.chat(model="llama3.1",messages=[{'role': 'user','content': 'O que é cachorro? resumidamente'}]) 

    print("...gerando sua mensagem..")
    time.sleep(1)
    
    print(f"Resposta: {response['message']['content']}")
