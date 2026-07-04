import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    return mo, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Perguntas de Negócio para Análise Exploratória de Dados (EDA)

    Este documento contém um conjunto de perguntas estruturadas e direcionadas para guiar a Análise Exploratória de Dados (EDA), extraindo insights estratégicos sobre faturamento, comportamento do cliente, logística, marketing e produto.

    ---

    ## 1. Faturamento, Lucratividade e Descontos (Visão Financeira)
    * **O desconto impulsiona o lucro ou apenas o volume?** Como o percentual de desconto (`Discount_Percent`) e o uso de cupons (`Coupon_Used`) impactam a margem de lucro real (`Profit_Margin_Percent`) e o valor do lucro (`Profit_Amount`)? Existe um "ponto ideal" de desconto que aumenta as vendas sem destruir a margem?
    * **Análise de Sazonalidade:** Como as vendas (`Order_Amount`) e o lucro flutuam ao longo dos meses e trimestres? O aumento de volume na temporada de férias (`Holiday_Season`) compensa possíveis aumentos nos custos de envio (`Shipping_Cost`) e impostos (`Tax_Amount`)?
    * **Anatomia do Pedido de Alto Valor:** O que diferencia um pedido comum de um `High_Value_Order`? É o volume de itens (`Quantity`), a escolha de marcas premium (`Brand`), ou a ausência de descontos?
    """)
    return


@app.cell
def _(pd):
    dados = pd.read_csv("./data/silver/ecommerce_tratado.csv")
    dados
    return (dados,)


@app.cell
def _(plt):
    def criar_scatter_plot(df, colA, colB):
        plt.scatter(df[colA], df[colB])
        plt.xlabel(colA)
        plt.ylabel(colB)
        plt.show()

    def criar_grafico_barras(df, col_categorias, col_valores):
        plt.bar(df[col_categorias], df[col_valores])
        plt.xlabel(col_categorias)
        plt.ylabel(col_valores)
        plt.show()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Faturamento, Lucratividade e Descontos (Visão Financeira)

    **Q1: O desconto impulsiona o lucro ou apenas o volume?** Como o percentual de desconto (`Discount_Percent`) e o uso de cupons (`Coupon_Used`) impactam a margem de lucro real (`Profit_Margin_Percent`) e o valor do lucro (`Profit_Amount`)? Existe um "ponto ideal" de desconto que aumenta as vendas sem destruir a margem?

    Vamos criar dois datasets para avaliação individual dos mesmos indicadores a partir do uso de cupons. A partir disto vamos avaliar como os descontos aplicados e a margem de lucro se comportam, comparando com o valor do lucro em si.
    """)
    return


@app.cell
def _(dados):
    # divisão dos dados

    dados_com_cupom = dados[dados["Coupon_Used"] == "Yes"]
    dados_sem_cupom = dados[dados["Coupon_Used"] == "No"]
    return dados_com_cupom, dados_sem_cupom


@app.cell
def _(plt, sns):
    def analisar_ponto_ideal_desconto(df, col_desconto, col_margem):
        plt.figure(figsize=(10, 6))
        # O boxplot agrupa os dados e mostra a variação da margem para cada desconto
        sns.boxplot(data=df, x=col_desconto, y=col_margem, palette="vlag")

        # Linha de referência no 0 para ver onde começa o prejuízo
        plt.axhline(0, color='red', linestyle='--', alpha=0.7, label='Margem Zero')

        plt.title('Impacto do Desconto na Margem de Lucro')
        plt.xlabel('Percentual de Desconto')
        plt.ylabel('Margem de Lucro (%)')
        plt.legend()
        plt.show()

    return (analisar_ponto_ideal_desconto,)


@app.cell
def _(plt):
    def analisar_lucro_vs_volume(df, col_desconto, col_lucro_absoluto):
        # Agrupa os dados por desconto para calcular a média do lucro e o volume de vendas
        analise = df.groupby(col_desconto).agg(
            Lucro_Medio=(col_lucro_absoluto, 'mean'),
            Volume_Vendas=(col_lucro_absoluto, 'count')
        ).reset_index()

        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Barra: Volume de Vendas
        color = 'lightblue'
        ax1.set_xlabel('Percentual de Desconto')
        ax1.set_ylabel('Volume de Vendas (Contagem)', color='navy')
        ax1.bar(analise[col_desconto].astype(str), analise['Volume_Vendas'], color=color, alpha=0.7)
        ax1.tick_params(axis='y', labelcolor='navy')

        # Linha (Eixo Gêmeo): Lucro Médio
        ax2 = ax1.twinx()
        color = 'darkgreen'
        ax2.set_ylabel('Lucro Médio Absoluto ($)', color=color)
        ax2.plot(analise[col_desconto].astype(str), analise['Lucro_Medio'], color=color, marker='o', linewidth=2)
        ax2.tick_params(axis='y', labelcolor='darkgreen')

        plt.title('Volume de Vendas vs. Lucro Médio por Nível de Desconto')
        fig.tight_layout()
        plt.show()

    return (analisar_lucro_vs_volume,)


@app.cell
def _(analisar_ponto_ideal_desconto, dados_sem_cupom):
    analisar_ponto_ideal_desconto(dados_sem_cupom, "Discount_Percent", "Profit_Margin_Percent")
    return


@app.cell
def _(analisar_ponto_ideal_desconto, dados_com_cupom):
    analisar_ponto_ideal_desconto(dados_com_cupom, "Discount_Percent", "Profit_Margin_Percent")
    return


@app.cell
def _(analisar_lucro_vs_volume, dados_com_cupom):
    analisar_lucro_vs_volume(dados_com_cupom, "Discount_Percent", "Profit_Amount")
    return


@app.cell
def _(analisar_lucro_vs_volume, dados_sem_cupom):
    analisar_lucro_vs_volume(dados_sem_cupom, "Discount_Percent", "Profit_Amount")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Podemos observar que os descontos aplicados degradam a margem de lucro de forma linear. No entanto, a zona de lucro zero, embora seja aproximada em alguns casos (como pode ser observado pelas caudas inferiores do boxplot), não é alcançada.

    **Q2: Análise de Sazonalidade:** Como as vendas (`Order_Amount`) e o lucro flutuam ao longo dos meses e trimestres? O aumento de volume na temporada de férias (`Holiday_Season`) compensa possíveis aumentos nos custos de envio (`Shipping_Cost`) e impostos (`Tax_Amount`)?
    """)
    return


@app.cell
def _(pd, plt, sns):
    def analisar_margem_trimestral(df, col_data, col_margem_percentual):
        df_copy = df.copy()
        df_copy[col_data] = pd.to_datetime(df_copy[col_data])
        # Extrai o trimestre (ex: 2026Q1)
        df_copy['Trimestre'] = df_copy[col_data].dt.to_period('Q').astype(str)

        trimestral = df_copy.groupby('Trimestre')[col_margem_percentual].mean().reset_index()

        plt.figure(figsize=(9, 5))
        sns.barplot(data=trimestral, x='Trimestre', y=col_margem_percentual, palette='Blues_d')

        plt.title('Margem de Lucro Média por Trimestre')
        plt.xlabel('Trimestre')
        plt.ylabel('Margem de Lucro Média (%)')
        plt.grid(axis='y', linestyle='--', alpha=0.3)

        # Adiciona os valores em cima das barras para facilitar a leitura
        for index, row in trimestral.iterrows():
            plt.text(index, row[col_margem_percentual] + 0.5, f"{row[col_margem_percentual]:.1f}%", 
                     ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        plt.show()

    return (analisar_margem_trimestral,)


@app.cell
def _(analisar_margem_trimestral, dados, pd):
    dados["Order_Date"] = pd.to_datetime(dados["Order_Date"], format="%Y-%m-%d")

    analisar_margem_trimestral(dados, "Order_Date", "Profit_Margin_Percent")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A margem de lucro é bem estável. Agora vamos aos efeitos dos feriados e impostos nos volumes de arrecadação.
    """)
    return


@app.cell
def _(plt):
    def analisar_impacto_ferias(df, col_ferias, col_vendas, col_envio, col_imposto, col_lucro):
        # Agrupa por temporada de férias (True/False ou Sim/Não)
        custos = df.groupby(col_ferias).agg({
            col_envio: 'mean',
            col_imposto: 'mean',
            col_lucro: 'mean'
        }).reset_index()

        # Criando o gráfico de barras empilhadas para ver a composição do preço/retorno médio
        custos.set_index(col_ferias).plot(kind='bar', stacked=True, figsize=(8, 6), 
                                          color=['#ff7f0e', '#d62728', '#2ca02c'])

        plt.title('Composição Média por Pedido: Temporada de Férias vs Normal')
        plt.xlabel('Temporada de Férias?')
        plt.ylabel('Valor Médio por Pedido ($)')
        plt.xticks(rotation=0)
        plt.legend(['Custo de Envio', 'Impostos', 'Lucro Líquido'])
        plt.tight_layout()
        plt.show()

    return (analisar_impacto_ferias,)


@app.cell
def _(analisar_impacto_ferias, dados):
    analisar_impacto_ferias(dados, "Holiday_Season", "Order_Amount", "Shipping_Cost", "Tax_Amount", "Profit_Amount")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As operações em período de férias e regular possuem o mesmo valor por pedido médio. Isto demonstra estabilidade operacional e fiscal por parte da empresa sem machucar a margem de lucro ao longo do tempo avaliado.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Q3: Anatomia do Pedido de Alto Valor:** O que diferencia um pedido comum de um `High_Value_Order`? É o volume de itens (`Quantity`), a escolha de marcas premium (`Brand`), ou a ausência de descontos?
    """)
    return


@app.cell
def _(plt, sns):
    def analisar_perfil_numerico_hvo(df, col_hvo, col_quantidade, col_desconto):
        plt.figure(figsize=(10, 6))

        # Ajustado: Chaves alteradas de True/False para 'Yes'/'No'
        sns.scatterplot(
            data=df, 
            x=col_quantidade, 
            y=col_desconto, 
            hue=col_hvo, 
            alpha=0.6, 
            palette={'Yes': '#2ca02c', 'No': '#7f7f7f'} 
        )

        plt.title('Anatomia do Pedido: Volume de Itens vs. Desconto')
        plt.xlabel('Quantidade de Itens no Pedido')
        plt.ylabel('Percentual de Desconto (%)')
        plt.legend(title='Pedido de Alto Valor?')
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.tight_layout()
        plt.show()

    return (analisar_perfil_numerico_hvo,)


@app.cell
def _(pd, plt):
    def analisar_marcas_hvo(df, col_hvo, col_marca):
        # Cria uma tabela de frequência cruzada (cross-tabulation) e normaliza por linha (index)
        df_marcas = pd.crosstab(df[col_hvo], df[col_marca], normalize='index') * 100

        # Plota as barras empilhadas que somam 100%
        df_marcas.plot(kind='bar', stacked=True, figsize=(10, 6), cmap='tab20')

        plt.title('Mix de Marcas: Pedidos Comuns vs. High Value Orders')
        plt.xlabel('Pedido de Alto Valor?')
        plt.ylabel('Proporção de Vendas da Marca (%)')
        plt.xticks(rotation=0)
        # Move a legenda para fora do gráfico para não cobrir os dados
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Marcas')
        plt.tight_layout()
        plt.show()

    return (analisar_marcas_hvo,)


@app.cell
def _(analisar_perfil_numerico_hvo, dados):
    analisar_perfil_numerico_hvo(dados, "High_Value_Order", "Quantity", "Discount_Percent")
    return


@app.cell
def _(analisar_marcas_hvo, dados):
    analisar_marcas_hvo(dados, "High_Value_Order", "Brand")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A amostra do dataset ébem homogênea quanto às marcas e pedidos de alto valor, de modo que não é possível fazer uma diferenciação profunda de produtos de alto valor e marcas com potencial expansivo.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
