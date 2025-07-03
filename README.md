# 🏫 ProyectoEscuelas

**ProyectoEscuelas** es una plataforma educativa integral desarrollada para digitalizar, automatizar y mejorar la gestión interna de instituciones escolares de nivel secundario. Está orientada a facilitar la administración de alumnos, materias, horarios, notas y asistencia, con interfaces personalizadas para cada tipo de usuario: **Administrador**, **Profesor** y **Alumno**.

---

## 🚀 Tecnologías utilizadas

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-%23000.svg?logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-e34c26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-264de4?logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563d7c?logo=bootstrap&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)

---

## 🎯 Funcionalidades principales

### 👨‍💼 Administrador
- Gestión de usuarios: crear, editar, eliminar y asignar roles
- Asignación de profesores a materias y cursos
- Gestión de horarios por curso
- Envío de comunicados por rol o curso

### 👩‍🏫 Profesor
- Registro de asistencias por curso
- Carga de notas y materiales
- Visualización de su cronograma

### 👨‍🎓 Alumno
- Consulta de horarios, materias y cronograma
- Visualización de calificaciones y asistencias
- Recepción de comunicados

---

## 🧱 Estructura del proyecto

ProyectoEscuelas/
├── admin/ # Vistas y lógica del rol administrador
├── alumno/ # Vistas del alumno
├── profesor/ # Funciones del profesor
├── auth/ # Autenticación y login
├── backend/ # Conexión a base de datos y controladores
├── comunicados/ # Envío y visualización de comunicados
├── static/ # CSS, JS, imágenes
├── templates/ # Archivos HTML con Jinja2
├── app.py # Punto de entrada de la app
├── requirements.txt # Librerías necesarias
└── README.md # Este archivo


---

## ⚙️ Instalación y ejecución

### 1. Cloná el repositorio

```
bash
git clone https://github.com/valencastaldi/ProyectoEscuelas
cd ProyectoEscuelas
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
---

✨ Autor
Valen Castaldi
Desarrolladora de Aplicaciones | GitHub

📄 Licencia## 📄 Licencia

Este proyecto está licenciado bajo la [MIT License](https://opensource.org/licenses/MIT).  
Uso libre para fines académicos, educativos y personales.







