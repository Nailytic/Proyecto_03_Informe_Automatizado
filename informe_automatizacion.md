# 📄 Informe Técnico – Proyecto 03: Automatización de Informes con Python

## 🎯 Objetivo del Proyecto

Automatizar el proceso de generación de informes mensuales para una red de centros educativos, transformando datos operativos en visualizaciones, análisis comparativos y documentos formateados (PDF, Excel) con un solo comando.

---

## 🧾 Dataset

El archivo `resultados_operativos.csv` contiene datos de 10 centros sobre:

- Asistencia promedio (%)
- Nivel de satisfacción (1 a 5)
- Tasa de finalización (%)
- Número de incidencias registradas

Incluye registros de **marzo y abril**, permitiendo análisis comparativo.

---

## ⚙️ Proceso Automatizado

Implementado en el script `generar_informe.py`, este flujo automatiza:

1. Carga de datos y cálculo de diferencias
2. Generación de gráficos con Seaborn
3. Renderizado de informe con Jinja2 (HTML → PDF)
4. Exportación a Excel con datos procesados

---

## 📈 Visualizaciones Generadas

- Barras de asistencia por centro (abril)
- Barras de satisfacción por centro (abril)

---

## ✅ Resultados

Se genera automáticamente:

- 📄 `informe_mensual_abril.pdf`
- 📊 `informe_excel.xlsx`

Ambos disponibles en la carpeta `output/`.

---

## 🧠 Conclusión

Este proyecto demuestra la capacidad de transformar datos crudos en documentos profesionales, listos para presentación, sin intervención manual. Es aplicable a cualquier entorno institucional o corporativo.

**Autora:** Naiara Rodríguez  
**Fecha:** Abril 2025  
**Licencia:** MIT
