import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    dicionario = pd.read_csv("./data/bronze/data_dictionary.csv") # por sorte dessa vez temos um dicionário! Vamos torcer para ele ser descritivo
    dicionario
    return


@app.cell
def _(pd):
    dados_brutos = pd.read_csv("./data/bronze/ecommerce_orders_dataset.csv")
    dados_brutos
    return (dados_brutos,)


@app.cell
def _(dados_brutos, pd):
    dados_com_datas = dados_brutos.copy()
    dados_com_datas["Order_Date"] = pd.to_datetime(dados_brutos["Order_Date"], format="%Y-%m-%d")
    dados_com_datas
    return (dados_com_datas,)


@app.cell
def _(dados_com_datas):
    dados_sem_redundancias = dados_com_datas.drop(columns=["Year", "Month", "Day", "Quarter"]) # deixando as colunas que sao redundantes ou podem ser inferidas a partir de ouras
    dados_sem_redundancias
    return (dados_sem_redundancias,)


@app.cell
def _(dados_sem_redundancias):
    dados_sem_redundancias.to_csv("./data/silver/ecommerce_tratado.csv")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
