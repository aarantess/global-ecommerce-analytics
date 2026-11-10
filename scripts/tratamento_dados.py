import pandas as pd
from pathlib import Path

# Localizar a pasta principal do projeto
PASTA_PROJETO = Path(__file__).resolve().parent.parent

# Caminho do arquivo original
caminho_csv = PASTA_PROJETO / "dados" / "brutos" / "global_ecommerce_sales.csv"

# Extração dos dados
df = pd.read_csv(caminho_csv)

# Primeira inspeção
print("\n=== PRIMEIRAS 5 LINHAS ===")
print(df.head())

print("\n=== DIMENSÕES DA BASE ===")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")

print("\n=== TIPOS DE DADOS ===")
print(df.dtypes)

print("\n=== VALORES AUSENTES ===")
print(df.isnull().sum())

print("\n=== REGISTROS DUPLICADOS ===")
print(df.duplicated().sum())

# ==========================================
# TRANSFORMAÇÃO DOS DADOS
# ==========================================

# Traduzir os nomes das colunas
df = df.rename(columns={
    "Order_ID": "id_pedido",
    "Country": "pais",
    "Category": "categoria",
    "Unit_Price": "preco_unitario",
    "Quantity": "quantidade",
    "Order_Date": "data_pedido",
    "Total_Amount": "valor_total"
})

# Converter a data (formato americano: mês/dia/ano)
df["data_pedido"] = pd.to_datetime(
    df["data_pedido"],
    format="%m/%d/%Y",
    errors="raise"
)

# Criar variáveis temporais
df["ano"] = df["data_pedido"].dt.year
df["mes"] = df["data_pedido"].dt.month
df["ano_mes"] = df["data_pedido"].dt.strftime("%Y-%m")

# Traduzir os países
paises = {
    "Germany": "Alemanha",
    "Pakistan": "Paquistão",
    "Australia": "Austrália",
    "UAE": "Emirados Árabes Unidos",
    "USA": "Estados Unidos",
    "Brazil": "Brasil",
    "India": "Índia",
    "Canada": "Canadá",
    "China": "China",
    "UK": "Reino Unido"
}

df["pais"] = df["pais"].replace(paises)

# Traduzir categorias
categorias = {
    "Electronics": "Eletrônicos",
    "Toys": "Brinquedos",
    "Fashion": "Moda",
    "Grocery": "Supermercado",
    "Sports": "Esportes",
    "Beauty": "Beleza",
    "Home": "Casa",
    "Books": "Livros"
}

df["categoria"] = df["categoria"].replace(categorias)

# ==========================================
# CARGA DOS DADOS TRATADOS
# ==========================================

caminho_saida = (
    PASTA_PROJETO / "dados" / "tratados" / "vendas_tratadas.csv"
)

caminho_saida.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(
    caminho_saida,
    index=False,
    encoding="utf-8-sig"
)

print("\n=== TRANSFORMAÇÃO CONCLUÍDA ===")
print(df.head())

print("\n=== PERÍODO DOS DADOS ===")
print("Data inicial:", df["data_pedido"].min())
print("Data final:", df["data_pedido"].max())

print("\n=== PAÍSES ===")
print(sorted(df["pais"].unique()))

print("\n=== CATEGORIAS ===")
print(sorted(df["categoria"].unique()))

print("\nArquivo salvo em:", caminho_saida)