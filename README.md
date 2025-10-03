# github-terminal-app 

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

##  Mi Primer Proyecto en Python: Perfilador Básico de GitHub CLI

Este proyecto, **`github-terminal-app`**, es mi primera incursión en la creación de una aplicación de línea de comandos (CLI) utilizando Python. Su propósito es interactuar con la **API REST de GitHub** para obtener y mostrar información pública básica de cualquier usuario de GitHub.

Fue un desafío emocionante aprender a usar la librería `requests` para realizar peticiones web y manejar los datos en formato JSON que la API devuelve. Este proyecto representa un paso importante en mi camino como desarrollador.

---

##  Características

* Obtiene el nombre de usuario, nombre real, ubicación, biografía, URL del perfil.
* Muestra el número de repositorios públicos, seguidores y a cuántas personas sigue el usuario.
* Aplicación de terminal simple y directa.

---

## Demostración (Opcional: Si tienes una captura de pantalla)

Aquí puedes ver la aplicación en acción:

![Captura de pantalla de la aplicación](screenshot.png) ---

## ¿Cómo Usar?

Sigue estos pasos para poner en marcha la aplicación en tu entorno local.

### 1. Requisitos Previos

Asegúrate de tener instalado **Python 3**.

La única dependencia de Python es la librería `requests`. Puedes instalarla fácilmente usando `pip`:

```bash
pip install requests
```
*(Si estás utilizando un entorno virtual, asegúrate de activarlo antes de ejecutar el comando `pip`.)*

### 2. Ejecución de la Aplicación

1.  Abre tu terminal.
2.  Navega hasta el directorio donde has clonado o descargado este repositorio.
3.  Ejecuta el script principal:
    ```bash
    python proyecto.py
    ```
4.  La aplicación te pedirá que ingreses un nombre de usuario de GitHub:
    ```
    Dame tu usuario de GitHub:
    ```
5.  Introduce el nombre de usuario (ejemplo: `octocat` o `torvalds`) y presiona Enter.
    El programa imprimirá la información obtenida directamente en tu terminal.

---

## Estructura del Proyecto

* `proyecto.py`: El script principal que contiene toda la lógica para la interacción con la API y la presentación de los datos.
* `README.md`: Este archivo, que describe el proyecto.
* `requirements.txt`: (Opcional, pero recomendado) Lista de dependencias de Python.

---

## Lecciones Aprendidas

Durante el desarrollo de `github-terminal-app`, aprendí sobre:

* **Uso de Librerías Externas**: La importancia de `requests` para peticiones HTTP.
* **APIs REST**: Cómo estructurar solicitudes a una API y entender sus respuestas.
* **Manejo de Datos JSON**: Cómo parsear y extraer información útil de las respuestas de la API.
* **Manejo Básico de Errores**: Cómo verificar el estado de las respuestas (`status_code`).
* **Desarrollo CLI**: Creación de aplicaciones interactivas para la terminal.

---

## Contribuciones

Este proyecto es un punto de partida. Si tienes sugerencias para mejorar el código, optimizar la lógica o añadir nuevas funcionalidades (por ejemplo, manejo de más datos, gestión de límites de la API, etc.), ¡son bienvenidas!

No dudes en:
* Abrir un [**Issue**](https://github.com/LuisandovalU/github-terminal-app/issues) para reportar errores o sugerir ideas.
* Enviar un [**Pull Request**](https://github.com/LuisandovalU/github-terminal-app/pulls) con tus contribuciones de código.

---

## Autor

* **Luis Alberto Sandoval Ramos** - [Perfil de GitHub](https://github.com/LuisandovalU)

---

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE` (si lo agregas).
