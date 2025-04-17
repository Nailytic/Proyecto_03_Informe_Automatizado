import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os

# Leer datos
df = pd.read_csv("data/resultados_operativos.csv")

# Calcular diferencias
df["Dif_Asistencia"] = (df["Asistencia_Abril"] - df["Asistencia_Marzo"]).round(2)
df["Dif_Satisfaccion"] = (df["Satisfaccion_Abril"] - df["Satisfaccion_Marzo"]).round(2)
df["Dif_Finalizacion"] = (df["Finalizacion_Abril"] - df["Finalizacion_Marzo"]).round(2)

# Resumen general
resumen = {
    "asistencia_prom": round(df["Asistencia_Abril"].mean(), 2),
    "satisfaccion_prom": round(df["Satisfaccion_Abril"].mean(), 2),
    "finalizacion_prom": round(df["Finalizacion_Abril"].mean(), 2),
    "incidencias_tot": int(df["Incidencias_Abril"].sum())
}

# Crear visualizaciones
sns.set(style="whitegrid")

plt.figure(figsize=(8, 4))
sns.barplot(x="Centro", y="Asistencia_Abril", data=df)
plt.title("Asistencia por Centro (Abril)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/grafico_asistencia.png")
plt.close()

plt.figure(figsize=(8, 4))
sns.barplot(x="Centro", y="Satisfaccion_Abril", data=df)
plt.title("Satisfacción por Centro (Abril)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/grafico_satisfaccion.png")
plt.close()

# Render HTML con Jinja2
env = Environment(loader=FileSystemLoader("scripts"))
template = env.get_template("plantilla_informe.html")
html_content = template.render(datos=df.to_dict(orient="records"), resumen=resumen)

# Guardar HTML temporal
with open("output/informe_temp.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Exportar a PDF (requiere wkhtmltopdf instalado)
pdfkit.from_file("output/informe_temp.html", "output/informe_mensual_abril.pdf")

# Exportar a Excel
df.to_excel("output/informe_excel.xlsx", index=False)

print("Informe generado exitosamente.")
