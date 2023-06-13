# PlatziGram

PlatziGram es un proyecto basado en Django que busca ofrecer una experiencia similar a la de Twitter, pero con su propio enfoque y características distintivas. Esta plataforma permite a los usuarios registrados compartir mensajes cortos, conocidos como "platziweets", con sus seguidores y conectarse con otras personas de manera rápida y sencilla.

## Características

- Registro de usuarios: Los usuarios pueden crear una cuenta en PlatziGram para comenzar a compartir sus propios platziweets y seguir a otros usuarios interesantes.
- Publicación de platziweets: Los usuarios pueden redactar y publicar mensajes cortos, de hasta 280 caracteres, para compartir sus ideas, pensamientos, enlaces o cualquier contenido relevante.
- Interacción social: Los usuarios pueden seguir a otros usuarios y recibir actualizaciones en su feed de noticias. También pueden dar "me gusta" a los platziweets que encuentren interesantes y dejar comentarios en ellos.
- Explorar y descubrir: Los usuarios pueden descubrir nuevos perfiles y platziweets interesantes a través de la función de búsqueda y las recomendaciones personalizadas.
- Perfiles de usuario: Cada usuario tiene su propio perfil donde pueden editar su información personal, agregar una foto de perfil y administrar la configuración de privacidad.
- Notificaciones: Los usuarios reciben notificaciones en tiempo real cuando otros interactúan con sus platziweets, como recibir un nuevo seguidor o un me gusta en su publicación.
- Temas y hashtags: Los usuarios pueden utilizar hashtags para etiquetar sus platziweets y explorar otros mensajes relacionados con un tema específico.

## Tecnologías utilizadas

El proyecto PlatziGram se ha desarrollado utilizando las siguientes tecnologías:

- Django: Framework de desarrollo web de alto nivel basado en Python.
- Python: Lenguaje de programación utilizado para la implementación del backend y la lógica de negocio.
- HTML/CSS: Lenguajes de marcado y estilos utilizados para la presentación de las páginas web.
- JavaScript: Lenguaje de programación utilizado para agregar interactividad y funcionalidades dinámicas en el frontend.
- Base de datos: Se utiliza una base de datos compatible con Django, como PostgreSQL o SQLite, para almacenar la información de los usuarios y los platziweets.

## Instalación y ejecución

1. Clona este repositorio: `git clone https://github.com/tu-usuario/platzigram.git`
2. Accede al directorio del proyecto: `cd platzigram`
3. Crea y activa un entorno virtual (opcional): `python3 -m venv env` y `source env/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Ejecuta las migraciones de la base de datos: `python manage.py migrate`
6. Inicia el servidor de desarrollo: `python manage.py runserver`
7. Abre tu navegador y accede a `http://localhost:8000` para utilizar PlatziGram.


