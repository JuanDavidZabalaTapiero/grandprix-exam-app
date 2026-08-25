# Flask Architecture Lab

Proyecto experimental desarrollado en Python con Flask para practicar y explorar una arquitectura por capas, separando responsabilidades entre repositorios, servicios, rutas, APIs y la capa de presentación.

La aplicación utiliza la siguiente estructura: **Repository → Service → Route / API → JavaScript → HTML**

El objetivo principal del proyecto es experimentar con esta arquitectura y evaluar cómo organizar una aplicación Flask de forma clara, modular y mantenible.

---

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.12
- **Framework Web:** Flask 3.1.3
- **ORM / Base de Datos:** Flask-SQLAlchemy 3.1.1, Flask-Migrate 4.1.0 (Alembic), MySQL (Driver `mysqlclient`)
- **Formularios y Validación:** Flask-WTF 1.3.0 / WTForms
- **Pruebas Automatizadas:** Pytest 9.1.1
- **Variables de Entorno:** python-dotenv
- **Contenerización:** Docker

---

## 🏛️ Arquitectura y Patrones

El proyecto sigue una **Arquitectura en Capas (Layered Architecture)** con separación clara de responsabilidades:

1. **Vistas / Rutas (`app/routes`):** Manejan las peticiones HTTP y renderizan plantillas Jinja2 o redirecciones.
2. **Formularios (`app/forms`):** Definen la validación y normalización de entradas de datos con Flask-WTF.
3. **Servicios (`app/services`):** Encapsulan la lógica de negocio. Coordinan las transacciones de base de datos (`commit`) y aplican el decorador de manejo global de excepciones `@handle_exceptions`.
4. **Repositorios (`app/repositories`):** Realizan consultas a la base de datos utilizando el ORM SQLAlchemy sin confirmar transacciones explícitamente (`commit`).
5. **Modelos (`app/database/models.py`):** Entidades de base de datos (`Student`, `Enrollment`, `LicenseCategory`, `Question`, `Option`, `Competence`, `Response`, etc.).

---

## 🚀 Iniciar Aplicación (Entorno Local)

### 1. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto tomando como referencia el siguiente esquema:

```env
SECRET_KEY=mi_llave_secreta
DB_URL=mysql+mysqldb://usuario:contraseña@localhost:3306/nombre_base_datos
TEST_DB_URL=mysql+mysqldb://usuario:contraseña@localhost:3306/nombre_base_datos_test
```

> **Nota:** Reemplaza los valores de `DB_URL` y `TEST_DB_URL` según tus credenciales locales de MySQL.

### 2. Crear Entorno Virtual y Activar

En Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar Dependencias del Sistema y Python

Asegúrate de contar con los paquetes de desarrollo para MySQL (`default-libmysqlclient-dev` y `pkg-config` en sistemas basados en Debian/Ubuntu) para compilar `mysqlclient`. Luego ejecuta:

```bash
pip install -r requirements.txt
```

### 4. Aplicar Migraciones de Base de Datos

```bash
flask db upgrade
```

### 5. Iniciar la Aplicación

```bash
python run.py
```

La aplicación se ejecutará por defecto en `http://localhost:5000`.

---

Aquí tienes la sección respetando estrictamente el orden que propusiste originalmente (descargando imágenes, creando contenedores por separado y luego conectándolos mediante la red), con los comandos completos y los valores genéricos:

---

## 🐋 Iniciar Aplicación con Docker

Sigue estos pasos para desplegar el entorno de desarrollo (Base de datos MySQL + Aplicación Flask) utilizando Docker.

---

### 1. Instalar la imagen e iniciar el contenedor de MySQL

1. **Descargar la imagen e iniciar el contenedor de MySQL:**

```bash
docker run -d \
  --name db-mysql \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=tu_contraseña_root \
  mysql:8.0
```

> **Nota:** Reemplaza `tu_contraseña_root` por una clave segura. Conserva este valor para configurar las cadenas de conexión (`DB_URL` y `TEST_DB_URL`).

2. **Crear la base de datos principal y de pruebas:**

Conéctate a MySQL en `localhost:3306` (usando MySQL Workbench, DBeaver o la terminal) con el usuario `root` y la contraseña configurada, luego ejecuta:

```sql
CREATE DATABASE nombre_base_datos;
CREATE DATABASE nombre_base_datos_test;
```

---

### 2. Construir la imagen de la aplicación Flask

Construye la imagen desde la raíz de tu proyecto:

```bash
docker build -t app-flask .
```

---

### 3. Crear e iniciar el contenedor de la aplicación Flask

Crea el contenedor asociando las variables de entorno y el volumen recomendado para sincronizar cambios de código en tiempo real:

```bash
docker run -d \
  --name contenedor-flask \
  -p 5000:5000 \
  -v "/ruta/absoluta/a/tu/proyecto:/app" \
  -e FLASK_APP=run.py \
  -e SECRET_KEY=tu_llave_secreta_super_segura \
  -e DB_URL=mysql+mysqldb://root:tu_contraseña_root@db-mysql/nombre_base_datos \
  -e TEST_DB_URL=mysql+mysqldb://root:tu_contraseña_root@db-mysql/nombre_base_datos_test \
  app-flask

```

> **Notas sobre los valores:**
>
> - En el volumen (`-v`), sustituye `/ruta/absoluta/a/tu/proyecto` por la ruta local de tu repositorio (ejemplo en Windows: `C:\ruta\al\proyecto`).
> - Reemplaza `nombre_base_datos` y `nombre_base_datos_test` por los nombres que creaste en el paso 1.

---

### 4. Crear la red y conectar ambos contenedores

1. **Crear la red puente (_bridge_):**

```bash
docker network create mi-red
```

2. **Conectar ambos contenedores (deben estar activos):**

```bash
docker network connect mi-red db-mysql
docker network connect mi-red contenedor-flask
```

---

### 5. Aplicar migraciones de la base de datos

Aplica las migraciones de Flask-Migrate / Alembic dentro del contenedor de la aplicación:

```bash
docker exec -it contenedor-flask flask db upgrade
```

---

### 6. Comandos para ejecutar/gestionar el contenedor de Flask

Si el contenedor no está activo o necesitas pausarlo/reiniciarlo:

- **Iniciar contenedor:**

```bash
docker start contenedor-flask
```

- **Detener contenedor:**

```bash
docker stop contenedor-flask
```

---

### 🧪 Ejecución de la suite de pruebas con Pytest

- **En entorno local:**

```bash
pytest
```

- **Desde Docker:**

```bash
docker exec -it contenedor-flask python -m pytest
```
