import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset


df = pd.read_csv("data/creditcard.csv", encoding="latin-1", low_memory=False)

print(df.head())
print(df.shape)

# Cantidad de fraudes

print(df["Class"].value_counts())


# Porcentaje de fraude

fraud_rate = df["Class"].mean() * 100
print("Porcentaje de fraude:", fraud_rate)


# Separar fraudes y normales

frauds = df[df["Class"] == 1]
normal = df[df["Class"] == 0]

print("Fraudes:", len(frauds))
print("Normales:", len(normal))


# Análisis de montos

print("Monto promedio fraude:", frauds["Amount"].mean())
print("Monto promedio normal:", normal["Amount"].mean())

print("Monto máximo fraude:", frauds["Amount"].max())


# Transacciones más grandes

print(df.sort_values("Amount", ascending=False).head(10))


# Distribución de montos

plt.hist(df["Amount"], bins=50)

plt.title("Distribución de montos de transacciones")
plt.xlabel("Monto")
plt.ylabel("Frecuencia")

plt.show()


# Fraude vs normal (gráfico)

df["Class"].value_counts().plot(kind="bar")

plt.yscale("log")

plt.title("Transacciones normales vs fraude")
plt.xlabel("Clase (0=Normal, 1=Fraude)")
plt.ylabel("Cantidad (log)")

plt.show()


# Comparación de montos


df.boxplot(column="Amount", by="Class")

plt.title("Monto de transacciones: normal vs fraude")
plt.suptitle("")
plt.xlabel("Clase (0=Normal, 1=Fraude)")
plt.ylabel("Monto")

plt.show()


# Promedio de montos

avg_fraud = df[df["Class"] == 1]["Amount"].mean()
avg_normal = df[df["Class"] == 0]["Amount"].mean()

print("Monto promedio fraude:", avg_fraud)
print("Monto promedio normal:", avg_normal)


# Fraudes más grandes

print("Top 10 fraudes más grandes:")
print(df[df["Class"] == 1].sort_values("Amount", ascending=False).head(10))


# Guardar dataset procesado

df.to_csv("data/transacciones_procesadas.csv", index=False)