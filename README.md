# Proyecto Final - Automatización Testing

## Descripción

Proyecto final de Automatización de Pruebas utilizando Python, Selenium WebDriver, Pytest y el patrón de diseño Page Object Model (POM).

Se automatizaron pruebas funcionales sobre el sitio SauceDemo y pruebas de API utilizando JSONPlaceholder.

---

## Tecnologías utilizadas

* Python 3
* Selenium WebDriver
* Pytest
* Requests
* ChromeDriver
* Page Object Model (POM)

---

## Estructura del proyecto

```text
proyecto-final-automation-testing-Gloriangel
│
├── data
│   └── usuarios.csv
│
├── pages
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_complete_page.py
│
├── tests
│   ├── test_login.py
│   ├── test_login_invalido.py
│   ├── test_catalogo.py
│   ├── test_carrito.py
│   ├── test_checkout.py
│   └── test_api.py
│
├── utils
│   └── helpers.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Casos de prueba automatizados

### UI Testing (SauceDemo)

* Login exitoso
* Login inválido
* Validación de catálogo de productos
* Agregar producto al carrito
* Flujo de checkout

### API Testing (JSONPlaceholder)

* Obtener listado de posts
* Obtener post por ID
* Eliminar post

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/gloriangelrojas-design/proyecto-final-automation-testing-Gloriangel.git
```

Ingresar al proyecto:

```bash
cd proyecto-final-automation-testing-Gloriangel
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Ejecutar todos los tests:

```bash
python -m pytest -v
```

---

## Resultado esperado

Todos los casos de prueba deben ejecutarse correctamente mostrando estado PASSED.

Resultado actual:

* 8 tests ejecutados
* 8 tests aprobados

---

## Repositorio GitHub

https://github.com/gloriangelrojas-design/proyecto-final-automation-testing-Gloriangel

