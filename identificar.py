import sys
import os

print("--- DIAGNÓSTICO ---")
print("Executável sendo usado:", sys.executable)
try:
    import pandas as pd
    print("Pandas encontrado na versão:", pd.__version__)
except ImportError:
    print("ERRO: Pandas não encontrado neste Python.")