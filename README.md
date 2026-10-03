# Biblioteca de Generación de Grafos

Este proyecto consiste en una biblioteca desarrollada en **Python 3** diseñada para la creación y exportación de grafos.

---

## Arquitectura del Proyecto

El código está dividido en capas para separar las responsabilidades:

1. **Capa de Estructuras de Datos (`Nodo`, `Arista`, `Grafo`):**
   - Implementa un modelo de **diccionarios** para almacenar las conexiones (`{fuente: {destino: arista}}`).
   - Capacidad de crear grafos dirigidos y no dirigidos.

2. **Capa de Generación (`GeneradorGrafos`):**
   - Una clase dedicada a la fabricación de grafos basados en modelos matemáticos.

3. **Capa de Exportación:**
   - Integrada en la clase `Grafo`, permite exportar la topología a un formato **GraphViz (`.gv`)**.

---

## Modelos de Generación Implementados

La biblioteca incluye 6 algoritmos de generación de grafos:

1. **Modelo $G_{m,n}$ (Malla)**

2. **Modelo $G_{n,m}$ (Erdös y Rényi)**

3. **Modelo $G_{n,p}$ (Gilbert)**

4. **Modelo $G_{n,r}$ (Geográfico Simple)**

5. **Modelo $G_{n,d}$ (Variante Barabási-Albert)**

6. **Modelo $G_{n}$ (Dorogovtsev-Mendes)**

---

## Visualización de Grafos

Todas las imágenes de los grafos incluidas en este proyecto fueron renderizadas en Gephi utilizando el algoritmo de distribución **Yifan Hu Proporcional**.

---

## Requisitos y Ejecución

### Prerrequisitos
- **Python 3** instalado en el sistema.
- **Gephi** (recomendado para la visualización de los resultados).
