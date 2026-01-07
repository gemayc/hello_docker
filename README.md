# 🐳 Hello Docker 

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

Mini aplicación web en **Python + Streamlit** creada para aprender **Docker paso a paso**.

---

## 🎯 Objetivo del ejercicio

Con este proyecto aprenderás a:

- ✅ Ejecutar una aplicación web en Python en local
- ✅ Crear tu propio Dockerfile
- ✅ Construir una imagen Docker
- ✅ Ejecutar un contenedor
- ✅ Etiquetar tu imagen para Docker Hub
- ✅ Subir tu imagen a Docker Hub
- ✅ Ejecutar la app desde Docker Hub

---

## 📁 Estructura del proyecto
```
hello_docker/
│
├── app.py              # Aplicación Streamlit
├── requirements.txt    # Dependencias Python
├── Dockerfile          # Instrucciones para Docker
└── README.md          # Este archivo
```

---

## 🚀 PARTE 1: Ejecutar la aplicación en local

Antes de dockerizar, vamos a probar que todo funciona correctamente.

### 1️⃣ Crear entorno virtual
```bash
python -m venv venv
```

### 2️⃣ Activar el entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la aplicación
```bash
streamlit run app.py
```

🎉 La aplicación debería abrirse automáticamente en `http://localhost:8501`

---

## 🐳 PARTE 2: Dockerizar la aplicación

Ahora vamos a crear un contenedor Docker para que la aplicación pueda ejecutarse en cualquier lugar.

### 📝 Paso 1: Crear el Dockerfile

Crea un archivo llamado `Dockerfile` (sin extensión) en la raíz del proyecto y añade el siguiente contenido:
```dockerfile
# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app.py .

# Exponer el puerto 8501 (puerto por defecto de Streamlit)
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```

#### 🔍 ¿Qué hace cada línea?

- `FROM python:3.11-slim` → Usa una imagen ligera de Python 3.11
- `WORKDIR /app` → Crea y establece `/app` como directorio de trabajo
- `COPY requirements.txt .` → Copia el archivo de dependencias al contenedor
- `RUN pip install...` → Instala las dependencias de Python
- `COPY app.py .` → Copia el código de la aplicación
- `EXPOSE 8501` → Indica que el contenedor escucha en el puerto 8501
- `CMD [...]` → Comando que se ejecuta al iniciar el contenedor

---

### 🏗️ Paso 2: Construir la imagen Docker

Abre una terminal en la carpeta del proyecto y ejecuta:
```bash
docker build -t hello_docker .
```

#### ¿Qué hace este comando?

- `docker build` → Construye una imagen Docker
- `-t hello_docker` → Asigna un nombre (tag) a la imagen
- `.` → Indica que el Dockerfile está en el directorio actual

---

### ▶️ Paso 3: Ejecutar el contenedor

Una vez construida la imagen, ejecuta:
```bash
docker run -p 8501:8501 hello_docker
```

#### ¿Qué hace este comando?

- `docker run` → Ejecuta un contenedor desde una imagen
- `-p 8501:8501` → Mapea el puerto 8501 del contenedor al puerto 8501 de tu máquina
- `hello_docker` → Nombre de la imagen a ejecutar

🎉 Abre tu navegador en `http://localhost:8501` y verás tu aplicación corriendo en Docker.

---

## 🌍 PARTE 3: Subir tu imagen a Docker Hub

Para compartir tu imagen con otros o ejecutarla en cualquier máquina, necesitas subirla a Docker Hub.

### Paso 0: Crear cuenta en Docker Hub (si no la tienes)

1. Ve a [hub.docker.com](https://hub.docker.com)
2. Crea una cuenta gratuita
3. Anota tu nombre de usuario (lo necesitarás en los siguientes pasos)

### 1️⃣ Iniciar sesión en Docker Hub
```bash
docker login
```

Introduce tu usuario y contraseña de Docker Hub.

### 2️⃣ Etiquetar la imagen con tu usuario y versión

Antes de subir la imagen, necesitas etiquetarla con tu nombre de usuario de Docker Hub y una versión:
```bash
docker tag hello_docker TU_USUARIO/hello_docker:v1.0
docker tag hello_docker TU_USUARIO/hello_docker:latest
```

**Ejemplos:**
- Si tu usuario es `gema`: 
```bash
  docker tag hello_docker gema/hello_docker:v1.0
  docker tag hello_docker gema/hello_docker:latest
```
- Si tu usuario es `juan123`: 
```bash
  docker tag hello_docker juan123/hello_docker:v1.0
  docker tag hello_docker juan123/hello_docker:latest
```

#### 🔍 ¿Por qué hacer esto?

- **Usuario:** Docker Hub organiza las imágenes por usuario (como GitHub con los repositorios). El formato es: `usuario/nombre-imagen:version`
- **Versión (`v1.0`):** Identifica versiones específicas de tu aplicación. Útil para mantener diferentes releases.
- **Tag `latest`:** Apunta siempre a la versión más reciente. Es la que se descarga por defecto si no especificas versión.

> 💡 **Buena práctica:** Siempre etiqueta con una versión específica (`v1.0`, `v2.0`) Y con `latest`. Así los usuarios pueden elegir una versión concreta o usar siempre la última.

### 3️⃣ Subir las imágenes
```bash
docker push TU_USUARIO/hello_docker:v1.0
docker push TU_USUARIO/hello_docker:latest
```

**Ejemplo:**
```bash
docker push gema/hello_docker:v1.0
docker push gema/hello_docker:latest
```

✅ Tu imagen ya está disponible públicamente en Docker Hub con ambas etiquetas.

---

## ⬇️ PARTE 4: Ejecutar la app desde Docker Hub

Cualquier persona puede ejecutar tu aplicación de estas formas:

**Usando la versión específica:**
```bash
docker run -p 8501:8501 TU_USUARIO/hello_docker:v1.0
```

**Usando la última versión (latest):**
```bash
docker run -p 8501:8501 TU_USUARIO/hello_docker:latest
```

**Sin especificar versión (descarga `latest` por defecto):**
```bash
docker run -p 8501:8501 TU_USUARIO/hello_docker
```

**Ejemplo:**
```bash
docker run -p 8501:8501 gema/hello_docker:v1.0
```

Docker descargará automáticamente la imagen desde Docker Hub y la ejecutará.

> 💡 **Tip:** Si haces cambios en tu app y quieres subir una nueva versión, cambia el número de versión (ej: `v2.0`) y repite los pasos de etiquetado y push.

---

## 🛠️ Comandos útiles de Docker
```bash
# Ver imágenes locales
docker images

# Ver contenedores en ejecución
docker ps

# Ver todos los contenedores (incluyendo detenidos)
docker ps -a

# Detener un contenedor
docker stop <container_id>

# Eliminar un contenedor
docker rm <container_id>

# Eliminar una imagen
docker rmi <image_name>

# Ver logs de un contenedor
docker logs <container_id>

# Ejecutar contenedor en segundo plano (detached mode)
docker run -d -p 8501:8501 hello_docker
```

---

## 📊 Resumen del flujo completo
```
1. Crear Dockerfile
   ↓
2. docker build -t hello_docker .
   ↓
3. docker run -p 8501:8501 hello_docker
   ↓
4. docker login
   ↓
5. docker tag hello_docker TU_USUARIO/hello_docker:v1.0
   docker tag hello_docker TU_USUARIO/hello_docker:latest
   ↓
6. docker push TU_USUARIO/hello_docker:v1.0
   docker push TU_USUARIO/hello_docker:latest
   ↓
7. Cualquiera puede ejecutar: 
   docker run -p 8501:8501 TU_USUARIO/hello_docker:v1.0
   o
   docker run -p 8501:8501 TU_USUARIO/hello_docker
```

---

## ❓ Preguntas frecuentes

### ¿Qué es Docker?
Docker es una plataforma que permite empaquetar aplicaciones y sus dependencias en contenedores, asegurando que funcionen igual en cualquier entorno.

### ¿Qué es una imagen Docker?
Es una plantilla de solo lectura que contiene todo lo necesario para ejecutar una aplicación (código, dependencias, configuración).

### ¿Qué es un contenedor Docker?
Es una instancia en ejecución de una imagen Docker. Es ligero, aislado y portable.

### ¿Por qué necesito etiquetar mi imagen antes de subirla?
Docker Hub organiza las imágenes por usuario. Al etiquetar con `usuario/nombre`, Docker sabe a qué cuenta pertenece la imagen.

### ¿Puedo tener varias versiones de la misma imagen?
Sí, puedes usar tags adicionales:
```bash
docker tag hello_docker gema/hello_docker:v1.0
docker tag hello_docker gema/hello_docker:latest
```

### ¿Por qué usar Docker?
- ✅ Mismo entorno en desarrollo, testing y producción
- ✅ Fácil distribución de aplicaciones
- ✅ Aislamiento entre aplicaciones
- ✅ Escalabilidad y eficiencia

---

## 📚 Recursos adicionales

- [Documentación oficial de Docker](https://docs.docker.com/)
- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Docker Hub](https://hub.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

## 💡 Consejos para principiantes

1. **¿Error al construir?** → Asegúrate de estar en la carpeta correcta (donde está el Dockerfile)
2. **¿Puerto ocupado?** → Cambia el puerto: `docker run -p 8502:8501 hello_docker`
3. **¿Cambios no se reflejan?** → Reconstruye la imagen: `docker build -t hello_docker .`
4. **¿Contenedor no se detiene?** → Usa `Ctrl+C` o `docker stop <container_id>`
5. **¿Olvidaste tu container_id?** → Usa `docker ps` para verlo

---

## 💪 ¡Enhorabuena!

Si has llegado hasta aquí, ya sabes cómo dockerizar una aplicación Python. Este conocimiento es fundamental en el desarrollo de software moderno.

---

<div align="center">

**Proyecto realizado por Gema Yébenes con ❤️ para aprender Docker**

![Docker Logo](https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png)

</div>