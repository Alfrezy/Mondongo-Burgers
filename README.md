# 🍔 Mondongo Burgers - API & Kubernetes Clúster

Este proyecto despliega una API en Flask conectada a una base de datos PostgreSQL, utilizando una arquitectura de microservicios altamente disponible con **Kubernetes**.

## 🚀 Cómo ejecutar el proyecto

1. **Construir la imagen de la API:**
   ```bash
   docker build -t mondongo-app:latest .

2. **Construir los kunernets:**
   ```bash
   kubectl apply -f mondongo-db.yml