# -*- coding: utf-8 -*-
"""
training.py
Orquestación: ejecuta 02 y 03 para limpieza/FE y entrenamiento/evaluación.
"""
import subprocess, sys
from pathlib import Path

def ejecutar_02_03():
    repo = Path(__file__).resolve().parent.parent
    nb2 = repo / "notebooks" / "02_LimpiezaEDA.ipynb"
    nb3 = repo / "notebooks" / "03_Entrenamiento_Evaluacion.ipynb"
    assert nb2.exists(), f"No encuentro {nb2}"
    assert nb3.exists(), f"No encuentro {nb3}"
    for nb in (nb2, nb3):
        cmd = [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", str(nb)]
        print("[nb] Ejecutando:", nb)
        subprocess.check_call(cmd, cwd=str(repo))
        print("[nb] Hecho:", nb)

if __name__ == "__main__":
    ejecutar_02_03()
