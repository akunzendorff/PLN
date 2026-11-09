### Análise dos Resultados

1. **Quantas avaliações foram classificadas como positivas pela métrica de Jaccard?**
29 avaliações.

2. **Quantas avaliações foram classificadas como negativas pela métrica de Jaccard?**
71 avaliações.

3. **Quantas avaliações foram classificadas como positivas pela distância de Levenshtein?**
43 avaliações.

4. **Quantas avaliações foram classificadas como negativas pela distância de Levenshtein?**
57 avaliações.

5. **Em quantas avaliações as duas métricas produziram a mesma classificação?**
66 avaliações.

6. **Em quantas avaliações as métricas produziram classificações diferentes?**
34 avaliações.

7. **Por que Jaccard e Levenshtein podem produzir resultados diferentes para uma mesma avaliação?**
A similaridade de Jaccard baseia-se em conjuntos de palavras soltas (bag-of-words), verificando apenas a presença ou ausência de termos em comum. Ela ignora completamente a ordem das palavras, a estrutura da frase e o tamanho total do texto. A distância de Levenshtein atua no nível dos caracteres de toda a string. Ela é altamente dependente da ordem das palavras e do comprimento do texto. Uma avaliação com as mesmas palavras da referência, mas em ordem totalmente alterada, terá uma alta pontuação em Jaccard (alta semelhança), mas também uma alta distância de Levenshtein (baixa semelhança devido aos deslocamentos de caracteres).

8. **Qual das duas métricas apresentou maior sensibilidade às diferenças entre os textos? Justifique sua resposta com base nos resultados obtidos.**
A distância de Levenshtein apresentou maior sensibilidade estrutural, pois penaliza severamente qualquer alteração de ordem, inserção de espaços extras ou uso de sinônimos com extensões de caracteres diferentes. Jaccard apresentou uma maior sensibilidade de vocabulário, agindo de forma mais rigorosa na classificação final (classificando 71 avaliações como negativas contra as 57 de Levenshtein). Para o contexto de análise de sentimento e avaliações, Jaccard captura melhor a proximidade semântica ao focar nas palavras-chave exatas ("excelente", "péssima", "recomendo") e ignorar a formatação ou ordem em que o cliente as escreveu.