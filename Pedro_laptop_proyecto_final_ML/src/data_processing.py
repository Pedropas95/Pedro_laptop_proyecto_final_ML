# -*- coding: utf-8 -*-

import subprocess, sys
from pathlib import Path

def ejecutar_01():
    repo = Path(__file__).resolve().parent.parent
    nb = repo / "notebooks" / "01_Fuentes.ipynb"
    assert nb.exists(), f"No encuentro {nb}"
    # Ejecuta y guarda un notebook ejecutado (no sobrescribe el original)
    out = repo / "notebooks" / "01_Fuentes_ejecutado.ipynb"
    cmd = [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", str(nb)]
    # Usamos --inplace para que el estado quede en el cuaderno (como pide el profe al inspeccionar)
    print("[01] Ejecutando:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(repo))
    print("[01] Hecho:", nb)

if __name__ == "__main__":
    ejecutar_01()
