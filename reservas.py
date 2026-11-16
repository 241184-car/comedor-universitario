# reservas.py - Reservas y control de aforo (RF04, RF05)
from config import AFORO_MAXIMO

reservas = {}

def reservar(turno, estudiante):
    ocupados = reservas.setdefault(turno, [])
    if len(ocupados) >= AFORO_MAXIMO:
        return False
    ocupados.append(estudiante)
    return True
