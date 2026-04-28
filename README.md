# Pre Entrega - Automation Testing

## Propósito
Este proyecto automatiza pruebas sobre el sitio saucedemo.com utilizando Selenium WebDriver y Pytest.

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML

## Instalación
Instalar dependencias con:
python -m pip install selenium pytest pytest-html

## Ejecución de pruebas
Ejecutar el siguiente comando:
python -m pytest -v --html=reports/reporte.html

## Estructura del proyecto
tests/
utils/
reports/

## Casos de prueba implementados
- Login exitoso
- Verificación de catálogo de productos
- Agregado de producto al carrito

## Reporte
Se genera un reporte en HTML dentro de la carpeta reports.