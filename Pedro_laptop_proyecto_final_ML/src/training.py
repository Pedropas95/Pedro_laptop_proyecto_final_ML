import sys, subprocess
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
notebooks = [
    repo / "notebooks" / "02_LimpiezaEDA.ipynb",
    repo / "notebooks" / "03_Entrenamiento_Evaluacion.ipynb"
]

for nb in notebooks:
    print("Ejecutando:", nb)
    subprocess.check_call([sys.executable, "-m", "jupyter", "nbconvert",
                           "--to", "notebook", "--execute", "--inplace", str(nb)],
                          cwd=str(repo))
    print("Hecho:", nb)
