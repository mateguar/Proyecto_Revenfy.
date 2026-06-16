# Revenfy

> Plataforma web de compra y venta de productos de segunda mano para aprendices e instructores del CGMLTI – SENA, Bogotá.

---

## ¿Qué es Revenfy?

**Revenfy** (Revender + fy) es un aplicativo web desarrollado en el SENA que ofrece un entorno digital controlado, seguro y organizado para que aprendices e instructores puedan comprar y vender productos de segunda mano. A diferencia de plataformas abiertas como Facebook Marketplace, Revenfy está pensado exclusivamente para la comunidad interna del CGMLTI, fomentando competencias empresariales, la economía circular y el emprendimiento.

---

## Equipo

| Nombre | Rol |
|---|---|
| Luis Mateo Beltrán Repizo | Desarrollador |
| Jhon Alex Beltrán Herrera | Desarrollador |
| Anamaria Forigua Murcia | Desarrolladora |

---

## Stack tecnológico

### Front-end (Prototipos HTML)
- **HTML5** — estructura de las páginas
- **CSS3** — estilos globales en `styles.css`
- **JavaScript (Vanilla ES6)** — lógica de interacción en el cliente
- **Bootstrap 5** — grid y componentes en `index.html`
- **Bootstrap Icons / Font Awesome** — íconos en la interfaz
- **Google Fonts** — tipografías *Changa One* y *Montserrat*

### Back-end (Python)
- **Python 3** — lógica del servidor y modelos de datos
- **SQLite** — base de datos local (`conexionSqlite.py`)
- **ABC (Abstract Base Classes)** — arquitectura orientada a objetos con clase base abstracta `EntidadBase`

### Almacenamiento temporal (prototipo)
- **localStorage** del navegador — se usa en el prototipo HTML para simular autenticación y gestión de sesión/rol (no reemplaza una base de datos real)

---

## Estructura del proyecto

```
revenfy/
│
├── index.html          # Página de inicio / landing page
├── login.html          # Inicio de sesión
├── registrarse.html    # Registro de nuevo usuario
├── rol.html            # Selección de rol (Comprador / Vendedor / Ambos)
├── dashboard.html      # Panel principal del usuario
├── styles.css          # Estilos globales de toda la aplicación
│
├── js/
│   ├── script.js       # Lógica del menú hamburguesa (index)
│   ├── login.js        # Autenticación y visibilidad de contraseña
│   ├── registrarse.js  # Validación y registro de usuario
│   ├── rol.js          # Selección y guardado del rol
│   └── dashboard.js    # Sidebar responsive y cierre de sesión
│
├── Revenfy.png         # Logo oficial del proyecto
│
└── python/
    ├── main.py             # Punto de entrada de la aplicación Python
    ├── conexionSqlite.py   # Módulo de conexión a la base de datos SQLite
    ├── entidadBase.py      # Clase abstracta base para todas las entidades
    ├── usuario.py          # Modelo de datos del usuario
    └── producto.py         # Modelo de datos del producto
```

---

## Cómo visualizar los prototipos HTML

No se requiere servidor ni instalación. Solo necesitas un navegador moderno (Chrome, Firefox, Edge).

**Pasos:**

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/revenfy.git
   cd revenfy
   ```

2. Abre el archivo `index.html` directamente en tu navegador:
   - En Windows: clic derecho → *Abrir con* → Chrome
   - En Mac/Linux: doble clic sobre el archivo

3. Desde la landing page puedes navegar a:
   - `login.html` → Iniciar sesión
   - `registrarse.html` → Crear cuenta
   - `rol.html` → Elegir rol (redirige automáticamente tras el login)
   - `dashboard.html` → Panel principal (requiere sesión activa)

> **Nota:** El prototipo usa `localStorage` para simular la sesión. Si accedes directamente a `dashboard.html` sin haberte registrado antes, serás redirigido al login automáticamente.

**Flujo completo de prueba:**
```
Registrarse → Iniciar Sesión → Elegir Rol → Dashboard
```

---

## Cómo ejecutar el código Python

### Requisitos previos

- Python 3.8 o superior
- No se requieren librerías externas (solo módulos de la biblioteca estándar)

Verifica tu versión:
```bash
python --version
```

### Instalación

```bash
git clone https://github.com/tu-usuario/revenfy.git
cd revenfy/python
```

### Ejecución

```bash
python main.py
```

### Descripción de los módulos Python

| Archivo | Descripción |
|---|---|
| `main.py` | Punto de entrada principal. Inicializa la aplicación. |
| `conexionSqlite.py` | Gestiona la conexión con la base de datos SQLite. |
| `entidadBase.py` | Clase abstracta (`ABC`) que define el contrato base para todas las entidades con el método `guardarEnBase()`. |
| `usuario.py` | Modelo que representa un usuario de la plataforma. Hereda de `EntidadBase`. |
| `producto.py` | Modelo que representa un producto publicado. Hereda de `EntidadBase`. |

---

## Funcionalidades actuales (prototipo)

- Registro de usuario con validación de contraseñas
- Inicio de sesión con credenciales guardadas en localStorage
- Selección de rol: Comprador, Vendedor o Ambos
- Dashboard personalizado según el rol del usuario
- Navegación responsive con menú hamburguesa en móviles
- Cierre de sesión

---

## Próximas funcionalidades

- Sistema de calificaciones entre compradores y vendedores
- Categorías de productos (ropa, tecnología, libros, etc.)
- Filtros avanzados de búsqueda
- Historial de compras y ventas
- Sistema de notificaciones
- Validación de usuarios por correo institucional SENA
- Sistema de reportes de usuarios o productos sospechosos
- Métricas de desempeño comercial

---

## Contexto académico

Proyecto desarrollado en el **CGMLTI del SENA**, Bogotá, como parte de la formación en tecnologías de la información. Busca fortalecer competencias empresariales alineadas con la economía circular y el uso responsable de la tecnología.
