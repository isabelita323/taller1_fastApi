# 🎓 Trainees API + CLI

API REST para la **gestión de aprendices**, construida con **FastAPI** 🚀 y **MongoDB** 🍃, desplegada en **Render** ☁️, junto con una **interfaz de consola (CLI)** 💻 que consume la API.

🌐 **API en producción:** https://t1-fastapi-jk1f.onrender.com
📖 **Documentación interactiva (Swagger):** https://t1-fastapi-jk1f.onrender.com/docs

---

## 📋 Tabla de contenido

- [✨ Qué se ha hecho](#-qué-se-ha-hecho)
- [🛠️ Tecnologías](#️-tecnologías)
- [📁 Estructura del proyecto](#-estructura-del-proyecto)
- [⚙️ Instalación](#️-instalación)
- [▶️ Ejecutar la API en local](#️-ejecutar-la-api-en-local)
- [💻 Usar el CLI](#-usar-el-cli)
- [🔗 Endpoints](#-endpoints)
- [🧾 Campos del aprendiz](#-campos-del-aprendiz)
- [☁️ Despliegue en Render](#️-despliegue-en-render)
- [🐞 Problemas encontrados y cómo se resolvieron](#-problemas-encontrados-y-cómo-se-resolvieron)
- [👩‍💻 Autora](#-autora)

---

## ✨ Qué se ha hecho

- ✅ API REST con **FastAPI** y operaciones **CRUD** completas sobre aprendices.
- ✅ Validación de datos con **Pydantic** (incluido el correo con `EmailStr`).
- ✅ Conexión a una base de datos **MongoDB** con **PyMongo**.
- ✅ Despliegue de la API en **Render** desde GitHub.
- ✅ Interfaz de consola (`views.py`) con menú interactivo para consumir la API con **requests**.
- ✅ Manejo de errores en el CLI: tiempo de espera agotado, falta de conexión y respuestas de error de la API.
- ✅ Documentación del proyecto en este README.

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|------------|-----|
| 🐍 Python | Lenguaje principal |
| ⚡ FastAPI | Framework de la API |
| 🦄 Uvicorn | Servidor ASGI |
| 🧩 Pydantic + `email-validator` | Modelos y validación de datos |
| 🍃 PyMongo | Conexión con MongoDB |
| 🌍 Requests | Consumo de la API desde el CLI |
| ☁️ Render | Hosting de la API |

---

## 📁 Estructura del proyecto

```
.
├── src/
│   ├── main.py              # 🚪 Punto de entrada de la API
│   ├── models/
│   │   └── model.py         # 🧩 Modelos Pydantic (TraineeModel, TraineeUpdateModel)
│   └── templates/
│       └── controllers.py   # 🎮 Lógica de cada operación
├── views.py                 # 💻 Interfaz de consola (CLI)
├── requeriments.txt         # 📦 Dependencias
└── README.md                # 📖 Este archivo
```

---

## ⚙️ Instalación

1. 📥 Clona el repositorio:
   ```bash
   git clone https://github.com/Mapu0825/t1_pyfastApi.git
   cd t1_pyfastApi
   ```
2. 🧪 Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux / macOS
   source .venv/bin/activate
   ```
3. 📦 Instala las dependencias:
   ```bash
   pip install -r requeriments.txt
   ```

---

## ▶️ Ejecutar la API en local

```bash
uvicorn src.main:app --reload
```

La API quedará disponible en http://127.0.0.1:8000 y su documentación en http://127.0.0.1:8000/docs 🎉

---

## 💻 Usar el CLI

```bash
python views.py
```

> ⏳ **Ojo:** la API está en el plan gratuito de Render. Si lleva un rato sin uso, la primera petición puede tardar hasta un minuto en responder mientras el servicio "despierta".

### 🧭 Menú

| Opción | Acción |
|--------|--------|
| 1️⃣ | 📋 Listar todos los aprendices |
| 2️⃣ | 🔍 Buscar aprendiz por ID |
| 3️⃣ | ➕ Crear aprendiz |
| 4️⃣ | ✏️ Actualizar aprendiz |
| 5️⃣ | 🗑️ Eliminar aprendiz |
| 0️⃣ | 👋 Salir |

---

## 🔗 Endpoints

**Base URL:** `https://t1-fastapi-jk1f.onrender.com/trainees`

| Método | Ruta | Descripción |
|--------|------|-------------|
| 🟢 GET | `/trainees/` | Obtener todos los aprendices |
| 🟢 GET | `/trainees/{id}` | Obtener un aprendiz por ID |
| 🟡 POST | `/trainees/` | Registrar un nuevo aprendiz |
| 🔵 PUT | `/trainees/{id}` | Actualizar un aprendiz |
| 🔴 DELETE | `/trainees/{id}` | Eliminar un aprendiz |

---

## 🧾 Campos del aprendiz

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `document` | texto | 🪪 Documento de identidad |
| `firstname` | texto | 🙋 Nombres |
| `lastname` | texto | 🙋 Apellidos |
| `email` | email | 📧 Correo electrónico |
| `age` | entero | 🎂 Edad |
| `program` | texto | 📚 Programa de formación |
| `record_number` | entero | 🔢 Número de ficha |

---

## ☁️ Despliegue en Render

- 🔨 **Build Command:** `pip install -r requeriments.txt`
- 🚀 **Start Command:** `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
- 🔐 **Variables de entorno:** la cadena de conexión a MongoDB se configura en **Environment** de Render (no se sube a GitHub).

---

## 🐞 Problemas encontrados y cómo se resolvieron

| # | Problema | Solución |
|---|----------|----------|
| 1 | ❌ `Could not open requirements file: No such file or directory` | 📄 El archivo de dependencias no estaba en la raíz o tenía otro nombre. Se creó y se subió al repo, y el Build Command se ajustó a su nombre. |
| 2 | ❌ `ImportError: email-validator is not installed` | 📧 `EmailStr` necesita `email-validator`. Se agregó al archivo de dependencias. |
| 3 | ❌ `No matching distribution found for email-validation` | ✍️ El nombre del paquete estaba mal escrito. El correcto es `email-validator`. |
| 4 | ❌ `404 Not Found` desde el CLI | 🔗 La ruta correcta es `/trainees` (plural), no `/trainee`. Se corrigió la URL base. |

---

## 👩‍💻 Autora

**Isabella Zzambrano** 💜 —[https://github.com/isabelita323/taller1_fastApi.git]