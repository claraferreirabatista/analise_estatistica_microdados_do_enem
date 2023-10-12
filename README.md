# Projeto: Análise dos Microdados do Enem - Impacto da COVID-19 na Região Centro-Oeste

Visualise o nossos gráficos gerados:

[Análise dos Microdados do Enem](https://nbviewer.org/github/claraferreirabatista/analise_estatistica_microdados_do_enem/blob/main/analise_estatistica_dos_dados_enem.html)

## Membros

**[Clara Ferreira Batista](https://www.linkedin.com/in/clara-ferreira-batista/)**

**[Laura Muglia](https://www.linkedin.com/in/lauramuglia/)**

**[Luana Ferraz](https://www.linkedin.com/in/luanamariaferraz/)**

**[Rafael Couto de Oliveira](https://www.linkedin.com/in/couto21/)**

**Contexto da análise do trabalho:** Análise do impacto da COVID-19 nos números da região Centro-oeste referente aos anos de 2018 a 2022.

**Onde encontrar os dados:** [Dados do Enem - INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

**Bibliotecas Utilizadas:**
- Matplotlib (utilizada para visualizações)
- Pandas (utilizada para manipulação de dados)
- Numpy (utilizada para cálculos numéricos)
- Scipy (utilizada para análises estatísticas)
- Seaborn (utilizada para visualizações estatísticas)
- Plotly (utilizada para visualizações interativas)

**Resumo do Trabalho**

Este trabalho consiste na análise dos Microdados do Exame Nacional do Ensino Médio (ENEM) e seu objetivo principal é avaliar o impacto da pandemia da COVID-19 nos números da região Centro-Oeste, considerando o período de 2018 a 2022. Foram exploradas diversas variáveis, incluindo faixa etária dos inscritos, tipo de escola frequentada, presença nos exames, escolha de língua estrangeira, distribuição de notas, notas de redação e a influência da localização geográfica na escolha da língua estrangeira.

**Principais Insights e Resultados**

1. **Faixa Etária dos Inscritos:** A análise não encontrou uma concentração significativa de participantes em uma faixa etária específica, e a falta de amostras suficientes impediu a realização de um teste de normalidade. 

2. **Tipo de Escola:** A distribuição dos tipos de escola (pública e privada) nos últimos 5 anos mostrou uma mudança significativa, comprovada através de um teste de hipótese.

3. **Presença nos Exames:** A análise demonstrou que a quantidade de alunos ausentes nos exames variou ao longo dos anos, com um destaque para o aumento de ausências em 2020, possivelmente devido à pandemia.

4. **Escolha de Língua Estrangeira:** Houve uma queda acentuada na escolha da língua espanhola em comparação com a língua inglesa nos últimos anos, particularmente de 2020 a 2022.

5. **Impacto da Localização Geográfica na Escolha da Língua Estrangeira:** O teste de qui-quadrado mostrou que há uma relação estatisticamente significativa entre a localização do estado e a escolha de idioma.

6. **Distribuição de Notas:** A análise da distribuição das notas ao longo dos anos indicou um aumento na variação das notas a partir de 2020, com notas máximas e quartis superiores mais elevados. No entanto, o teste Kruskall-Wallis não demonstrou uma diferença significativa nas médias das notas entre os anos.

7. **Notas de Redação:** A análise das notas de redação ao longo dos anos revelou uma possível mudança significativa em relação à média geral das notas. O teste de Mann-Whitney confirmou que a nota média entre os anos de 2019 e 2020 variou de maneira estatisticamente significativa.

8. **Impacto da Pandemia nas Notas de Redação dos Alunos do Terceiro Ano:** A análise das notas de redação dos estudantes do terceiro ano demonstrou que suas médias de notas variaram ao longo dos anos, com sombreamentos de intervalos de confiança.

**Conclusão**

O trabalho fornece uma análise abrangente dos Microdados do ENEM e seu impacto na região Centro-Oeste, particularmente em relação à pandemia da COVID-19. Embora tenhamos observado variações estatísticas em algumas métricas, como a escolha de língua estrangeira e a distribuição de notas, é importante notar que a relação de causalidade entre a pandemia e essas mudanças requer uma investigação mais aprofundada. Além disso, a análise destaca a importância de uma abordagem estatística rigorosa na interpretação dos dados e ressalta a necessidade de continuar a monitorar e avaliar o impacto de eventos como a pandemia em futuras análises educacionais.

