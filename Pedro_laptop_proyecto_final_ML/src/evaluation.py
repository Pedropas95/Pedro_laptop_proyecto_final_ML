# -*- coding: utf-8 -*-

import subprocess, sys
from pathlib import Path

def evaluar():
    repo = Path(__file__).resolve().parent.parent
    nb3 = repo / "notebooks" / "03_Entrenamiento_Evaluacion.ipynb"
    assert nb3.exists(), f"No encuentro {nb3}"
    cmd = [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", str(nb3)]
    print("[eval] Ejecutando:", nb3)
    subprocess.check_call(cmd, cwd=str(repo))
    print("[eval] Hecho:", nb3)

if __name__ == "__main__":
    evaluar()
