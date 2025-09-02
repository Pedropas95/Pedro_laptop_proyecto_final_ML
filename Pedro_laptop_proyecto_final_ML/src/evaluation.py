import sys, subprocess
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
nb3 = repo / "notebooks" / "03_Entrenamiento_Evaluacion.ipynb"

print("Ejecutando evaluación:", nb3)
subprocess.check_call([sys.executable, "-m", "jupyter", "nbconvert",
                       "--to", "notebook", "--execute", "--inplace", str(nb3)],
                      cwd=str(repo))
print("Hecho:", nb3)
