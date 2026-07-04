# 🛒 Análise Exploratória de Dados (EDA) - E-commerce

Este repositório contém o pipeline de Análise Exploratória de Dados (EDA) para a base de dados de vendas do e-commerce. O objetivo principal deste projeto é transformar dados brutos de transações em insights estratégicos para apoiar a tomada de decisão das equipes de precificação, marketing e logística.

As análises podem ser verificadas em formato HTML no diretório reports.

---

## 🎯 Perguntas de Negócio Respondidas

O projeto foi estruturado para responder a três dores latentes da operação:

### **Q1: O desconto impulsiona o lucro ou apenas o volume?**
* **Objetivo:** Entender o impacto do percentual de desconto (`Discount_Percent`) e cupons na margem real (`Profit_Margin_Percent`) e valor absoluto (`Profit_Amount`).
* **Abordagem:** Identificar se existe um "ponto ideal" de desconto que alavanque o volume de vendas sem destruir a rentabilidade da operação.

### **Q2: Análise de Sazonalidade e Custos**
* **Objetivo:** Avaliar como as vendas (`Order_Amount`) e o lucro flutuam ao longo dos meses e trimestres.
* **Abordagem:** Validar se o pico de faturamento na temporada de férias (`Holiday_Season`) é saudável ou se acaba sendo engolido por custos logísticos (`Shipping_Cost`) e impostos (`Tax_Amount`).

### **Q3: Anatomia do Pedido de Alto Valor (HVO)**
* **Objetivo:** Mapear o perfil dos pedidos classificados como `High_Value_Order` (Yes/No).
* **Abordagem:** Descobrir se esses pedidos se diferenciam pelo volume de itens comprados (`Quantity`), pela escolha de marcas premium (`Brand`) ou se são impulsionados por compras a preço cheio (sem desconto).

---

## 🛠️ Tecnologias e Ferramentas

O projeto foi desenvolvido em ambiente isolado utilizando:
* **Linguagem:** Python 3.14+
* **Ambiente de Desenvolvimento:** Marimo Notebooks (`marimo`)
* **Manipulação de Dados:** `pandas`
* **Visualização de Dados:** `matplotlib` e `seaborn`
