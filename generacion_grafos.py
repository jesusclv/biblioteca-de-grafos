import random
import math
from typing import Dict, List, Any, Set, Tuple, Union

#* ==========================================
#* CAPA DE ESTRUCTURA DE DATOS
#* ==========================================

class Nodo:
    """Representa un vértice dentro del grafo."""
    def __init__(self, id_nodo: Union[int, str], **kwargs: Any):
        self.id = id_nodo
        # TODO: Permite escalabilidad para guardar pesos, colores, coordenadas, etc.
        self.atributos: Dict[str, Any] = kwargs

    def __str__(self) -> str:
        return str(self.id)


class Arista:
    """Representa la conexión entre dos nodos."""
    def __init__(self, fuente: Nodo, destino: Nodo, dirigido: bool = False, peso: float = 1.0):
        self.fuente = fuente
        self.destino = destino
        self.dirigido = dirigido
        self.peso = peso # TODO: Escalabilidad para futuros algoritmos.

    def __str__(self) -> str:
        conector = "->" if self.dirigido else "--"
        return f"{self.fuente.id} {conector} {self.destino.id}"


class Grafo:
    """Estructura principal del grafo basada en diccionarios."""
    def __init__(self, dirigido: bool = False):
        self.dirigido: bool = dirigido
        self.nodos: Dict[Union[int, str], Nodo] = {}
        self.aristas: Dict[Union[int, str], Dict[Union[int, str], Arista]] = {}

    def agregar_nodo(self, id_nodo: Union[int, str], **kwargs: Any) -> None:
        """Agrega un nodo si no existe e inicializa su diccionario."""
        if id_nodo not in self.nodos:
            self.nodos[id_nodo] = Nodo(id_nodo, **kwargs)
            self.aristas[id_nodo] = {}

    def agregar_arista(self, id_fuente: Union[int, str], id_destino: Union[int, str], peso: float = 1.0) -> None:
        """Crea una arista entre dos nodos, y valida duplicados."""
        self.agregar_nodo(id_fuente)
        self.agregar_nodo(id_destino)
        
        #! Evita duplicados
        if id_destino in self.aristas[id_fuente]:
            return
            
        nueva_arista = Arista(self.nodos[id_fuente], self.nodos[id_destino], self.dirigido, peso)
        self.aristas[id_fuente][id_destino] = nueva_arista
        
        if not self.dirigido:
            self.aristas[id_destino][id_fuente] = nueva_arista

    def obtener_todas_las_aristas(self) -> List[Arista]:
        """Devuelve una lista sin duplicados de todas las aristas del grafo."""
        todas: List[Arista] = []
        visitadas: Set[Tuple[Union[int, str], Union[int, str]]] = set()
        
        for origen, conexiones in self.aristas.items():
            for destino, arista in conexiones.items():
                if not self.dirigido:
                    conexion = tuple(sorted([str(origen), str(destino)]))
                    if conexion not in visitadas:
                        todas.append(arista)
                        visitadas.add(conexion)
                else:
                    todas.append(arista)
        return todas

    def exportar_graphviz(self, nombre_archivo: str) -> None:
        """Exporta el grafo a un archivo .gv."""
        tipo_grafo = "digraph" if self.dirigido else "graph"
        conector = "->" if self.dirigido else "--"

        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(f"{tipo_grafo} G {{\n")
            for id_nodo in self.nodos:
                f.write(f'  "{id_nodo}";\n')
            
            for arista in self.obtener_todas_las_aristas():
                f.write(f'  "{arista.fuente.id}" {conector} "{arista.destino.id}";\n')
            f.write("}\n")


#* ==========================================
#* CAPA DE CREACIÓN
#* ==========================================

class GeneradorGrafos:
    """Clase encargada exclusivamente de fabricar grafos según los modelos."""
    
    @staticmethod
    def malla(m: int, n: int, dirigido: bool = False) -> Grafo:
        g = Grafo(dirigido)
        for i in range(m):
            for j in range(n):
                actual = f"n{i}_{j}"
                g.agregar_nodo(actual)
                if i < m - 1:
                    g.agregar_arista(actual, f"n{i+1}_{j}")
                if j < n - 1:
                    g.agregar_arista(actual, f"n{i}_{j+1}")
        return g

    @staticmethod
    def erdos_renyi(n: int, m: int, dirigido: bool = False) -> Grafo:
        g = Grafo(dirigido)
        for i in range(n): g.agregar_nodo(i)
        
        aristas_creadas = 0
        max_aristas = n * (n - 1) if dirigido else n * (n - 1) // 2
        m = min(m, max_aristas)

        while aristas_creadas < m:
            u, v = random.randint(0, n - 1), random.randint(0, n - 1)
            if u != v and v not in g.aristas[u]:
                g.agregar_arista(u, v)
                aristas_creadas += 1
        return g

    @staticmethod
    def gilbert(n: int, p: float, dirigido: bool = False) -> Grafo:
        g = Grafo(dirigido)
        for i in range(n): g.agregar_nodo(i)
            
        for i in range(n):
            inicio_j = 0 if dirigido else i + 1
            for j in range(inicio_j, n):
                if i != j and random.random() < p:
                    g.agregar_arista(i, j)
        return g

    @staticmethod
    def geografico(n: int, r: float, dirigido: bool = False) -> Grafo:
        g = Grafo(dirigido)
        for i in range(n):
            g.agregar_nodo(i, x=random.uniform(0, 1), y=random.uniform(0, 1))

        for i in range(n):
            for j in range(i + 1, n):
                n1, n2 = g.nodos[i], g.nodos[j]
                dist = math.hypot(n1.atributos['x'] - n2.atributos['x'], n1.atributos['y'] - n2.atributos['y'])
                if dist <= r:
                    g.agregar_arista(i, j)
                    if dirigido: g.agregar_arista(j, i)
        return g

    @staticmethod
    def barabasi_albert(n: int, d: int, dirigido: bool = False) -> Grafo:
        g = Grafo(dirigido)
        for i in range(d): g.agregar_nodo(i)
        for i in range(d):
            for j in range(i + 1, d):
                g.agregar_arista(i, j)
                
        for i in range(d, n):
            g.agregar_nodo(i)
            grados_nodos = []
            for nodo, conexiones in g.aristas.items():
                if isinstance(nodo, int) and nodo < i:
                    grados_nodos.extend([nodo] * len(conexiones))
                    
            objetivos = set()
            while len(objetivos) < d and len(objetivos) < i:
                obj = random.choice(grados_nodos)
                if obj != i: objetivos.add(obj)
                    
            for obj in objetivos:
                g.agregar_arista(i, obj)
        return g

    @staticmethod
    def dorogovtsev_mendes(n: int, dirigido: bool = False) -> Grafo:
        g = Grafo(dirigido)
        if n < 3: return g
        
        for i in range(3): g.agregar_nodo(i)
        g.agregar_arista(0, 1)
        g.agregar_arista(1, 2)
        g.agregar_arista(2, 0)
        
        for i in range(3, n):
            g.agregar_nodo(i)
            arista_aleatoria = random.choice(g.obtener_todas_las_aristas())
            g.agregar_arista(i, arista_aleatoria.fuente.id)
            g.agregar_arista(i, arista_aleatoria.destino.id)
        return g


#* ==========================================
#* RUTINA PRINCIPAL DE EJECUCIÓN
#* ==========================================
if __name__ == "__main__":
    tamanos = [50, 200, 500]
    
    for tam in tamanos:
        #? Ajuste de dimensiones de la malla
        dims_malla = {50: (10, 5), 200: (20, 10), 500: (25, 20)}
        m, n_cols = dims_malla[tam]
        
        #? Creación usando el Patrón
        grafos_generados = {
            f"Malla_{tam}": GeneradorGrafos.malla(m, n_cols),
            f"ErdosRenyi_{tam}": GeneradorGrafos.erdos_renyi(tam, tam * 3),
            f"Gilbert_{tam}": GeneradorGrafos.gilbert(tam, 6.0 / tam),
            f"Geografico_{tam}": GeneradorGrafos.geografico(tam, math.sqrt(4 / (math.pi * tam))), 
            f"BarabasiAlbert_{tam}": GeneradorGrafos.barabasi_albert(tam, 3),
            f"DorogovtsevMendes_{tam}": GeneradorGrafos.dorogovtsev_mendes(tam)
        }
        
        #? Exportación
        for nombre, grafo in grafos_generados.items():
            grafo.exportar_graphviz(f"{nombre}.gv")
            print(f"Generado correctamente: {nombre}.gv")