import pandas as pd
import string
import re

def preprocess_jaccard(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return set(text.split())

def preprocess_levenshtein(text):
    text = str(text).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return re.sub(r'\s+', ' ', text).strip()

def jaccard(set1, set2):
    intersecao = len(set1.intersection(set2))
    uniao = len(set1.union(set2))
    return intersecao / uniao if uniao != 0 else 0

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    linha_anterior = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        linha_atual = [i + 1]
        for j, c2 in enumerate(s2):
            insercoes = linha_anterior[j + 1] + 1
            delecoes = linha_atual[j] + 1
            substituicoes = linha_anterior[j] + (c1 != c2)
            linha_atual.append(min(insercoes, delecoes, substituicoes))
        linha_anterior = linha_atual
        
    return linha_anterior[-1]

def classificar_avaliacoes(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    
    ref_pos = "O produto possui excelente qualidade, chegou rapidamente e atendeu completamente às minhas expectativas. Gostei muito da compra e recomendo este produto para outras pessoas."
    ref_neg = "O produto possui péssima qualidade, apresentou problemas logo após a compra e não atendeu às minhas expectativas. Fiquei muito decepcionado e não recomendo este produto."
    
    set_pos = preprocess_jaccard(ref_pos)
    set_neg = preprocess_jaccard(ref_neg)
    str_pos = preprocess_levenshtein(ref_pos)
    str_neg = preprocess_levenshtein(ref_neg)
    
    jaccard_pos_list, jaccard_neg_list, class_jaccard_list = [], [], []
    lev_pos_list, lev_neg_list, class_lev_list = [], [], []
    
    for _, row in df.iterrows():
        texto = row['avaliacao']
        
        # Similaridade de Jaccard
        s = preprocess_jaccard(texto)
        jp = jaccard(s, set_pos)
        jn = jaccard(s, set_neg)
        cj = 'POSITIVA' if jp > jn else 'NEGATIVA'
        
        jaccard_pos_list.append(round(jp, 4))
        jaccard_neg_list.append(round(jn, 4))
        class_jaccard_list.append(cj)
        
        # Distância de Levenshtein
        txt = preprocess_levenshtein(texto)
        lp = levenshtein(txt, str_pos)
        ln = levenshtein(txt, str_neg)
        cl = 'POSITIVA' if lp < ln else 'NEGATIVA'
        
        lev_pos_list.append(lp)
        lev_neg_list.append(ln)
        class_lev_list.append(cl)
        
    df['Jaccard Pos.'] = jaccard_pos_list
    df['Jaccard Neg.'] = jaccard_neg_list
    df['Class. Jaccard'] = class_jaccard_list
    df['Lev. Pos.'] = lev_pos_list
    df['Lev. Neg.'] = lev_neg_list
    df['Class. Lev.'] = class_lev_list
    
    return df

if __name__ == "__main__":
    df_resultados = classificar_avaliacoes("avaliacoes (1).xlsx")
    df_resultados.to_excel("resultados_classificacao.xlsx", index=False)