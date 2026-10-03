# 🕸️ Biblioteca de Generación de Grafos Orientada a Objetos

Este proyecto consiste en una biblioteca desarrollada en **Python 3** diseñada para la creación, representación y exportación de grafos utilizando el paradigma de Programación Orientada a Objetos (POO). 

El sistema ha sido estructurado bajo los principios de **Clean Code** y **SOLID**, garantizando un alto rendimiento mediante diccionarios de adyacencia ($O(1)$ en búsquedas) y una arquitectura modular escalable, lista para la futura implementación de algoritmos de búsqueda y recorridos (BFS, DFS, Dijkstra, etc.).

---

## 📐 Arquitectura del Proyecto

El código base está dividido en capas lógicas para separar las responsabilidades:

1. **Capa de Estructuras de Datos (`Nodo`, `Arista`, `Grafo`):**
   - Implementa un modelo de **diccionarios de adyacencia** anidados para almacenar las conexiones (`{fuente: {destino: arista}}`). Esto soluciona cuellos de botella en grafos densos al evitar iteraciones completas sobre listas.
   - Capacidad de crear grafos dirigidos y no dirigidos.
   - Los nodos pueden almacenar atributos dinámicos (`**kwargs`), como coordenadas espaciales ($x, y$) o futuros pesos/colores.

2. **Capa de Generación - Patrón Factory (`GeneradorGrafos`):**
   - Una clase estática dedicada exclusivamente a la fabricación de grafos basados en modelos matemáticos y probabilísticos. Separa la lógica de construcción de la lógica de almacenamiento.

3. **Capa de Exportación:**
   - Integrada en la clase `Grafo`, permite exportar la topología de la red a formato **GraphViz (`.gv`)** de manera nativa para su posterior análisis topológico y visual.

---

## 🧬 Modelos de Generación Implementados

La biblioteca incluye 6 algoritmos clásicos de generación de grafos:

1. **Modelo $G_{m,n}$ (Malla):**
   Genera una cuadrícula de $m \times n$ nodos, conectando cada nodo $(i,j)$ con sus adyacentes $(i+1, j)$ e $(i, j+1)$.
2. **Modelo $G_{n,m}$ (Erdös y Rényi):**
   Crea $n$ nodos y elige uniformemente al azar $m$ pares de vértices distintos para conectarlos.
3. **Modelo $G_{n,p}$ (Gilbert):**
   Crea $n$ nodos y evalúa cada par posible. Una arista se crea con una probabilidad uniforme $p$.
4. **Modelo $G_{n,r}$ (Geográfico Simple):**
   Distribuye $n$ nodos aleatoriamente en un plano unitario (coordenadas entre 0 y 1). Dos nodos se conectan si la distancia euclidiana entre ellos es menor o igual a un radio $r$.
5. **Modelo $G_{n,d}$ (Variante Barabási-Albert):**
   Genera un grafo libre de escala. Comienza con una clique de $d$ nodos. Los nodos subsecuentes se conectan a $d$ nodos existentes con una probabilidad proporcional al grado actual de los nodos destino (conexión preferencial).
6. **Modelo $G_{n}$ (Dorogovtsev-Mendes):**
   Comienza con un triángulo (3 nodos, 3 aristas). Cada nuevo nodo introducido se conecta a los dos extremos de una arista elegida aleatoriamente del grafo existente.

---

## 🚀 Requisitos y Ejecución

### Prerrequisitos
- **Python 3.x** instalado en el sistema.
- No se requieren bibliotecas externas de Python (se utilizan exclusivamente bibliotecas estándar: `random`, `math`, `typing`).
- **Gephi** (recomendado para la visualización de los resultados).

### ¿Cómo ejecutar el proyecto?

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DE_LA_CARPETA>