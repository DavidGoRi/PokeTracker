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
- **Ruta sugerida**: zonas ordenadas por cuántos Pokémon te faltan.
- **Intercambios**: los exclusivos de la otra versión que te faltan, con un mensaje listo para copiar.
- **Marcar o desmarcar todos los que se ven**, o toda una línea evolutiva desde Detalles.
- **Alfas** (Leyendas: Arceus y Z-A) y colección de **formas** (Vivillon, Unown, Alcremie…).
- **Condiciones de aparición** (clima en Espada / Escudo y hora en Diamante Brillante / Perla Reluciente).
- **Combate** en Detalles: debilidades y resistencias por tipo y estadísticas base.
- **Objetos para evolucionar**: piedras y objetos que necesitas para los que te faltan.
- Mapa de Luminalia con las zonas salvajes de Z-A.
- **Movimientos por nivel** de cada juego y **crianza** paso a paso (grupos huevo, pareja, dónde criar, incienso y movimientos huevo).
- **Eventos**: aviso de teraincursiones de evento de Escarlata / Púrpura activas o próximas. `herramientas/eventos.py` los descarga a diario con GitHub Actions.
- **Búsqueda** por nombre en español o en inglés, número regional o nacional y tipo (por ejemplo, "fuego volador").
- Accesible con teclado y lector de pantalla.

Los datos van en `datos/` y se cargan solo cuando hacen falta, para que la página abra rápido.

Cada juego tiene una pestaña con lo que te falta para su premio: el Amuleto Iris, el Volcanion variocolor de Z-A o el Diploma de Rojo Fuego / Verde Hoja.

## Qué hace

- Marca los Pokémon que ya tienes (se guarda en el navegador de cada dispositivo).
- Pestaña **Amuleto Iris** con los que te faltan y los requisitos de cada juego.
- Marca con la ★ los que tienes variocolores (shiny), aparte de los capturados.
- Filtros por tipo, por zona, por exclusivos de versión y "Por evolucionar" (no lo tienes, pero sí su preevolución). Orden por número, por nombre o los que faltan primero.
- Etiqueta "Solo Espada", "Solo Escudo", etc. en los exclusivos de cada versión.
- Botón **Detalles** con el ratio de captura, las tareas de investigación (Leyendas: Arceus), la línea evolutiva completa (nivel, objeto, intercambio u otra condición, según el juego) y las ubicaciones, con la foto de la zona y un mapa con la posición aproximada.
- Copia de seguridad: "Guardar copia de todo" descarga un archivo con todos los juegos (marcas, variocolores, alfas, formas, fechas y ajustes) y "Cargar copia" lo restaura en otro navegador o dispositivo.

Las marcas viven en el `localStorage` del navegador: no se pierden al recargar, pero sí si borras los datos del sitio. Haz una copia de vez en cuando.

## Datos

Ilustraciones oficiales y líneas evolutivas de [PokeAPI](https://pokeapi.co/); ubicaciones, fotos, mapas, exclusivos, tareas de investigación, movimientos de Z-A y eventos de [Serebii.net](https://www.serebii.net/); nombres oficiales de los lugares de [WikiDex](https://www.wikidex.net/). Pokémon y sus nombres son marcas de Nintendo, Game Freak y The Pokémon Company. Proyecto personal sin ánimo de lucro.

## Acceder a la web

Podéis entrar en la web desde el siguiente enlace:
https://davidgori.github.io/PokeTracker/
