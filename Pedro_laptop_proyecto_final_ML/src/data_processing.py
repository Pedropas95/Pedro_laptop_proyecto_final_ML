import sys, subprocess
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
nb = repo / "notebooks" / "01_Fuentes.ipynb"

print("Ejecutando:", nb)
subprocess.check_call([sys.executable, "-m", "jupyter", "nbconvert",
                       "--to", "notebook", "--execute", "--inplace", str(nb)],
                      cwd=str(repo))
print("Hecho:", nb)
