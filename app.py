
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"
from pathlib import Path

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="E-commerce em Dados",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# IDENTIDADE VISUAL DO DASHBOARD
# ==========================================

st.markdown("""
<style>
    /* Fundo principal */
    .stApp {
        background-color: #F1F5F9;
        color: #0F172A;
    }

    /* Área central */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #0C172B;
    }

    [data-testid="stSidebar"] * {
        color: #F8FAFC;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #0F172A;
        font-family: 'Segoe UI', sans-serif;
        letter-spacing: -0.5px;
    }

    h1 {
        font-weight: 750;
    }

    /* Cartões de indicadores */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
    }

    [data-testid="stMetricLabel"] {
        color: #64748B;
    }

    [data-testid="stMetricValue"] {
        color: #1D4ED8;
        font-weight: 700;
    }

    /* Separadores */
    hr {
        border-color: #CBD5E1;
    }

    /* Tabelas */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
    }

    /* Campos dos filtros */
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #FFFFFF;
    border-radius: 10px;
    border: 1px solid #CBD5E1;
}

/* Opções selecionadas */
[data-testid="stSidebar"] [data-baseweb="tag"] {
    background-color: #2563EB;
    border-radius: 6px;
}

[data-testid="stSidebar"] span[data-baseweb="tag"] {
    background-color: #2563EB !important;
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] * {
    color: #FFFFFF !important;
}

/* Texto dos campos e opções selecionadas */
[data-testid="stSidebar"] [data-baseweb="select"] input {
    color: #0F172A;
}

[data-testid="stSidebar"] [data-baseweb="tag"] span {
    color: #FFFFFF;
}

/* Ajustar fonte dos valores dos indicadores */
[data-testid="stMetricValue"] {
    font-size: clamp(1.3rem, 2vw, 2rem);
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# CARREGAMENTO DOS DADOS
# ==========================================

PASTA_PROJETO = Path(__file__).resolve().parent

@st.cache_data
def carregar_dados():
    caminho = PASTA_PROJETO / "dados" / "tratados" / "vendas_tratadas.csv"
    dados = pd.read_csv(caminho, parse_dates=["data_pedido"])
    return dados

df = carregar_dados()



# ==========================================
# CABEÇALHO
# ==========================================

st.markdown(
    """
<div style="background: linear-gradient(120deg, #0C172B, #183B68); padding: 32px 38px; border-radius: 18px; margin-bottom: 18px;">
<p style="color: #93C5FD; font-size: 13px; font-weight: 600; letter-spacing: 2px; margin: 0 0 12px 0;">BUSINESS INTELLIGENCE | 2025</p>
<h1 style="color: #FFFFFF; font-size: 38px; font-weight: 750; margin: 0 0 12px 0;">E-commerce em Dados</h1>
<p style="color: #CBD5E1; font-size: 17px; margin: 0;">Análise interativa de vendas globais, desempenho comercial e tendências de consumo.</p>
</div>
    """,
    unsafe_allow_html=True
)


st.divider()


# ==========================================
# FILTROS
# ==========================================

st.sidebar.header("Filtros da análise")

opcoes_paises = ["Todos"] + sorted(df["pais"].unique().tolist())
opcoes_categorias = ["Todas"] + sorted(df["categoria"].unique().tolist())

paises = st.sidebar.multiselect(
    "Países",
    options=opcoes_paises,
    default=["Todos"]
)

categorias = st.sidebar.multiselect(
    "Categorias",
    options=opcoes_categorias,
    default=["Todas"]
)

# Aplicar filtros
df_filtrado = df.copy()

if "Todos" not in paises:
    df_filtrado = df_filtrado[
        df_filtrado["pais"].isin(paises)
    ]

if "Todas" not in categorias:
    df_filtrado = df_filtrado[
        df_filtrado["categoria"].isin(categorias)
    ]


# ==========================================
# INDICADORES
# ==========================================

faturamento = df_filtrado["valor_total"].sum()
pedidos = df_filtrado["id_pedido"].nunique()
unidades = df_filtrado["quantidade"].sum()
ticket_medio = faturamento / pedidos if pedidos > 0 else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Faturamento total",
    f"US$ {faturamento / 1_000_000:,.2f} mi"
    if faturamento >= 1_000_000
    else f"US$ {faturamento:,.2f}"
)

col2.metric(
    "Total de pedidos",
    f"{pedidos:,}"
)

col3.metric(
    "Unidades vendidas",
    f"{unidades:,}"
)

col4.metric(
    "Ticket médio",
    f"US$ {ticket_medio:,.2f}"
)

st.divider()

with st.expander("📋 Visualizar base de dados", expanded=False):
    st.dataframe(
        df_filtrado,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# VISUALIZAÇÕES INTERATIVAS
# ==========================================

st.divider()
st.header("Análise de desempenho comercial")

if df_filtrado.empty:
    st.warning("Nenhum registro encontrado para os filtros selecionados.")

else:
    # --------------------------------------
    # GRÁFICO 1 — EVOLUÇÃO MENSAL
    # --------------------------------------

    st.subheader("Evolução mensal do faturamento")

    vendas_mensais = (
        df_filtrado.groupby("ano_mes", as_index=False)["valor_total"]
        .sum()
        .sort_values("ano_mes")
    )

    fig_mensal = px.line(
        vendas_mensais,
        x="ano_mes",
        y="valor_total",
        markers=True,
        labels={
            "ano_mes": "Mês",
            "valor_total": "Faturamento (US$)"
        }
    )

    fig_mensal.update_layout(
        hovermode="x unified",
        xaxis_title="Mês",
        yaxis_title="Faturamento (US$)"
    )

    fig_mensal.update_traces(
    line_color="#2563EB",
    line_width=3,
    marker=dict(size=8)
)

    st.plotly_chart(fig_mensal, use_container_width=True)

    st.caption(
        "Nota: novembro de 2025 possui registros somente até o dia 01/11. "
        "Por isso, seu faturamento não é diretamente comparável "
        "ao dos meses completos."
    )


    # --------------------------------------
    # GRÁFICO 2 — FATURAMENTO POR PAÍS
    # --------------------------------------

    col_esquerda, col_direita = st.columns(2)

    with col_esquerda:
        st.subheader("Faturamento por país")

        vendas_pais = (
            df_filtrado.groupby("pais", as_index=False)["valor_total"]
            .sum()
            .sort_values("valor_total", ascending=True)
        )

        fig_pais = px.bar(
            vendas_pais,
            x="valor_total",
            y="pais",
            orientation="h",
            labels={
                "valor_total": "Faturamento (US$)",
                "pais": "País"
            }
        )

        fig_pais.update_layout(
            yaxis_title="",
            xaxis_title="Faturamento (US$)"
        )

        fig_pais.update_traces(
            marker_color="#2563EB"
        )

        st.plotly_chart(fig_pais, use_container_width=True)


    # --------------------------------------
    # GRÁFICO 3 — FATURAMENTO POR CATEGORIA
    # --------------------------------------

    with col_direita:
        st.subheader("Faturamento por categoria")

        vendas_categoria = (
            df_filtrado.groupby("categoria", as_index=False)["valor_total"]
            .sum()
            .sort_values("valor_total", ascending=False)
        )

        fig_categoria = px.bar(
            vendas_categoria,
            x="categoria",
            y="valor_total",
            labels={
                "categoria": "Categoria",
                "valor_total": "Faturamento (US$)"
            }
        )

        fig_categoria.update_layout(
            xaxis_tickangle=-35,
            xaxis_title="",
            yaxis_title="Faturamento (US$)"
        )

        fig_categoria.update_traces(
            marker_color="#60A5FA"
        )

        st.plotly_chart(fig_categoria, use_container_width=True)

    # ==========================================
    # INSIGHTS AUTOMÁTICOS
    # ==========================================

st.divider()
st.header("Principais insights")

if df_filtrado.empty:
    st.info("Selecione ao menos um país e uma categoria para visualizar os insights.")

else:
    faturamento_pais = (
        df_filtrado.groupby("pais")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    faturamento_categoria = (
        df_filtrado.groupby("categoria")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    faturamento_mes = (
        df_filtrado.groupby("ano_mes")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    pais_destaque = faturamento_pais.index[0]
    categoria_destaque = faturamento_categoria.index[0]
    mes_destaque = faturamento_mes.index[0]

    participacao_pais = (
        faturamento_pais.iloc[0] / df_filtrado["valor_total"].sum() * 100
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            f"🌎 **País em destaque:** {pais_destaque} "
            f"representa {participacao_pais:.1f}% "
            "do faturamento selecionado."
        )

    with col2:
        st.info(
            f"🛍️ **Categoria líder:** {categoria_destaque} "
            "apresenta o maior faturamento."
        )

    with col3:
        st.info(
            f"📈 **Mês de maior faturamento:** {mes_destaque}."
        )

# ==========================================
# RODAPÉ
# ==========================================

st.divider()

st.markdown(
    """
<div style="text-align: center; padding: 18px 10px;">
    <p style="color: #334155; font-size: 14px; font-weight: 600;">
        E-commerce em Dados | Análise de Vendas Globais — 2025
    </p>
    <p style="color: #64748B; font-size: 12px;">
        Fonte: Global E-Commerce Sales Dataset (2025) — Kaggle
    </p>
    <p style="color: #64748B; font-size: 12px;">
        Tecnologias: Python • Pandas • Plotly • Streamlit
    </p>
    <p style="color: #64748B; font-size: 12px;">
        Período analisado: janeiro a novembro de 2025.
        Novembro possui cobertura parcial.
        Os resultados descrevem exclusivamente as transações da base utilizada.
    </p>
</div>
    """,
    unsafe_allow_html=True
)
