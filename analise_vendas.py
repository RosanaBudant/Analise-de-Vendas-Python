import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
df = pd.read_csv("vendas.csv")

# calcular faturamento
df["faturamento"] = df["quantidade"] * df["preco"]

print("Faturamento total:")
print(df["faturamento"].sum())

print("\nProdutos mais vendidos:")
print(df.sort_values("quantidade", ascending=False))

# vendas por categoria
categoria = df.groupby("categoria")["faturamento"].sum()

print("\nFaturamento por categoria:")
print(categoria)

# gráfico
categoria.plot(kind="bar")

plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento")

plt.show()