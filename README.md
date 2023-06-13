# PlatziGram

PlatziGram es una aplicación basada en Django que replica las funcionalidades principales de Instagram. Permite a los usuarios registrados compartir fotos y videos, seguir a otros usuarios, dar "me gusta" y comentar publicaciones, entre otras características.

## Características

- Registro de usuarios: Los usuarios pueden crear una cuenta en PlatziGram para comenzar a compartir sus propias fotos y videos, y seguir a otros usuarios interesantes.
- Subida de fotos y videos: Los usuarios pueden subir sus imágenes y videos favoritos para compartirlos con su comunidad.
- Interacción social: Los usuarios pueden seguir a otros usuarios y recibir actualizaciones en su feed de noticias. También pueden dar "me gusta" y dejar comentarios en las publicaciones de otros usuarios.
- Explorar y descubrir: Los usuarios pueden explorar nuevas fotos y videos a través de la función de búsqueda y las recomendaciones personalizadas.
- Perfiles de usuario: Cada usuario tiene su propio perfil donde pueden editar su información personal, agregar una foto de perfil y administrar su configuración de privacidad.
- Mensajería directa: Los usuarios pueden enviar mensajes directos a otros usuarios para comunicarse de forma privada.
- Historias: Los usuarios pueden compartir historias efímeras que desaparecen después de 24 horas.
- Filtros y edición de imágenes: Los usuarios pueden aplicar filtros y realizar ediciones básicas en sus fotos antes de compartirlas.

## Tecnologías utilizadas

El proyecto PlatziGram se ha desarrollado utilizando las siguientes tecnologías:

- Django: Framework de desarrollo web de alto nivel basado en Python.
- Python: Lenguaje de programación utilizado para la implementación del backend y la lógica de negocio.
- HTML/CSS: Lenguajes de marcado y estilos utilizados para la presentación de las páginas web.
- JavaScript: Lenguaje de programación utilizado para agregar interactividad y funcionalidades dinámicas en el frontend.
- Base de datos: Se utiliza una base de datos compatible con Django, como PostgreSQL o SQLite, para almacenar la información de los usuarios y las publicaciones.

## Instalación y ejecución

1. Clona este repositorio: `git clone https://github.com/tu-usuario/platzigram.git`
2. Accede al directorio del proyecto: `cd platzigram`
3. Crea y activa un entorno virtual (opcional): `python3 -m venv env` y `source env/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Ejecuta las migraciones de la base de datos: `python manage.py migrate`
6. Inicia el servidor de desarrollo: `python manage.py runserver`
7. Abre tu navegador y accede a `http://localhost:8000` para utilizar PlatziGram.
