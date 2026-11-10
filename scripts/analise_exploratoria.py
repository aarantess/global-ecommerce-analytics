import pandas as pd
from pathlib import Path

# Localizar o projeto
PASTA_PROJETO = Path(__file__).resolve().parent.parent

# Carregar os dados tratados
caminho_csv = (
    PASTA_PROJETO / "dados" / "tratados" / "vendas_tratadas.csv"
)

df = pd.read_csv(caminho_csv, parse_dates=["data_pedido"])

# ==========================================
# INDICADORES GERAIS
# ==========================================

faturamento_total = df["valor_total"].sum()
total_pedidos = df["id_pedido"].nunique()
quantidade_vendida = df["quantidade"].sum()
ticket_medio = faturamento_total / total_pedidos

print("\n=== INDICADORES GERAIS ===")
print(f"Faturamento total: US$ {faturamento_total / 1_000_000:,.2f} mi"
    if faturamento_total >= 1_000_000
    else f"Faturamento total: US$ {faturamento_total:,.2f}"
)
print(f"Total de pedidos: {total_pedidos}")
print(f"Quantidade vendida: {quantidade_vendida}")
print(f"Ticket médio: US$ {ticket_medio:,.2f}")

# ==========================================
# FATURAMENTO POR PAÍS
# ==========================================

vendas_pais = (
    df.groupby("pais")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== FATURAMENTO POR PAÍS ===")
print(vendas_pais)

# ==========================================
# FATURAMENTO POR CATEGORIA
# ==========================================

vendas_categoria = (
    df.groupby("categoria")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== FATURAMENTO POR CATEGORIA ===")
print(vendas_categoria)

# ==========================================
# EVOLUÇÃO MENSAL DAS VENDAS
# ==========================================

vendas_mensais = (
    df.groupby("ano_mes")["valor_total"]
    .sum()
    .sort_index()
)

print("\n=== EVOLUÇÃO MENSAL ===")
print(vendas_mensais)