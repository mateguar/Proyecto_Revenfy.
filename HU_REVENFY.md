# Historias de Usuario Épicas — Revenfy

**Número de Documento:** HU - REVENFY  
**Nombre del Documento:** Historias de Usuario Épicas  
**Elaborado por:** Jhon Alex Beltrán · Anamaria Forigua · Brayan Suárez · Mateo Beltrán

---

## Rol: Comprador

### HU-COM-001 — Registrarse en el aplicativo
> Como **Comprador**, se necesita registrarse en el aplicativo, con la finalidad de acceder a la plataforma de compra y venta.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Registro exitoso | El usuario diligencie correctamente los datos | Cuando seleccione registrarse | El sistema creará la cuenta exitosamente |
| 2 | Correo inválido | El correo no sea institucional | Cuando intente registrarse en el sistema | El sistema rechazará el registro |
| 3 | Campos vacíos | Existan campos incompletos | Cuando envíe el formulario | El sistema mostrará mensajes de validación |

---

### HU-COM-002 — Iniciar sesión
> Como **Comprador**, se necesita iniciar sesión, con la finalidad de ingresar de forma segura al sistema.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Inicio exitoso | Las credenciales sean correctas | Cuando el usuario inicie sesión | El sistema permitirá el acceso |
| 2 | Contraseña incorrecta | La contraseña no coincida | Cuando el usuario ingrese | El sistema mostrará error |
| 3 | Cuenta bloqueada | El usuario esté bloqueado | Cuando intente ingresar | El sistema negará el acceso |

---

### HU-COM-003 — Buscar productos
> Como **Comprador**, se necesita buscar productos, con la finalidad de encontrar artículos de interés rápidamente.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Búsqueda exitosa | Existan productos relacionados | Cuando el usuario realice la búsqueda | El sistema mostrará coincidencias |
| 2 | Sin resultados | No existan coincidencias | Cuando el usuario busque | El sistema mostrará mensaje informativo |
| 3 | Búsqueda rápida | El usuario escriba palabras clave | Cuando inicie la búsqueda | El sistema filtrará resultados automáticamente |

---

### HU-COM-004 — Filtrar productos por categoría y precio
> Como **Comprador**, se necesita filtrar productos por categoría y precio, con la finalidad de facilitar la búsqueda de productos.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Filtro por categoría | Existan categorías | Cuando el usuario seleccione una | El sistema mostrará productos relacionados |
| 2 | Filtro por precio | El usuario indique un rango | Cuando aplique el filtro | El sistema mostrará productos dentro del rango |
| 3 | Sin coincidencias | No existan productos | Cuando aplique filtros | El sistema mostrará mensaje de no resultados |

---

### HU-COM-005 — Visualizar detalles del producto
> Como **Comprador**, se necesita visualizar detalles del producto, con la finalidad de conocer información del producto antes de comprar.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Ver detalles | El producto exista | Cuando seleccione el producto | El sistema mostrará descripción, imágenes y precio |
| 2 | Producto eliminado | El producto ya no exista | Cuando intente visualizarlo | El sistema mostrará aviso |
| 3 | Visualización responsive | El usuario use celular | Cuando abra el producto | El sistema adaptará la interfaz |

---

### HU-COM-006 — Contactar al vendedor
> Como **Comprador**, se necesita contactar al vendedor, con la finalidad de negociar la compra del producto.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Envío de mensaje | El producto esté disponible | Cuando el comprador escriba al vendedor | El sistema enviará el mensaje correctamente |
| 2 | Producto no disponible | El producto esté vendido | Cuando el comprador intente contactar | El sistema mostrará un aviso |
| 3 | Historial de conversación | Existan mensajes previos | Cuando el usuario abra el chat | El sistema mostrará el historial |

---

### HU-COM-007 — Guardar productos favoritos
> Como **Comprador**, se necesita guardar productos favoritos, con la finalidad de consultar productos más tarde.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Agregar favorito | El producto exista | Cuando el comprador seleccione favoritos | El sistema almacenará el producto |
| 2 | Eliminar favorito | El producto ya esté guardado | Cuando el usuario lo retire | El sistema eliminará el registro |
| 3 | Consultar favoritos | Existan productos guardados | Cuando el usuario consulte | El sistema mostrará el listado |

---

### HU-COM-008 — Calificar vendedores
> Como **Comprador**, se necesita calificar vendedores, con la finalidad de aumentar la confianza en la plataforma.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Calificación exitosa | Exista una compra realizada | Cuando el comprador califique | El sistema guardará la valoración |
| 2 | Comentario vacío | El comentario no tenga contenido | Cuando el usuario envíe | El sistema permitirá solo la calificación |
| 3 | Intento duplicado | Ya exista una calificación | Cuando el usuario intente repetir | El sistema impedirá duplicados |

---

### HU-COM-009 — Reportar publicaciones sospechosas
> Como **Comprador**, se necesita reportar publicaciones sospechosas, con la finalidad de mantener la seguridad del entorno.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Reporte exitoso | Exista una publicación sospechosa | Cuando el comprador reporte | El sistema almacenará la denuncia |
| 2 | Motivo obligatorio | No se escriba una razón | Cuando el usuario envíe | El sistema solicitará completar el campo |
| 3 | Confirmación enviada | El reporte sea válido | Cuando el proceso finalice | El sistema confirmará el registro |

---

### HU-COM-010 — Consultar historial de compras
> Como **Comprador**, se necesita consultar historial de compras, con la finalidad de llevar control de adquisiciones.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Historial disponible | Existan compras registradas | Cuando el usuario consulte | El sistema mostrará el historial |
| 2 | Sin compras realizadas | No existan registros | Cuando el usuario ingrese | El sistema mostrará mensaje informativo |
| 3 | Detalle de compra | El usuario seleccione una compra | Cuando abra el detalle | El sistema mostrará información completa |

---

## Rol: Vendedor

### HU-VEN-001 — Recibir notificaciones de interés
> Como **Vendedor**, se necesita recibir notificaciones de interés, con la finalidad de responder rápidamente a compradores.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Notificación enviada | Un comprador escriba | Cuando envíe un mensaje | El sistema notificará al vendedor |
| 2 | Mensaje leído | El vendedor abra la notificación | Cuando consulte mensajes | El sistema marcará como leído |
| 3 | Sin conexión | El usuario esté desconectado | Cuando reciba mensajes | El sistema almacenará la notificación |

---

### HU-VEN-002 — Consultar métricas de ventas
> Como **Vendedor**, se necesita consultar métricas de ventas, con la finalidad de medir el desempeño comercial.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Visualización de métricas | Existan ventas registradas | Cuando se consulte las estadísticas | El sistema mostrará las métricas |
| 2 | Sin ventas | No existan registros | Cuando consulte | El sistema mostrará valores en cero |
| 3 | Datos actualizados | Existan nuevas ventas | Cuando recargue | El sistema actualizará la información |

---

### HU-VEN-003 — Marcar productos como vendidos
> Como **Vendedor**, se necesita marcar productos como vendidos, con la finalidad de mantener información actualizada.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Cambio exitoso | El producto esté disponible | Cuando seleccione vendido | El sistema actualizará el estado del producto |
| 2 | Producto ya vendido | El producto ya esté marcado | Cuando intente repetir la acción | El sistema mostrará un aviso |
| 3 | Actualización visible | Otros usuarios consulten | Cuando ingresen al producto | El sistema mostrará estado vendido |

---

### HU-VEN-004 — Editar publicaciones
> Como **Vendedor**, se necesita editar publicaciones, con la finalidad de actualizar información de productos.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Edición exitosa | El producto exista | Cuando el usuario edite | El sistema actualizará la información |
| 2 | Producto inexistente | El producto haya sido eliminado | Cuando intente editar | El sistema mostrará error |
| 3 | Validación de datos | Existan datos inválidos | Cuando guarde cambios | El sistema impedirá la actualización |

---

### HU-VEN-005 — Publicar productos
> Como **Vendedor**, se necesita publicar productos, con la finalidad de ofrecer artículos de segunda mano.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Publicación exitosa | Los datos estén completos | Cuando publique el producto | El sistema guardará la publicación |
| 2 | Campos obligatorios | Falten datos | Cuando intente publicar | El sistema mostrará las validaciones faltantes |
| 3 | Imagen inválida | El formato no sea permitido | Cuando suba la imagen | El sistema rechazará el archivo |

---

### HU-VEN-006 — Consultar historial de ventas
> Como **Vendedor**, se necesita consultar el historial de ventas, con la finalidad de llevar control comercial.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Historial disponible | Existan ventas realizadas | Cuando el vendedor consulte | El sistema mostrará las ventas |
| 2 | Sin registros | No existan ventas | Cuando consulte | El sistema mostrará mensaje informativo |
| 3 | Detalle de venta | El usuario seleccione una venta | Cuando abra el registro | El sistema mostrará información detallada |

---

### HU-VEN-007 — Responder mensajes de compradores
> Como **Vendedor**, se necesita responder mensajes de compradores, con la finalidad de facilitar negociaciones.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Respuesta enviada | Exista una conversación activa | Cuando el vendedor responda | El sistema enviará el mensaje |
| 2 | Mensaje vacío | No exista contenido | Cuando el usuario envíe | El sistema solicitará completar el mensaje |
| 3 | Conversación almacenada | Existan mensajes | Cuando se consulte el chat | El sistema mostrará el historial |

---

### HU-VEN-008 — Recibir calificaciones
> Como **Vendedor**, se necesita recibir calificaciones, con la finalidad de fortalecer la reputación en la plataforma.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Visualización de calificaciones | Existan valoraciones | Cuando el vendedor consulte | El sistema mostrará puntuaciones |
| 2 | Promedio actualizado | Se registre una nueva calificación | Cuando se actualice el perfil | El sistema recalculará el promedio |
| 3 | Sin calificaciones | No existan valoraciones | Cuando se consulte el perfil | El sistema mostrará mensaje informativo |

---

### HU-VEN-009 — Subir imágenes de productos
> Como **Vendedor**, se necesita subir imágenes de productos, con la finalidad de mostrar mejor los artículos.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Carga exitosa | El formato sea válido | Cuando el usuario suba imágenes | El sistema almacenará los archivos |
| 2 | Formato inválido | El archivo no sea permitido | Cuando el usuario cargue la imagen | El sistema rechazará el archivo |
| 3 | Vista previa | La imagen cargue correctamente | Cuando el proceso termine | El sistema mostrará vista previa |

---

### HU-VEN-010 — Eliminar publicaciones
> Como **Vendedor**, se necesita eliminar publicaciones, con la finalidad de retirar productos no disponibles.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Eliminación exitosa | La publicación exista | Cuando el vendedor elimine | El sistema retirará el producto |
| 2 | Confirmación requerida | El usuario seleccione eliminar | Cuando confirme la acción | El sistema ejecutará el proceso |
| 3 | Publicación inexistente | El producto ya no exista | Cuando intente eliminar | El sistema mostrará un mensaje de error |

---

## Rol: Administrador

### HU-ADM-001 — Gestionar usuarios registrados
> Como **Administrador**, se necesita gestionar usuarios registrados, con la finalidad de garantizar la seguridad y control del aplicativo.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Visualización de usuarios | Existan usuarios registrados | Cuando el administrador consulte | El sistema mostrará el listado |
| 2 | Bloqueo de usuario | Exista comportamiento indebido | Cuando el administrador bloquee | El sistema restringirá el acceso |
| 3 | Búsqueda de usuario | El administrador necesite filtrar | Cuando se busque a un usuario | El sistema mostrará coincidencias |

---

### HU-ADM-002 — Eliminar publicaciones inapropiadas
> Como **Administrador**, se necesita eliminar publicaciones inapropiadas, con la finalidad de mantener un entorno seguro.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Eliminación exitosa | La publicación incumpla normas | Cuando el administrador elimine | El sistema retirará la publicación |
| 2 | Notificación al usuario | Se elimine contenido | Cuando finalice la acción | El sistema notificará al vendedor |
| 3 | Registro de acciones | Se elimine una publicación | Cuando el proceso termine | El sistema guardará evidencia |

---

### HU-ADM-003 — Visualizar métricas generales
> Como **Administrador**, se necesita visualizar métricas generales, con la finalidad de analizar el uso del aplicativo.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Métricas disponibles | Existan datos registrados | Cuando consulte estadísticas | El sistema mostrará gráficas e indicadores |
| 2 | Actualización automática | Existan nuevos movimientos | Cuando recargue la información | El sistema actualizará métricas |
| 3 | Sin registros | No existan datos | Cuando consulte | El sistema mostrará estadísticas vacías |

---

### HU-ADM-004 — Gestionar reportes de usuarios
> Como **Administrador**, se necesita gestionar reportes de usuarios, con la finalidad de resolver conflictos dentro del aplicativo.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Recepción de reportes | Un usuario denuncie | Cuando envíe el reporte | El sistema almacenará la información |
| 2 | Revisión de evidencia | Existan pruebas adjuntas | Cuando el administrador consulte | El sistema mostrará la evidencia |
| 3 | Resolución del caso | El reporte sea válido | Cuando el administrador actúe | El sistema aplicará medidas correspondientes |

---

### HU-ADM-005 — Gestionar categorías de productos
> Como **Administrador**, se necesita gestionar categorías de productos, con la finalidad de organizar las publicaciones.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Crear categoría | El administrador agregue datos válidos | Cuando cree una categoría | El sistema almacenará la información |
| 2 | Editar categoría | Exista una categoría registrada | Cuando modifique datos | El sistema actualizará los cambios |
| 3 | Eliminar categoría | La categoría no tenga productos asociados | Cuando elimine | El sistema eliminará la categoría |

---

### HU-ADM-006 — Validar correos institucionales
> Como **Administrador**, se necesita validar correos institucionales, con la finalidad de permitir acceso solo a usuarios del SENA.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Correo válido | El correo pertenezca al SENA | Cuando el usuario se registre | El sistema permitirá el acceso |
| 2 | Correo inválido | El correo no sea institucional | Cuando intente registrarse | El sistema rechazará el registro |
| 3 | Validación automática | El usuario escriba el correo | Cuando continúe el proceso | El sistema verificará el dominio |

---

### HU-ADM-007 — Bloquear usuarios reportados
> Como **Administrador**, se necesita bloquear usuarios reportados, con la finalidad de mantener un entorno seguro.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Bloqueo exitoso | Existan reportes válidos | Cuando el administrador bloquee | El sistema restringirá el acceso |
| 2 | Notificación enviada | El usuario sea bloqueado | Cuando termine el proceso | El sistema notificará al usuario su bloqueo |
| 3 | Registro de bloqueo | Se aplique la sanción | Cuando finalice la acción | El sistema almacenará evidencia |

---

### HU-ADM-008 — Enviar notificaciones masivas
> Como **Administrador**, se necesita enviar notificaciones masivas, con la finalidad de informar novedades importantes.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Envío exitoso | Existan usuarios registrados | Cuando el administrador envíe la notificación | El sistema distribuirá el mensaje |
| 2 | Mensaje vacío | El contenido esté vacío | Cuando intente enviar | El sistema solicitará completar la información |
| 3 | Confirmación de envío | El proceso finalice correctamente | Cuando termine | El sistema mostrará confirmación |

---

### HU-ADM-009 — Consultar historial de actividad
> Como **Administrador**, se necesita consultar historial de actividad, con la finalidad de supervisar movimientos del sistema.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Consulta exitosa | Existan registros | Cuando el administrador consulte | El sistema mostrará actividades |
| 2 | Filtros de búsqueda | El administrador aplique filtros | Cuando seleccione criterios | El sistema mostrará resultados filtrados |
| 3 | Sin registros | No existan actividades | Cuando consulte | El sistema mostrará un mensaje informativo |

---

### HU-ADM-010 — Gestionar estados de publicaciones
> Como **Administrador**, se necesita gestionar estados de publicaciones, con la finalidad de controlar productos activos o vendidos.

| # | Título | Contexto | Evento | Resultado esperado |
|---|--------|----------|--------|--------------------|
| 1 | Cambio de estado | La publicación exista | Cuando el administrador modifique el estado | El sistema actualizará la información |
| 2 | Estado inválido | El estado no sea permitido | Cuando intente actualizar | El sistema rechazará el cambio |
| 3 | Visualización actualizada | Otros usuarios consulten | Cuando ingresen a la publicación | El sistema mostrará el estado actual |
