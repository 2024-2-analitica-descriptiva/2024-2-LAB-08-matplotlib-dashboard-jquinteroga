# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

"""
El archivo `files//shipping-data.csv` contiene información sobre los envios
de productos de una empresa. Cree un dashboard estático en HTML que
permita visualizar los siguientes campos:

* `Warehouse_block`

* `Mode_of_Shipment`

* `Customer_rating`

* `Weight_in_gms`

El dashboard generado debe ser similar a este:

https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

Para ello, siga las instrucciones dadas en el siguiente video:

https://youtu.be/AgbWALiAGVo

Tenga en cuenta los siguientes cambios respecto al video:

* El archivo de datos se encuentra en la carpeta `data`.

* Todos los archivos debe ser creados en la carpeta `docs`.

* Su código debe crear la carpeta `docs` si no existe.

"""

# pylint: disable=line-too-long
"""
Genera un dashboard estático en HTML con visualizaciones de los datos de envíos.
"""
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo
import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    """
    Crea un conjunto de gráficos estáticos en la carpeta `docs` a partir de
    los datos del archivo `files/input/shipping-data.csv`. Genera los siguientes
    gráficos:
    - Distribución de envíos por almacén.
    - Modalidad de envío.
    - Calificación promedio de clientes por modalidad de envío.
    - Distribución del peso de los envíos.
    
    Además, crea un archivo `index.html` vacío en la carpeta `docs`.
    """
    # Crear la carpeta `docs` si no existe
    os.makedirs("docs", exist_ok=True)
    
    # Leer los datos
    df = pd.read_csv("files/input/shipping-data.csv")
    
    # Gráfico: Distribución por almacén
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Warehouse block",
        ylabel="Record Count",
        color="tab:blue",
        fontsize=8
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png")

    # Gráfico: Modalidad de envío
    plt.figure()
    counts2 = df.Mode_of_Shipment.value_counts()
    counts2.plot.pie(
        title="Mode of Shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"]
    )
    plt.savefig("docs/mode_of_shipment.png")

    # Gráfico: Calificación del cliente
    plt.figure()
    df1 = (
        df[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )
    df1.columns = df1.columns.droplevel()
    df1 = df1[["mean", "min", "max"]]
    plt.barh(
        y=df1.index.values,
        width=df1["max"].values - 1,
        left=df1["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8
    )
    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in df1["mean"].values
    ]
    plt.barh(
        y=df1.index.values,
        width=df1["mean"].values - 1,
        left=df1["min"].values,
        color=colors,
        height=0.5,
        alpha=1.0
    )
    plt.title("Average Customer Rating")
    plt.gca().spines["left"].set_visible("gray")
    plt.gca().spines["bottom"].set_visible("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/average_customer_rating.png")

    # Gráfico: Distribución del peso
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title="Shipped Weight Distribution",
        color="tab:orange",
        edgecolor="white"
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/weight_distribution.png")

    # Crear un archivo index.html vacío
    with open("docs/index.html", "w") as file:
        file.write("")

    return df

# Ejecutar la función
pregunta_01()
