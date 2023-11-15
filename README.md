
![Linkedin Henry STUDENTS-09](https://github.com/hernanquev/PI_MLOps/assets/133261827/12fb7464-65a1-4a49-9542-d3d1a791ff96)
# <h1 align=center> **PROYECTO INDIVIDUAL** </h1>
# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>
<p align="center">


## <h2 align=center>**`Introducción y descripción del Proyecto`**</h2>

**¡Bienvenido/a a mi proyecto individual de Machine Learning Operations (MLOps)!**

En este proyecto, mi objetivo consiste en llevar mi modelo de recomendación, desarrollado en el ámbito de la Ciencia de Datos, al mundo real. Enfrento los desafíos que conlleva el ciclo de vida completo de un proyecto de Aprendizaje Automático (Machine Learning).

Imagina la siguiente situación: Acabo de unirme como Científico de Datos a una plataforma multinacional de videojuegos. Tengo la oportunidad de crear mi primer modelo de Aprendizaje Automático que aborda un problema de negocio crucial: un sistema de recomendación de videojuegos para usuarios.

Sin embargo, la realidad es bastante desafiante: Los datos con los que trabajo distan de ser ideales. Están anidados, sin transformar y carecen de procesos automatizados para mantenerse actualizados. Por lo tanto, comienzo desde cero, asumiendo el papel de Ingeniero de Datos, con el fin de construir un Producto Mínimo Viable (MVP) y asegurar el éxito del proyecto.


## <h2 align=center>**`Proceso de Extracción, Transformación y Carga (ETL)`** </h2>


En este proyecto, nos asignaron tareas específicas de transformación de datos que fueron ejecutadas como parte del proceso de Extracción, Transformación y Carga (ETL). Para obtener una visión más detallada de cómo se llevaron a cabo estas transformaciones. A continuación, te proporciono un breve resumen de las acciones realizadas:

+Desanidamiento de campos: Algunos campos, como "reviews", "genres" y otros, estaban anidados en el conjunto de datos. Se llevó a cabo un proceso de desanidamiento para desglosar estos campos y permitir su integración adecuada.

+Formato de fechas: Se ajustaron las fechas presentes en el conjunto de datos al formato AAAA-mm-dd para una mayor consistencia. Asimismo, se creó una nueva columna denominada "year" para extraer el año de la fecha de estreno.

+Busqueda de valores duplicados y/o con formatos incorrectos y elimínarlos/ajústarlos.

+Analizar los conjuntos de datos y eliminar las columnas que no son útiles para la API o los modelos.

Estas acciones de transformación de datos fueron esenciales para preparar el conjunto de datos y garantizar su idoneidad para su posterior análisis y aplicación en el proyecto

## <h2 align=center> **`Desarrollo de API`**</h2>

### En esta etapa del proyecto, se propone disponibilizar los datos de la empresa mediante el uso del framework FastAPI. Se han definido 6 funciones para los endpoints que serán consumidos en la API, cada una de ellas con un decorador `@app.get('/')`.

+ def **PlayTimeGenre( *`genero` : str* )**:
    Devuelve `año` con mas horas jugadas para dicho género.

+ def **UserForGenre( *`genero` : str* )**:
    Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

+ def **UsersNotRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

+ def **sentiment_analysis( *`año` : int* )**:
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

+ def **recomendacion_juego( *`id de producto`* )**:
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

  ### Contacto: https://www.linkedin.com/in/hernanquevedo/
  ### Email: hernanquev@gmail.com
