import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys; import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "01_Programa"))
from arbol_palabras import ArbolBusqueda, limpiar_oracion

ORACION = "El perro café persigue al gato, y el gato huye del perro."

arbol = ArbolBusqueda()
for p in limpiar_oracion(ORACION):
    arbol.insertar(p)

# Posición x = orden inorden, y = profundidad
pos = {}
orden = arbol.inorden(arbol.raiz, [])
for i, n in enumerate(orden):
    pos[id(n)] = [i, 0]

def prof(n, d):
    if n:
        pos[id(n)][1] = -d
        prof(n.izq, d + 1)
        prof(n.der, d + 1)
prof(arbol.raiz, 0)

fig, ax = plt.subplots(figsize=(11, 5.2))
ax.axis("off")

def aristas(n):
    for h, lado in ((n.izq, "I"), (n.der, "D")):
        if h:
            x1, y1 = pos[id(n)]
            x2, y2 = pos[id(h)]
            ax.plot([x1, x2], [y1, y2], color="#555", lw=1.3, zorder=1)
            ax.text((x1 + x2) / 2 + (-0.18 if lado == "I" else 0.18), (y1 + y2) / 2,
                    lado, fontsize=9, color="#888", ha="center", va="center")
            aristas(h)
aristas(arbol.raiz)

hojas = {id(n) for n in arbol.hojas(arbol.raiz, [])}
for n in orden:
    x, y = pos[id(n)]
    es_hoja = id(n) in hojas
    ax.scatter([x], [y], s=3000, zorder=2,
               color="#ffffff" if es_hoja else "#dbe7f5",
               edgecolors="#1f3b5c", linewidths=1.6)
    etiqueta = n.palabra + (f"\n×{n.frecuencia}" if n.frecuencia > 1 else "")
    ax.text(x, y, etiqueta, ha="center", va="center", fontsize=10, zorder=3, color="#111")

ax.set_title(f"Árbol binario de búsqueda para la oración:\n“{ORACION}”", fontsize=12, pad=14)
ax.scatter([], [], s=150, color="#dbe7f5", edgecolors="#1f3b5c", label="Nodo interno")
ax.scatter([], [], s=150, color="#ffffff", edgecolors="#1f3b5c", label="Hoja")
ax.legend(loc="lower left", frameon=False, fontsize=9)
ax.set_xlim(-0.8, len(orden) - 0.2)
ax.set_ylim(min(p[1] for p in pos.values()) - 0.6, 0.6)
plt.tight_layout()
plt.savefig("diagrama_arbol.png", dpi=200)
print("ok")
