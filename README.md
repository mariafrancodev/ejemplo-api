## Ejemplo API Frutas

`python3 -m venv venv` Crear un entorno virtual

`source venv/bin/activate` Activar entorno virtual

`python3 manage.py runserver` Correr el proyecto

### Base JSON

```
{
  "nombre": "sandia",
  "color": "verde",
  "sabor": "dulce",
  "precio": "2000"
}
```

`http://127.0.0.1:8000/frutas/` Api Overview

`http://127.0.0.1:8000/frutas/listar/` Lista las frutas

`http://127.0.0.1:8000/frutas/crear/` Crear frutas

`http://127.0.0.1:8000/frutas/editar/<str:pk>/` Editar frutas (Debe mandar el JSON completo)

`http://127.0.0.1:8000/frutas/eliminar/<str:pk>/` Eliminar frutas

