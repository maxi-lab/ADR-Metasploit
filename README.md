
# API de Experimentación con Metasploit

Este proyecto es una API desarrollada para experimentar y facilitar pruebas con Metasploit, en el marco del trabajo de investigación de la materia **Administración de Sistemas de Información** de la **Universidad Tecnológica Nacional, Facultad Regional La Plata (UTN FRLP)**.

## Objetivo
El objetivo principal de esta API es servir como entorno de pruebas y experimentación para integrar Metasploit, permitiendo a los alumnos explorar conceptos de seguridad informática y administración de sistemas.

## Tecnologías utilizadas
- **Django** y **Django REST Framework** (DRF) para la creación de la API.
- Python 3.x

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
