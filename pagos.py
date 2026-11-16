# pagos.py - Pagos y ticket con QR (RF06, RF07)
from config import PRECIO_RACION

def calcular_tarifa(es_becario):
    if es_becario:
        return 0.0
    return PRECIO_RACION

def registrar_pago(estudiante, es_becario):
    tarifa = calcular_tarifa(es_becario)
    return {"estudiante": estudiante, "monto": tarifa}

def emitir_ticket(estudiante, turno):
    codigo_qr = "TICKET-" + estudiante + "-" + turno
    return {"estudiante": estudiante, "turno": turno, "qr": codigo_qr, "usado": False}
