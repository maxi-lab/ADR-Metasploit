
# API de Experimentación con Metasploit

Este proyecto es una API desarrollada para experimentar y facilitar pruebas con Metasploit, en el marco del trabajo de investigación de la materia **Administración de Sistemas de Información** de la **Universidad Tecnológica Nacional, Facultad Regional La Plata (UTN FRLP)**.

## Objetivo
El objetivo principal de esta API es servir como entorno de pruebas y experimentación para integrar Metasploit, permitiendo a los alumnos explorar conceptos de seguridad informática y administración de sistemas.

## Tecnologías utilizadas
- **Django** y **Django REST Framework** (DRF) para la creación de la API.
- Python 3.x

## Instalación y Configuración

### 1. Clonar el repositorio y crear entorno virtual

Windows (CMD):
```cmd
# Navegar al directorio del proyecto
cd ADR-Metasploit\API

# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual
env\Scripts\activate
```

Linux/macOS (Bash):
```bash
# Navegar al directorio del proyecto
cd ADR-Metasploit/API

# Crear el entorno virtual
python3 -m venv env

# Activar el entorno virtual
source env/bin/activate
```

### 2. Instalar dependencias

Windows (CMD):
```cmd
# Con el entorno virtual activado
python -m pip install -r requirements.txt
```

Linux/macOS (Bash):
```bash
# Con el entorno virtual activado
pip install -r requirements.txt
```

### 3. Configurar la base de datos

Windows (CMD):
```cmd
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS (Bash):
```bash
./manage.py makemigrations
./manage.py migrate
```

### 4. Crear un superusuario (para acceder a la API)

Windows (CMD):
```cmd
python manage.py createsuperuser
```

Linux/macOS (Bash):
```bash
./manage.py createsuperuser
```

### 5. Iniciar el servidor de desarrollo

Windows (CMD):
```cmd
python manage.py runserver
```

Linux/macOS (Bash):
```bash
./manage.py runserver
```
El servidor estará disponible en `http://127.0.0.1:8000/`.

## Autenticación
Esta API utiliza autenticación por token (DRF Token Authentication). Para obtener un token, realiza un POST a `/api/token-auth/` con tu usuario y contraseña de Django:

```
POST /api/token-auth/
{
	"username": "<usuario>",
	"password": "<contraseña>"
}
```
El token devuelto debe ser enviado en el header `Authorization` de tus requests:

```
Authorization: Token <tu_token>
```

Todos los endpoints requieren autenticación, excepto la obtención del token.

## Ejemplos de Uso

### Gestión de Tareas (Tasks)

#### Crear una tarea
```http
POST /api/tasks/
Authorization: Token <tu_token>
Content-Type: application/json

{
    "title": "Probar MSFconsole",
    "description": "Realizar pruebas iniciales con la consola de Metasploit",
    "completed": false
}
```

#### Listar todas las tareas
```http
GET /api/tasks/
Authorization: Token <tu_token>
```

#### Obtener una tarea específica
```http
GET /api/tasks/1/
Authorization: Token <tu_token>
```

#### Actualizar una tarea
```http
PUT /api/tasks/1/
Authorization: Token <tu_token>
Content-Type: application/json

{
    "title": "Probar MSFconsole",
    "description": "Pruebas completadas con la consola de Metasploit",
    "completed": true
}
```

#### Eliminar una tarea
```http
DELETE /api/tasks/1/
Authorization: Token <tu_token>
```

#### Respuestas de ejemplo

Crear/Obtener tarea:
```json
{
    "id": 1,
    "title": "Probar MSFconsole",
    "description": "Realizar pruebas iniciales con la consola de Metasploit",
    "completed": false,
    "created_at": "2025-10-20T14:30:00Z",
    "updated_at": "2025-10-20T14:30:00Z"
}
```

Listar tareas:
```json
[
    {
        "id": 1,
        "title": "Probar MSFconsole",
        "description": "Realizar pruebas iniciales con la consola de Metasploit",
        "completed": false,
        "created_at": "2025-10-20T14:30:00Z",
        "updated_at": "2025-10-20T14:30:00Z"
    }
]
```

### Endpoint de Ping
```http
GET /api/ping/
Authorization: Token <tu_token>
```

Respuesta:
```json
{
    "ping": "pong"
}
```

## Autores
- Agustín Cucchiarelli
- Emiliano Di Grappa
- Máximo Preneste
- Gustavo Senna

## Notas
Este proyecto fue generado y asistido con la ayuda de un agente de Inteligencia Artificial para acelerar el desarrollo y asegurar buenas prácticas.

---

> Trabajo de investigación para la materia Administración de Sistemas de Información, UTN FRLP.
