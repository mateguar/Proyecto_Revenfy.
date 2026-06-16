# Especificación de Requisitos de Software (SRS)

## Proyecto: Revenfy  
**Versión:** 1.0  
**Fecha:** 28 de mayo de 2026  

---

## Autores
- Anamaria Forigua Murcia  
- Luis Mateo Beltrán Repizo  
- Jhon Alex Beltrán Herrera  
---

## Tabla de Contenido
1. Introducción  
   - 1.1 Alcance del producto  
   - 1.2 Valor del producto  
   - 1.3 Público objetivo  
   - 1.4 Uso previsto  
   - 1.5 Descripción general  
2. Requisitos funcionales  
3. Requisitos de interfaz externa  
   - 3.1 Interfaz de usuario  
   - 3.2 Interfaz de hardware  
   - 3.3 Interfaz de software  
   - 3.4 Interfaz de comunicación  
4. Requisitos no funcionales  
5. Definiciones y acrónimos  
6. Referencias  

---

## 1. Introducción

Este documento describe los requisitos funcionales, no funcionales y técnicos del sistema Revenfy.

Su propósito es definir de manera clara el comportamiento esperado de la aplicación, sus características principales, restricciones técnicas y necesidades de interfaz para su desarrollo e implementación.

Revenfy será una aplicación móvil enfocada en la compra y venta de productos de segunda mano, permitiendo que los usuarios publiquen, busquen y gestionen productos de forma sencilla y segura dentro de una plataforma digital.

---

### 1.1 Alcance del producto

Revenfy es una plataforma móvil diseñada para conectar personas interesadas en vender, comprar o intercambiar productos de segunda mano.

**Objetivos**
- Facilitar la publicación de productos usados.
- Promover la economía circular mediante la reutilización de ropa.
- Crear una comunidad digital enfocada en moda sostenible.
- Ofrecer una experiencia sencilla de compra y venta entre usuarios.

**Beneficios**
- Reduce el desperdicio textil.
- Da una segunda vida útil a prendas usadas.
- Genera ingresos a usuarios vendedores.
- Permite encontrar prendas a menor costo.

---

### 1.2 Valor del producto

Revenfy aporta valor al usuario al ofrecer un espacio digital cómodo y accesible para comercializar productos usados.

Los usuarios podrán:
- Vender productos que ya no usan.
- Encontrar productos a precios accesibles.
- Descubrir artículos únicos.
- Participar en consumo responsable y sostenible.

---

### 1.3 Público objetivo

- Jóvenes entre 16 y 35 años.
- Compradores de productos de segunda mano.
- Vendedores independientes de productos usados.
- Personas que buscan monetizar productos que ya no utilizan.

---

### 1.4 Uso previsto

El usuario podrá:
- Registrarse en la aplicación.
- Iniciar sesión.
- Crear publicaciones de Productos usados.
- Subir fotografías de productos.
- Agregar descripción, estado, categoría y precio.
- Buscar productos publicados.
- Visualizar perfiles.
- Contactar otros usuarios.
- Administrar sus publicaciones.

---

### 1.5 Descripción general

El sistema contará con:
- Autenticación de usuarios.
- Perfil personal.
- Gestión de publicaciones.
- Catálogo de productos.
- Motor de búsqueda.
- Carga de imágenes.
- Visualización detallada del producto.
- Mensajería o contacto entre usuarios.

---

## 2. Requisitos Funcionales

| Código | Requisito |
|--------|----------|
| RF01 | Registro de usuario |
| RF02 | Inicio de sesión |
| RF03 | Gestión de perfil |
| RF04 | Publicación de productos |
| RF05 | Carga de imágenes |
| RF06 | Búsqueda de productos |
| RF07 | Visualización del producto |
| RF08 | Gestión de publicaciones |
| RF09 | Comunicación entre usuarios |
| RF10 | Navegación dentro de la aplicación |
| RF11 | Gestión de favoritos |
| RF12 | Notificaciones |
| RF13 | Historial de publicaciones |
| RF14 | Calificación de usuarios |
| RF15 | Reporte de publicaciones |

---

## 3. Requisitos de Interfaz Externa

### 3.1 Interfaz de Usuario
- Interfaz visual clara e intuitiva.
- Navegación sencilla entre pantallas.
- Diseño adaptable a dispositivos móviles.
- Menú accesible desde pantalla principal.
- Botones visibles y de fácil interacción.

---

### 3.2 Interfaz de Hardware
- Teléfonos Android.
- Dispositivos iOS.
- Acceso a cámara.
- Acceso a galería.
- Conexión a internet.
- Almacenamiento temporal de imágenes.

---

### 3.3 Interfaz de Software

- Frontend: Flutter  
- Backend: FastAPI  
- Base de Datos: PostgreSQL  
- Arquitectura: API REST  

---

### 3.4 Interfaz de Comunicación
- HTTP / HTTPS  
- API REST  
- JSON  
- Transferencia de imágenes  
- Comunicación cliente-servidor  

---

## 4. Requisitos No Funcionales

### 4.1 Seguridad
- Protección de credenciales.
- Autenticación segura.
- Protección de datos personales.
- Acceso restringido.

---

### 4.2 Capacidad
- Soporte para múltiples usuarios simultáneos.
- Almacenamiento continuo de publicaciones.
- Gestión de imágenes.
- Crecimiento progresivo de la base de datos.

---

### 4.3 Compatibilidad
- Android 8+
- iOS 13+
- Diferentes tamaños de pantalla.

---

### 4.4 Confiabilidad
- Disponibilidad estable.
- Funcionamiento continuo.
- Minimización de errores críticos.

---

### 4.5 Escalabilidad
- Incremento de usuarios.
- Incremento de publicaciones.
- Nuevas categorías.
- Nuevos módulos.

---

### 4.6 Mantenibilidad
- Arquitectura modular.
- Separación Frontend/Backend.
- Documentación técnica.
- Facilidad de corrección y mejora.

---

### 4.7 Facilidad de uso
- Interfaz intuitiva.
- Navegación simple.
- Aprendizaje rápido.
- Procesos cortos de publicación.

---

### 4.8 Otros requisitos
- Buen rendimiento.
- Tiempos rápidos de carga.
- Diseño responsive.
- Estabilidad de conexión.
- Experiencia visual consistente.

---

## 5. Definiciones y Acrónimos

| Término | Definición |
|--------|------------|
| API | Interfaz que permite comunicación entre sistemas |
| Backend | Lógica de negocio y acceso a datos |
| Frontend | Interfaz visual del sistema |
| UI | User Interface |
| UX | User Experience |
| RF | Requisito Funcional |
| RNF | Requisito No Funcional |
| SRS | Software Requirements Specification |

---

## 6. Referencias
- IEEE 830 - Software Requirements Specification  
- Documentación oficial de Flutter  
- Documentación oficial de FastAPI  
- Documentación oficial de PostgreSQL  
