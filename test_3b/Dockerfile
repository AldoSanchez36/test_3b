# Imagen de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . /app/

# Instala las dependencias
RUN python3 -m venv venv
RUN . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Usa el puerto para Django 8000
EXPOSE 8000

# Comando para correr la aplicación
CMD ["venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
