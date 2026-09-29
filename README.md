# Cuenta bancaria a 10 años

Aplicación en Python y Streamlit, con la misma estructura del modelo proporcionado:

```text
cuenta_bancaria/
  app.py
  pages/1_Cuenta_bancaria.py
  services/__init__.py
  services/calculations.py
  requirements.txt
```

## Iniciar

1. Descomprime el ZIP.
2. Abre una terminal dentro de la carpeta `cuenta_bancaria`.
3. Instala las dependencias: `python -m pip install -r requirements.txt`
4. Ejecuta: `python -m streamlit run app.py`
5. Abre **Cuenta bancaria** en el menú izquierdo.

Requiere Python 3.10 o posterior y acceso a Internet para instalar las dependencias.

## Funciones

- Proyección fija de 10 años (120 meses).
- Saldo inicial, depósito mensual y tasa nominal anual editables.
- Gráfica de saldo, aportaciones e intereses acumulados.
- Gráfica de intereses generados en cada mes o año.
- Filtros por rango de años, detalle mensual/anual y series de la gráfica de evolución.
- Tabla y descarga CSV que respetan el rango y el detalle seleccionados.
- Indicadores finales a 10 años, independientes de los filtros.

## Supuestos

La tasa nominal anual se divide entre 12 y se aplica al saldo de inicio de cada mes.
Después se añade el depósito mensual. Los intereses se reinvierten; no se consideran
retiros, impuestos, comisiones ni inflación. Se usa una sola unidad monetaria elegida
por quien utiliza la aplicación. Los valores iniciales son un ejemplo editable.

## Funciones lambda de Python

En `services/calculations.py` se utilizan funciones `lambda` para calcular el
interés mensual, actualizar el saldo, obtener el año y validar los valores.
La validación aplica `map` y `all` a los tres datos de entrada.

```python
calcular_interes_mensual = lambda saldo, tasa_anual: saldo * tasa_anual / 1200
actualizar_saldo = lambda saldo, interes, deposito: saldo + interes + deposito
obtener_anio = lambda mes: (mes - 1) // 12 + 1
es_valor_valido = lambda valor: isfinite(valor) and valor >= 0
```

La función `calcular_cuenta` conserva `def` para coordinar la validación y el
bucle de 120 meses: una función `lambda` solo admite una expresión.
