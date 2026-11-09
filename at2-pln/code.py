import random
import re

# 1. CRIAÇÃO DA BASE DE DADOS (20 avaliações)
avaliacoes = [
    ("O quadrinho possui uma história incrível e os desenhos são excelentes", 1),
    ("A história é muito fraca e a qualidade do quadrinho deixou a desejar", 0),
    ("Personagens fantásticos e roteiro muito divertido", 1),
    ("Achei a leitura cansativa e o final previsível", 0),
    ("Arte maravilhosa e enredo envolvente recomendo muito", 1),
    ("Decepcionante os diálogos são ruins e a arte é feia", 0),
    ("Uma obra prima dos quadrinhos superou minhas expectativas", 1),
    ("Não gostei a trama é confusa e sem sentido", 0),
    ("Excelente desenvolvimento de personagens muito bom", 1),
    ("Péssimo investimento história entediante", 0),
    ("Ação do começo ao fim leitura empolgante", 1),
    ("Muito chato abandonei na metade", 0),
    ("Traços belíssimos e cores vibrantes amei", 1),
    ("Edição mal feita folhas caindo e impressão ruim", 0),
    ("Roteiro genial uma das melhores HQs que já li", 1),
    ("Falta criatividade história clichê", 0),
    ("Muito divertido me fez rir bastante", 1),
    ("Não vale o preço conteúdo muito raso", 0),
    ("Surpreendente a reviravolta no final é incrível", 1),
    ("Total perda de tempo muito ruim", 0)
]

# 2. PRÉ-PROCESSAMENTO DOS TEXTOS
stopwords = {"o", "a", "os", "as", "um", "uma", "e", "é", "são", "do", "da", "de", "que", "muito", "na", "no", "dos", "das"}

def pre_processar(texto):
    texto = texto.lower() # Converter para minúsculas
    texto = re.sub(r'[^\w\s]', '', texto) # Remover pontuação
    palavras = texto.split() # Separar em palavras
    return [p for p in palavras if p not in stopwords] # Remover stopwords

# 3. TRANSFORMAÇÃO DOS TEXTOS EM NÚMEROS (Bag of Words)
vocabulario = set()
avaliacoes_processadas = []

for texto, classe in avaliacoes:
    palavras_limpas = pre_processar(texto)
    avaliacoes_processadas.append((palavras_limpas, classe))
    vocabulario.update(palavras_limpas)

vocabulario = list(vocabulario)

def text_to_bow(palavras_limpas, vocab):
    return [1 if palavra in palavras_limpas else 0 for palavra in vocab]

X = [text_to_bow(p, vocabulario) for p, _ in avaliacoes_processadas]
y = [c for _, c in avaliacoes_processadas]

# 4. IMPLEMENTAÇÃO DO PERCEPTRON
random.seed(42)
pesos = [random.uniform(-0.1, 0.1) for _ in range(len(vocabulario))]
bias = random.uniform(-0.1, 0.1)
taxa_aprendizagem = 0.1
epocas = 100

def ativacao(soma):
    return 1 if soma > 0.5 else 0

# 5. TREINAMENTO
for epoca in range(epocas):
    erros_epoca = 0
    for i in range(len(X)):
        entrada = X[i]
        classe_real = y[i]
        
        # Cálculo da soma ponderada
        soma = bias
        for j in range(len(entrada)):
            soma += entrada[j] * pesos[j]
            
        classe_prevista = ativacao(soma)
        erro = classe_real - classe_prevista
        
        # Atualização dos pesos (apenas se houver erro)
        if erro != 0:
            erros_epoca += 1
            bias += taxa_aprendizagem * erro
            for j in range(len(entrada)):
                pesos[j] += taxa_aprendizagem * erro * entrada[j]
                
    if erros_epoca == 0:
        print(f"Treinamento concluído antecipadamente na época {epoca+1} (Erro zero)\n")
        break

# 6 e 7. TESTE DO MODELO E CÁLCULO DA PORCENTAGEM DE ACERTO
print("--- TESTE DO MODELO (BASE ORIGINAL) ---")
corretas = 0
for i, (texto, classe_real) in enumerate(avaliacoes):
    entrada = text_to_bow(pre_processar(texto), vocabulario)
    soma = bias + sum(entrada[j] * pesos[j] for j in range(len(entrada)))
    classe_prevista = ativacao(soma)
    
    if classe_prevista == classe_real:
        corretas += 1
        resultado = "ACERTO"
    else:
        resultado = "ERRO"
        
    print(f"Classe Real: {classe_real} | Prevista: {classe_prevista} | {resultado} -> {texto}")

acuracia = (corretas / len(avaliacoes)) * 100
print(f"\nTotal de avaliações: {len(avaliacoes)}")
print(f"Classificações corretas: {corretas}")
print(f"Classificações incorretas: {len(avaliacoes) - corretas}")
print(f"Acurácia: {acuracia:.2f}%\n")

# 8. TESTE COM NOVAS AVALIAÇÕES
novas_avaliacoes = [
    ("História envolvente e arte excelente", 1),
    ("Leitura chata, não recomendo a ninguém", 0),
    ("Diálogos geniais, adorei", 1),
    ("Péssima qualidade, rasgou fácil", 0),
    ("Arte fantástica, mas a história é muito fraca", 0) # Teste de ambiguidade
]

print("--- TESTE COM NOVAS AVALIAÇÕES ---")
for texto, classe_real in novas_avaliacoes:
    entrada = text_to_bow(pre_processar(texto), vocabulario)
    soma = bias + sum(entrada[j] * pesos[j] for j in range(len(entrada)))
    classe_prevista = ativacao(soma)
    resultado = "ACERTO" if classe_prevista == classe_real else "ERRO"
    print(f"Real: {classe_real} | Prev: {classe_prevista} | {resultado} -> {texto}")