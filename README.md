# E-commerce em Dados | Análise de Vendas Globais — 2025

## 1. Sobre o projeto

Este projeto apresenta uma solução de Business Intelligence (BI) desenvolvida em Python para analisar dados de vendas de e-commerce em diferentes países e categorias de produtos ao longo de 2025.

A solução contempla um pipeline de Extração, Transformação e Carregamento (ETL), Análise Exploratória de Dados (EDA) e um dashboard interativo desenvolvido com Streamlit.

O objetivo é transformar registros de transações em indicadores e visualizações que apoiem a interpretação do desempenho comercial.

## 2. Problema e objetivo

**Pergunta orientadora:**

Como o faturamento das transações de e-commerce registradas em 2025 varia entre países, categorias de produtos e períodos, e quais segmentos apresentam maior participação financeira?

**Objetivo geral:** analisar a distribuição do faturamento e identificar padrões relevantes nas transações disponíveis.

**Público-alvo:** analistas de dados, profissionais de inteligência comercial e gestores interessados em indicadores de vendas.

**Relevância:** o acompanhamento de faturamento, volume de pedidos e ticket médio pode apoiar análises comerciais e a identificação de segmentos que merecem investigação.

## 3. Escopo

A análise contempla:

- Faturamento total;
- Quantidade de pedidos;
- Unidades vendidas;
- Ticket médio;
- Faturamento por país;
- Faturamento por categoria;
- Evolução mensal do faturamento.

O projeto não contempla custos, margens de lucro, identificação de clientes, previsão de vendas ou avaliação de causalidade.

## 4. Fonte dos dados

- **Dataset:** Global E-Commerce Sales Dataset (2025)
- **Publicador:** kojibrand
- **Plataforma:** Kaggle
- **Link:** https://www.kaggle.com/datasets/kojibrand/global-e-commerce-sales-dataset-2025
- **Licença informada:** Creative Commons CC0 1.0
- **Método de obtenção:** download de arquivo CSV
- **Arquivo original:** `global_ecommerce_sales.csv`
- **Data de acesso:** 10/11/2026

A base utilizada possui 1.200 registros e sete colunas originais: `Order_ID`, `Country`, `Category`, `Unit_Price`, `Quantity`, `Order_Date` e `Total_Amount`.

Os registros analisados abrangem o período de 01/01/2025 a 01/11/2025. O mês de novembro possui cobertura parcial.

A licença CC0 foi informada para a base e deve ser conferida na página original do Kaggle.

## 5. Metodologia e pipeline

### Extração

Os dados foram obtidos por download do arquivo CSV disponibilizado no Kaggle e armazenados na pasta `dados/brutos`.

### Transformação

O script `scripts/tratamento_dados.py` realiza:

- Leitura dos dados com Pandas;
- Verificação de valores ausentes e registros duplicados;
- Padronização dos nomes das colunas;
- Conversão da coluna de datas;
- Tradução e padronização de países e categorias;
- Criação das variáveis `ano`, `mes` e `ano_mes`.

A inspeção inicial identificou 1.200 registros, sem valores ausentes ou linhas duplicadas. A categoria `Home Decor` foi mantida com sua denominação original.

### Carregamento

Após o tratamento, o arquivo é salvo em `dados/tratados/vendas_tratadas.csv`, utilizado nas etapas de análise e visualização.

### Análise exploratória

O script `scripts/analise_exploratoria.py` calcula indicadores gerais e realiza agrupamentos por país, categoria e mês.

As visualizações foram construídas com Plotly e disponibilizadas em uma aplicação Streamlit.

## 6. Principais resultados

| Indicador | Resultado |
|---|---:|
| Faturamento total | US$ 1.512.252,98 |
| Pedidos | 1.200 |
| Unidades vendidas | 6.008 |
| Ticket médio | US$ 1.260,21 |

**País com maior faturamento:** Estados Unidos, com US$ 206.117,53, aproximadamente 13,6% do total.

**Categoria com maior faturamento:** Home Decor, com US$ 232.275,86, aproximadamente 15,4% do total.

**Mês com maior faturamento:** julho de 2025, com US$ 180.208,16.

Os resultados identificam os maiores valores registrados na amostra, mas não demonstram que esses segmentos sejam necessariamente os mais lucrativos ou representativos do mercado global.

## 7. Dashboard interativo

A aplicação apresenta quatro indicadores principais, visualizações por país e categoria, evolução mensal do faturamento e filtros interativos.

Os filtros permitem selecionar países e categorias, atualizando as métricas e os gráficos conforme o recorte escolhido.

**Link da aplicação:** https://global-ecommerce-analytics.streamlit.app/
 

## 8. Tecnologias utilizadas

- **Python:** linguagem de programação do projeto.
- **Pandas:** leitura, tratamento, validação e análise dos dados.
- **NumPy:** biblioteca de apoio a operações numéricas.
- **Plotly:** criação de gráficos interativos.
- **Streamlit:** desenvolvimento e disponibilização do dashboard.
- **Git e GitHub:** versionamento e publicação do código.

## 9. Estrutura do projeto

```text
global-ecommerce-analytics/
├── .streamlit/
│   └── config.toml
├── dados/
│   ├── brutos/
│   │   └── global_ecommerce_sales.csv
│   └── tratados/
│       └── vendas_tratadas.csv
├── scripts/
│   ├── tratamento_dados.py
│   └── analise_exploratoria.py
├── app.py
├── requirements.txt
└── README.md
```

O ambiente virtual `.venv` é utilizado localmente e não deve ser versionado.

## 10. Como executar

É necessário ter Python e Git instalados.

Clone o repositório, entre na pasta do projeto e crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Para reproduzir o tratamento dos dados:

```bash
python scripts/tratamento_dados.py
```

Para executar a análise exploratória:

```bash
python scripts/analise_exploratoria.py
```

Para iniciar o dashboard:

```bash
python -m streamlit run app.py
```

O arquivo original pode ser obtido no link do dataset informado na seção de fontes, respeitando os termos de utilização.

## 11. Discussão e limitações

Os resultados são descritivos e se referem exclusivamente aos registros presentes na base analisada.

As principais limitações incluem:

- Ausência de informações sobre custos e lucratividade;
- Impossibilidade de generalizar os resultados para todo o comércio eletrônico mundial;
- Cobertura incompleta de novembro de 2025;
- Ausência de variáveis necessárias para investigar causas das diferenças de faturamento;
- Necessidade de confirmar a representatividade e a natureza real ou sintética dos dados na documentação original da fonte.

As comparações realizadas não estabelecem relações de causa e efeito.

## 12. Aplicabilidade profissional

Em um ambiente corporativo, a estrutura desenvolvida poderia servir como base para acompanhar indicadores comerciais, desde que fosse conectada a dados operacionais confiáveis e atualizados.

Para uso profissional, seriam necessários processos de atualização, validação de qualidade, controle de acesso, proteção de dados, monitoramento de falhas e manutenção das dependências.

A aplicação também poderia ser ampliada para incorporar metas, margens, custos, comparações entre períodos e indicadores de desempenho operacional.

## 13. Melhorias futuras

- Adicionar filtros por período;
- Ampliar as estatísticas descritivas;
- Automatizar a obtenção dos dados por API, quando disponível;
- Incluir indicadores de crescimento e variação percentual;
- Implementar testes automatizados de qualidade dos dados;
- Adicionar monitoramento de atualização e execução do pipeline.

## 14. Créditos e referências

- Dataset: https://www.kaggle.com/datasets/kojibrand/global-e-commerce-sales-dataset-2025
- Licença CC0: https://creativecommons.org/publicdomain/zero/1.0/
- Python: https://www.python.org/
- Pandas: https://pandas.pydata.org/docs/
- NumPy: https://numpy.org/doc/
- Plotly: https://plotly.com/python/
- Streamlit: https://docs.streamlit.io/

Projeto acadêmico desenvolvido individualmente para aplicação de conhecimentos de análise de dados, ETL, EDA e Business Intelligence.

## 15. Links de entrega

- **Repositório pessoal:** https://github.com/aarantess/global-ecommerce-analytics
- **Dashboard publicado:** https://global-ecommerce-analytics.streamlit.app/
- **Repositório oficial da turma:** a inserir.
- **Quadro de tarefas:** a inserir, se aplicável.
- **Publicação e vídeo explicativo:** a inserir.
