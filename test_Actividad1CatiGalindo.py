import math
import numpy as np
import pytest
import Actividad1CatiGalindo as pr

def test_mesmasgastado():
    gastos ={'Enero': -17621, 'Febrero': -24398, 'Marzo': -29690, 'Abril': -34133, 'Mayo': -17200, 'Junio': -24197, 'Julio': -18390, 'Agosto': -29013, 'Septiembre': -29151, 'Octubre': -22957, 'Noviembre': -24180, 'Diciembre': -25861}
    mes, maxmesgasto =  pr.mes_mas_gastado(gastos)
    assert maxmesgasto == -34133

def test_mesmasahorrado():
    ingresos = {'Enero': 29685, 'Febrero': 24437, 'Marzo': 21721, 'Abril': 15200, 'Mayo': 27504, 'Junio': 22720, 'Julio': 26690, 'Agosto': 20278, 'Septiembre': 18203, 'Octubre': 26369, 'Noviembre': 25337, 'Diciembre': 22817}
    mesahorro, maxmes =pr.mes_mas_ahorrado(ingresos)
    assert maxmes == 29685

def test_mediagastosanual():
    gastos = {'Enero': -17621, 'Febrero': -24398, 'Marzo': -29690, 'Abril': -34133, 'Mayo': -17200, 'Junio': -24197, 'Julio': -18390, 'Agosto': -29013, 'Septiembre': -29151, 'Octubre': -22957, 'Noviembre': -24180, 'Diciembre': -25861}
    assert pr.media_gastos_anual(gastos) == -24732.583333333332

def test_gastototalanual():
    gastos = {'Enero': -17621, 'Febrero': -24398, 'Marzo': -29690, 'Abril': -34133, 'Mayo': -17200, 'Junio': -24197, 'Julio': -18390, 'Agosto': -29013, 'Septiembre': -29151, 'Octubre': -22957, 'Noviembre': -24180, 'Diciembre': -25861}
    assert pr.total_gastos_anual(gastos) == -296791
 
def test_ingresostotalanual():
    ingresos = {'Enero': 29685, 'Febrero': 24437, 'Marzo': 21721, 'Abril': 15200, 'Mayo': 27504, 'Junio': 22720, 'Julio': 26690, 'Agosto': 20278, 'Septiembre': 18203, 'Octubre': 26369, 'Noviembre': 25337, 'Diciembre': 22817}
    assert pr.total_ingresos_anual(ingresos) == 280961