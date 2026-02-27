import pandas as pd
import numpy as np

def gerar_dados_sac(n=300):
    # Criando o dicionário com as colunas exigidas na Atividade_03.py
    data = {
        'qtd_exclamacao': np.random.randint(0, 10, n),
        'tem_palavra_alerta': np.random.choice([0, 1], n),
        'tamanho_msg': np.random.randint(20, 500, n),
        'rotulo': [] # 1: Alta Prioridade, 0: Comum
    }
    
    for i in range(n):
        # Regras ocultas para a Árvore de Decisão descobrir
        alerta = data['tem_palavra_alerta'][i]
        exclamacoes = data['qtd_exclamacao'][i]
        tamanho = data['tamanho_msg'][i]
        
        # Lógica: É Alta Prioridade (1) se tiver palavra de alerta E (mais de 2 exclamações OU mensagem longa)
        # OU se tiver um número extremo de exclamações.
        if alerta == 1 and exclamacoes > 2:
            data['rotulo'].append(1)
        elif alerta == 1 and tamanho > 300:
            data['rotulo'].append(1)
        elif exclamacoes > 6:
            data['rotulo'].append(1)
        else:
            data['rotulo'].append(0)
            
    return pd.DataFrame(data)

# Gerando o arquivo para a aula
df = gerar_dados_sac(500) # Gerando 500 linhas para dar uma boa base de treino
df.to_csv('dados_sac.csv', index=False)
print("Dataset 'dados_sac.csv' gerado com sucesso!")