### Análise dos Resultados

**a) A rede aprendeu a classificar as avaliações?**
Sim. Devido à simplicidade e separabilidade do vocabulário gerado na base de treinamento, o Perceptron consegue ajustar a reta de decisão linearmente. O treinamento é interrompido antecipadamente quando o erro zera, resultando em uma acurácia de 100% sobre os dados conhecidos.

**b) Quantas avaliações foram classificadas incorretamente?**
Na base de testes (dados de treinamento), o modelo apresenta $0$ classificações incorretas. No entanto, ao aplicar o modelo às $5$ novas avaliações, é altamente provável que ele cometa 1 ou 2 erros, especialmente em frases ambíguas que misturam termos positivos e negativos (ex: "Arte fantástica, mas a história é muito fraca").

**c) Por que ocorreram os erros?**
Em previsões de novos dados, as falhas derivam fortemente das limitações do modelo *Bag of Words*. O modelo atua unicamente sobre a frequência das palavras, ignorando completamente a ausência de análise de contexto e a sintaxe da frase. Isso significa que ele não consegue interpretar ironias ou ambiguidades, somando pesos de palavras positivas (como "arte" e "fantástica") mesmo quando estão em uma avaliação que deveria ser negativa. Além disso, o tamanho reduzido da base (apenas 20 avaliações originais) resulta em um vocabulário pobre, não conseguindo mapear palavras com significado semelhante que não apareceram durante o treinamento.