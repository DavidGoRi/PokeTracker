# PokeTracker

Seguimiento personal de la Pokédex de los juegos de Pokémon de Nintendo Switch que dan el Amuleto Iris al completarla:

- Let's Go, Pikachu! / Eevee!
- Espada / Escudo (con la Isla de la Armadura y las Nieves de la Corona)
- Diamante Brillante / Perla Reluciente
- Leyendas: Arceus
- Escarlata / Púrpura (con Noroteo y Arándano)

## Qué hace

- Marca los Pokémon que ya tienes (se guarda en el navegador de cada dispositivo).
- Pestaña **Amuleto Iris** con los que te faltan y los requisitos de cada juego.
- Botón **Ver Spawn** con las ubicaciones, la foto de la zona y un mapa con la posición aproximada.
- Copia de seguridad: "Guardar copia" y "Cargar copia" para pasar las marcas de un dispositivo a otro.

Las marcas viven en el `localStorage` del navegador: no se pierden al recargar, pero sí si borras los datos del sitio. Haz una copia de vez en cuando.

## Datos

Ilustraciones oficiales de [PokeAPI](https://pokeapi.co/); ubicaciones, fotos y mapas de [Serebii.net](https://www.serebii.net/). Pokémon y sus nombres son marcas de Nintendo, Game Freak y The Pokémon Company. Proyecto personal sin ánimo de lucro.

## Actualizar la web

Desde esta carpeta, en PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File subir.ps1 "Mensaje opcional"
```
