
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

## Autores
- Agustín Cucchiarelli
- Emiliano Di Grappa
- Máximo Preneste
- Gustavo Senna

## Notas
Este proyecto fue generado y asistido con la ayuda de un agente de Inteligencia Artificial para acelerar el desarrollo y asegurar buenas prácticas.

---

> Trabajo de investigación para la materia Administración de Sistemas de Información, UTN FRLP.
