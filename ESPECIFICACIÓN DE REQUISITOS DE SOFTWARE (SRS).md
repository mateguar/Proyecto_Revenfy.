ESPECIFICACIÓN DE REQUISITOS DE SOFTWARE (SRS)
Nombre del proyecto:
Revenfy
Fecha:
28 de mayo de 2026
Versión:
1.0
Creado por:
Anamaria Forigua Murcia.
Luis Mateo Beltrán Repizo.
Jhon Alex Beltrán Herrera.
Brayan Santiago Suarez Piraquive.






TABLA DE CONTENIDO
Introducción
 1.1 Alcance del producto
 1.2 Valor del producto
 1.3 Público objetivo
 1.4 Uso previsto
 1.5 Descripción general
Requisitos funcionales
Requisitos de interfaz externa
 3.1 Requisitos de la interfaz de usuario
 3.2 Requisitos de la interfaz de hardware
 3.3 Requisitos de la interfaz de software
 3.4 Requisitos de la interfaz de comunicación
Requisitos no funcionales
 4.1 Seguridad
 4.2 Capacidad
 4.3 Compatibilidad
 4.4 Confiabilidad
 4.5 Escalabilidad
 4.6 Mantenibilidad
 4.7 Facilidad de uso
 4.8 Otros requisitos no funcionales
Definiciones y acrónimos
Referencias




Historial de revisiones
Versión
Autor
Descripción de la versión
Fecha de realización
1.0
Anamaria Forigua Murcia
Documento inicial de especificación de requisitos de software de Revenfy.
28/05/2026
1.0
Luis Mateo Beltrán Repizo
Revisión de requisitos funcionales.
28/05/2026
1.0
Jhon Alex Beltrán Herrera
Revisión de requisitos no funcionales.
28/05/2026
1.0
Brayan Santiago Suarez Piraquive
Revisión general y validación del documento.
28/05/2026


Historial de aprobaciones
Aprobador
Versión aprobada
Firma
Fecha
Pendiente
1.0
—
—


Historial de revisión
Revisor
Versión revisada
Firma
Fecha
Pendiente
1.0
—
—






1. Introducción
Este documento describe los requisitos funcionales, no funcionales y técnicos del sistema Revenfy.
Su propósito es definir de manera clara el comportamiento esperado de la aplicación, sus características principales, restricciones técnicas y necesidades de interfaz para su desarrollo e implementación.
Revenfy será una aplicación móvil enfocada en la compra y venta de ropa de segunda mano, permitiendo que los usuarios publiquen, busquen y gestionen productos de forma sencilla y segura dentro de una plataforma digital.

1.1 Alcance del producto
Revenfy es una plataforma móvil diseñada para conectar personas interesadas en vender, comprar o intercambiar ropa de segunda mano.
Objetivos
Facilitar la publicación de prendas usadas.
Promover la economía circular mediante la reutilización de ropa.
Crear una comunidad digital enfocada en moda sostenible.
Ofrecer una experiencia sencilla de compra y venta entre usuarios.
Beneficios
Reduce desperdicio textil.
Da segunda vida útil a prendas usadas.
Genera ingresos a usuarios vendedores.
Permite encontrar prendas a menor costo.

1.2 Valor del producto
Revenfy aporta valor al usuario al ofrecer un espacio digital cómodo y accesible para comercializar ropa usada.
Los usuarios podrán:
Vender prendas que ya no usan.
Encontrar ropa a precios accesibles.
Descubrir artículos únicos.
participar en consumo responsable y sostenible.
El producto genera impacto ambiental positivo al reducir residuos textiles y fomentar reutilización.

1.3 Público objetivo
Revenfy está dirigido principalmente a:
Jóvenes entre 16 y 35 años.
Personas interesadas en moda sostenible.
Compradores de ropa de segunda mano.
Vendedores independientes de prendas usadas.
Personas que buscan monetizar ropa que ya no utilizan.

1.4 Uso previsto
El usuario podrá utilizar Revenfy para:
Registrarse en la aplicación.
Iniciar sesión.
Crear publicaciones de ropa usada.
Subir fotografías de prendas.
Agregar descripción, talla, categoría y precio.
Buscar productos publicados.
Visualizar perfiles.
Contactar otros usuarios.
Administrar sus publicaciones.

1.5 Descripción general
Revenfy será una aplicación móvil desarrollada para dispositivos Android e iOS.
El sistema contará con:
Autenticación de usuarios.
Perfil personal.
Gestión de publicaciones.
Catálogo de prendas.
Motor de búsqueda.
Carga de imágenes.
Visualización detallada del producto.
Mensajería o contacto entre usuarios.
La plataforma busca ofrecer una experiencia visual simple, intuitiva y enfocada en la compraventa rápida de ropa de segunda mano.

2. Requisitos funcionales
Los principales requisitos funcionales del sistema son:
RF01 Registro de usuario
El sistema permitirá crear una cuenta mediante correo electrónico.
RF02 Inicio de sesión
El usuario podrá ingresar usando correo y contraseña.
RF03 Gestión de perfil
El usuario podrá editar su información personal.
RF04 Publicación de productos
El usuario podrá crear publicaciones de prendas.
RF05 Carga de imágenes
El sistema permitirá subir imágenes desde cámara o galería.
RF06 Búsqueda de productos
Los usuarios podrán buscar ropa por nombre, categoría o filtros.
RF07 Visualización del producto
Se mostrará detalle completo del producto publicado.
RF08 Gestión de publicaciones
El usuario podrá editar o eliminar publicaciones.
RF09 Comunicación entre usuarios
El sistema permitirá interacción o contacto entre comprador y vendedor.
RF10 Navegación dentro de la aplicación
El usuario podrá desplazarse entre las diferentes secciones de la app.

RF11 Gestión de favoritos
Permite guardar publicaciones de interés para consultarlas posteriormente. 
RF12 Notificaciones
Permite recibir avisos sobre actividades relevantes dentro de la aplicación. 
RF13 Historial de publicaciones
Permite consultar publicaciones activas, vendidas o eliminadas. 
RF14 Calificación de usuarios
Permite valorar la experiencia de compra o venta entre usuarios. 
RF15 Reporte de publicaciones
Permite reportar contenido inapropiado o que incumpla las normas de la plataforma. 


3. Requisitos de interfaz externa

3.1 Requisitos de la interfaz de usuario
Interfaz visual clara e intuitiva.
Navegación sencilla entre pantallas.
Diseño adaptable a dispositivos móviles.
Menú accesible desde pantalla principal.
Botones visibles y de fácil interacción.
Consistencia visual en colores, tipografía e iconografía.
Experiencia centrada en el usuario.

3.2 Requisitos de la interfaz de hardware
El sistema deberá funcionar en:
Teléfonos Android.
Dispositivos iOS
Acceso a cámara del dispositivo.
Acceso a galería de imágenes.
Conexión a internet móvil o Wi-Fi.
Almacenamiento local para carga temporal de imágenes.

3.3 Requisitos de la interfaz de software
Revenfy se integrará mediante:
Frontend: Flutter.
Backend: FastAPI.
Base de datos: PostgreSQL.
APIs REST para comunicación cliente-servidor.
Almacenamiento estructurado de usuarios, productos e imágenes.

3.4 Requisitos de la interfaz de comunicación
El sistema utilizará:
Protocolo HTTP/HTTPS.
Comunicación cliente-servidor vía API REST.
Transmisión de datos en formato JSON.
Carga y recepción de imágenes desde el dispositivo.
Envío y recuperación de información desde base de datos.

4. Requisitos no funcionales

4.1 Seguridad
Protección de credenciales de usuario.
Autenticación segura mediante login.
Protección de datos personales.
Acceso restringido a cuentas personales.
Almacenamiento seguro de información.

4.2 Capacidad
El sistema deberá soportar:
Múltiples usuarios registrados simultáneamente.
Almacenamiento continuo de publicaciones
Carga de imágenes por publicación.
Crecimiento progresivo de base de datos.

4.3 Compatibilidad
Revenfy deberá ser compatible con:
Android 8 o superior.
iOS 13 o superior.
Navegadores usados en panel administrativo si aplica.
Diferentes tamaños de pantalla móvil.

4.4 Confiabilidad
El sistema deberá mantener disponibilidad estable y funcionamiento continuo.
Debe minimizar errores críticos durante:
Inicio de sesión.
Carga de productos.
Consulta de publicaciones.
Visualización de contenido.

4.5 Escalabilidad
El sistema deberá permitir crecimiento futuro en:
Cantidad de usuarios.
Publicaciones almacenadas.
Nuevas categorías de productos.
Integración de nuevos módulos.

4.6 Mantenibilidad
El sistema debe permitir mantenimiento sencillo mediante:
Arquitectura modular.
Separación entre frontend y backend.
Documentación técnica clara.
Facilidad para corregir errores o añadir mejoras.

4.7 Facilidad de uso
Revenfy deberá ofrecer:
Interfaz intuitiva.
Navegación simple.
Aprendizaje rápido del uso de la aplicación.
Procesos cortos para publicar productos.
Buena experiencia visual en móviles.

4.8 Otros requisitos no funcionales
Buen rendimiento general.
Tiempos rápidos de carga.
Diseño responsive.
Estabilidad en conexión con servidor.
Experiencia visual consistente.

5. Definiciones y acrónimos
API
Interfaz que permite comunicación entre sistemas o aplicaciones.
Backend
Parte del sistema encargada de lógica del negocio, procesamiento y conexión con base de datos.
Frontend
Parte visual de la aplicación con la que interactúa el usuario.
Base de datos
Sistema de almacenamiento organizado de información.
UI
User Interface — interfaz gráfica de usuario.
UX
User Experience — experiencia del usuario al interactuar con el sistema.
RF
Requisito funcional.
RNF
Requisito no funcional.
SRS
Software Requirements Specification — especificación de requisitos de software.

