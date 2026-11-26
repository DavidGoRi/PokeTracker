# PokeTracker

Seguimiento personal de la Pokédex de los juegos principales de Pokémon que se pueden jugar en Nintendo Switch y Switch 2:

- Let's Go, Pikachu! / Eevee!
- Espada / Escudo (con la Isla de la Armadura y las Nieves de la Corona)
- Diamante Brillante / Perla Reluciente
- Leyendas: Arceus
- Escarlata / Púrpura (con Noroteo y Arándano)
- Leyendas Pokémon: Z-A (con el Hiperespacio del DLC Megadimensión)
- Rojo Fuego / Verde Hoja (Kanto y Nacional)
- Pokémon HOME: Pokédex viviente con los 1025 Pokémon y dónde conseguir cada uno en los juegos de Switch

Leyendas Z-A incluye también la Pokédex de megaevoluciones, con dónde está cada megapiedra.

Otras herramientas:

- **Estadísticas**: progreso por Pokédex, tipo y generación, variocolores, alfas y capturas por semana.
- **Ruta sugerida**: zonas ordenadas por cuántos Pokémon te faltan. Cada zona abre su ficha: qué te falta allí y cómo aparece (caña, incursión, encuentro fijo…), un botón para marcarlo y lo que puedes conseguir evolucionando lo que sale en esa zona.
- **Intercambios**: los exclusivos de la otra versión que te faltan (marcando los que tiene tu amigo si has cargado su copia), los que puedes evolucionar por intercambio porque ya tienes la preevolución y un mensaje listo para copiar.
- **Marcar o desmarcar todos los que se ven**, o toda una línea evolutiva desde Detalles.
- **Alfas** (Leyendas: Arceus y Z-A) y colección de **formas** (Vivillon, Unown, Alcremie…).
- **Condiciones de aparición** (clima en Espada / Escudo y hora en Diamante Brillante / Perla Reluciente).
- **Combate** en Detalles: debilidades y resistencias por tipo y estadísticas base.
- **Objetos para evolucionar**: piedras y objetos que necesitas para los que te faltan. En Detalles, debajo de la línea evolutiva, sale dónde conseguir cada objeto en el juego.
- **Pasar a otro dispositivo**: un enlace y un código QR con todo tu progreso dentro (no se sube a ningún servidor). Al abrirlo en el otro dispositivo, pregunta y lo carga. Si no cabe en el QR, el QR va sin las fechas de captura; el enlace siempre lleva todo.
- **Puedes evolucionar**: los que te faltan y puedes conseguir ya evolucionando uno que tienes, con cómo hacerlo (respeta las formas regionales: Meowth de Galar evoluciona a Perrserker).
- **Puedes criar**: los que te faltan y puedes sacar de un huevo con un Pokémon que ya tienes, con la pareja y el incienso.
- Mapa de Luminalia con las zonas salvajes de Z-A.
- **Movimientos por nivel** de cada juego y **crianza** paso a paso (grupos huevo, pareja, dónde criar, incienso y movimientos huevo).
- **Eventos**: aviso de teraincursiones de evento y regalos con código (con el código, si es público) de Escarlata / Púrpura y Leyendas Z-A, activos o próximos. `herramientas/eventos.py` los descarga a diario con GitHub Actions.
- **Habilidades** (normales y oculta) con su descripción, y **dónde conseguir cada objeto de evolución** en cada juego.
- **Cazador de variocolores**: contador de encuentros por Pokémon con la probabilidad real de cada juego según el método (Masuda, brotes masivos, Poder Brillo, Amuleto Iris, combo de capturas…) y el historial de cazas terminadas.
- **Comparar** dos Pokémon: estadísticas, debilidades, resistencias e inmunidades lado a lado (también desde Detalles).
- **Naturalezas**: tabla de las 25 con lo que suben y bajan, buscador y la recomendada para cada Pokémon según sus estadísticas.
- **Logros**: medallas que se desbloquean solas (capturas, variocolores, alfas, premios de cada juego, maestro de cada tipo, zonas…), con aviso animado.
- **Comparar con un amigo**: cargas su copia de seguridad y ves qué tiene tu amigo que te falta a ti y al revés, con un mensaje listo para enviar.
- **Compartir progreso**: genera una imagen con tu porcentaje, tus Pokédex, variocolores y logros para descargarla o compartirla.
- **Aviso de eventos**: una campana en la barra superior avisa cuando hay un evento activo con un Pokémon que te falta.
- **Idioma**: español o inglés (selector ES / EN en la barra superior); se traducen la interfaz y los datos.
- **Búsqueda** por nombre en español o en inglés, número regional o nacional y tipo (por ejemplo, "fuego volador").
- Accesible con teclado y lector de pantalla.

Los datos van en `datos/` y se cargan solo cuando hacen falta, para que la página abra rápido.

Cada juego tiene una pestaña con lo que te falta para su premio: el Amuleto Iris, el Volcanion variocolor de Z-A o el Diploma de Rojo Fuego / Verde Hoja.

## Qué hace

- Marca los Pokémon que ya tienes (se guarda en el navegador de cada dispositivo).
- Pestaña **Amuleto Iris** con los que te faltan y los requisitos de cada juego.
- Marca con la ★ los que tienes variocolores (shiny), aparte de los capturados.
- Filtros por tipo, por zona, por exclusivos de versión, por generación y por color (datos de PokeAPI, en `datos/colores.json`), todos combinables y con un botón «Quitar filtros»; y "Por evolucionar" (no lo tienes, pero sí su preevolución). "Por criar" y la etiqueta "Crianza disponible" marcan los que puedes sacar de un huevo con un Pokémon que ya tienes; al abrir Detalles, lo primero es con quién criarlo. Orden por número, por nombre o los que faltan primero.
- Etiqueta "Solo Espada", "Solo Escudo", etc. en los exclusivos de cada versión.
- Botón **Detalles** con el ratio de captura, las tareas de investigación (Leyendas: Arceus), la línea evolutiva completa (nivel, objeto, intercambio u otra condición, según el juego) y las ubicaciones, con la foto de la zona y un mapa con la posición aproximada.
- Copia de seguridad: "Guardar copia de todo" descarga un archivo con todos los juegos (marcas, variocolores, alfas, formas, fechas y ajustes) y "Cargar copia" lo restaura en otro navegador o dispositivo.

Las marcas viven en el `localStorage` del navegador: no se pierden al recargar, pero sí si borras los datos del sitio. Haz una copia de vez en cuando.

## Datos

Ilustraciones oficiales y líneas evolutivas de [PokeAPI](https://pokeapi.co/); ubicaciones, fotos, mapas, exclusivos, tareas de investigación, movimientos de Z-A y eventos de [Serebii.net](https://www.serebii.net/); nombres oficiales de los lugares de [WikiDex](https://www.wikidex.net/). Pokémon y sus nombres son marcas de Nintendo, Game Freak y The Pokémon Company. Proyecto personal sin ánimo de lucro.

## Acceder a la web

Podéis entrar en la web desde el siguiente enlace:
https://davidgori.github.io/PokeTracker/

## Autor

<!-- author-section -->
Hecho por **David Gómez Rivas**, técnico de soporte IT y sistemas. **Disponible para trabajar** en soporte IT o administración de sistemas (presencial o remoto).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-David_G%C3%B3mez_Rivas-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/david-gomez-rivas-6026501b7/) [![Email](https://img.shields.io/badge/Email-david.gm.ri%40gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:david.gm.ri@gmail.com)

Más proyectos en [github.com/DavidGoRi](https://github.com/DavidGoRi).

