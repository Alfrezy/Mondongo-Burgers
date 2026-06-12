## 🚀 ¿Qué cosas nuevas se agregaron?
*Marca con una `x` todo lo nuevo que estás metiendo al proyecto en este cambio:*

- [ ] 🛣️ **Nuevas Rutas / Endpoints en la API** (ej. `/menu/snacks`, `/ordenes`)
- [ ] 🗄️ **Cambios en la Base de Datos** (Nuevas tablas, columnas o datos en el `init.sql`)
- [ ] ⚙️ **Nuevas Variables de Entorno** (Modificaciones en el archivo `.env`)
- [ ] 📦 **Nuevas Dependencias** (Librerías nuevas agregadas a `requirements.txt`)
- [ ] 🐳 **Ajustes de Infraestructura** (Cambios en Docker o manifiestos de Kubernetes)

---

## 📝 Detalle de las nuevas implementaciones
*Explica brevemente qué hacen las cosas nuevas que metiste y cómo funcionan:*
- **Nueva funcionalidad:** [Ej. Se agregó el endpoint /snacks para listar los tacos de pizza]
- **Cambio en la base de datos:** [Ej. Se creó la tabla 'clientes_frecuentes']

---

## 🗹 Lista de Chequeo de Expansión (Control de Calidad)
*Antes de dar por terminado este cambio, marca las casillas para asegurar que no rompimos nada de lo anterior:*

- [ ] 🔌 **Conexión intacta:** Probé las cosas nuevas y la API se sigue conectando bien a PostgreSQL.
- [ ] 📜 **Estructura limpia:** Si agregué tablas, actualicé el archivo `init.sql` para que el contenedor inicialice todo automáticamente.
- [ ] 📌 **Dependencias al día:** Si usé un `import` nuevo en Python, ya lo anoté en el `requirements.txt`.
- [ ] 🔒 **Seguridad:** Verifiqué que las credenciales nuevas de las bases de datos se manejen por `Secret` o `.env` y no escritas fijas en el código.
- [ ] 🐳 **Build exitoso:** Corrí `docker build -t mondongo-app:latest .` y la imagen compiló sin dar errores de capas.
- [ ] ☸️ **Kubernetes verificado:** Levanté las 3 réplicas en mi clúster local y todas pasaron a estado `Running` correctamente.

---

## 📸 Evidencia de Funcionamiento
*Pega aquí una captura de pantalla de DBeaver, de tu terminal o de la respuesta en tu navegador (http://localhost:30001) que demuestre que lo nuevo que metiste funciona al 100%.*