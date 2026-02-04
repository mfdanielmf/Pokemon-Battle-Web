# PokeWarriors

**INTEGRANTES DEL EQUIPO**:

- Francisco Antonio Sánchez Díaz
- Daniel Martínez Fernández

**¿DE QUÉ TRATA ESTE PROYECTO?**:

Se trata de una página web con el objetivo de simular un campo de batalla al estilo Pokémon.

**TECNOLOGÍAS**

**1. Frontend**: HTML, CSS, JavaScript  
**2. Backend**: Pyhon + Flask  
**3. Templates:** Jinja2

**INSTALACIÓN Y LANZAMIENTO**

**1. Clonar repositorio:**

Abrir cmd y pegar el siguiente comando:

```
git clone https://github.com/mfdanielmf/Pokemon-Battle-Web.git
```

**2. Crear entorno virtual (necesario tener instalado python)**

Ejecutar el siguiente comando en la raíz del proyecto:

```
python -m venv .venv
```

**3. Instalar las dependencias necesarias:**

Ejecutar el siguiente comando para descar los requirements:

```
./.venv/Scripts/pip.exe install -r requirements.txt
```

**4. Crear la base de datos y las tablas:**

Ahora hay que crear las tablas de la base de datos.  
Para ello, hay que ejecutar el siguiente comando:

```
./.venv/Scripts/flask.exe --app app.main crear-tablas
```

**5. Lanzar main.py**

Ejecutar el siguiente comando para lanzar el servidor local:

```
./.venv/Scripts/python.exe -m app.main
```

**6. Abrir en el navegador**

Esto abrirá el servidor en la siguiente dirección:

```
http://127.0.0.1:8080
```

# Sobre la API

Hemos usado la [PokeAPI](https://pokeapi.co/) para obtener la información de los pokemons.  
El manejo de la API está en la carpeta clients (donde hacemos las peticiones) y la lógica de negocio y la adaptación de los datos de la api está en pokemon service.  
Los datos se guardan en caché durante 5 minutos (podría ser más tiempo porque es raro que cambie la info de los pokemons) y se mantienen hasta 4 páginas y 10 detalles de pokemons. Cuando no queda espacio, borramos los datos más antiguos.
