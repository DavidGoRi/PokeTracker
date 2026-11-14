"""Eventos de Escarlata / Púrpura y Leyendas Z-A (Serebii) -> datos/eventos.json.

- Teraincursiones de evento (Escarlata / Púrpura).
- Regalos con código de un solo uso o compartido (Escarlata / Púrpura y Z-A).

Se ejecuta a diario con GitHub Actions (.github/workflows/eventos.yml). Solo usa la biblioteca estándar.
"""
import datetime, html, json, os, re, urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower().replace('é', 'e').replace('♀', 'f').replace('♂', 'm'))
NOMBRES = {int(k): v for k, v in json.load(open(os.path.join(RAIZ, 'datos', 'nombres-en.json'), encoding='utf-8')).items()}
EN = {v.lower(): k for k, v in NOMBRES.items()}
SLUG = {norm(v): k for k, v in NOMBRES.items()}
MESES = {m: i for i, m in enumerate(['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                                      'september', 'october', 'november', 'december'], 1)}

def bajar(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (PokeTracker, uso personal)'})
    return urllib.request.urlopen(req, timeout=60).read().decode('latin-1')

def fechas(txt):
    """'August 28th 2026 - September 3rd 2026', 'October 6th - 8th 2023', 'June 6th 2026 - June 7th 2026'."""
    out = []
    pat = r'(\w+) (\d+)(?:st|nd|rd|th)?(?:,? (\d{4}))? - (?:(\w+) )?(\d+)(?:st|nd|rd|th)?,? (\d{4})'
    for m1, d1, a1, m2, d2, a2 in re.findall(pat, txt):
        if m1.lower() not in MESES: continue
        m2 = m2 or m1
        if m2.lower() not in MESES: continue
        a2 = int(a2); a1 = int(a1) if a1 else (a2 - 1 if MESES[m1.lower()] > MESES[m2.lower()] else a2)
        try:
            out.append([datetime.date(a1, MESES[m1.lower()], int(d1)).isoformat(), datetime.date(a2, MESES[m2.lower()], int(d2)).isoformat()])
        except ValueError:
            pass
    return out

def nombres_en_texto(txt):
    ids = []
    for nombre, i in sorted(EN.items(), key=lambda x: -len(x[0])):
        if re.search(r'(?<![\w-])' + re.escape(nombre) + r'(?![\w-])', txt.lower()) and i not in ids:
            ids.append(i)
    return ids

def bloques(t):
    """Cada evento de Serebii: <td class="fooleft"><h2|h3>Título</h…> … hasta el siguiente."""
    partes = re.split(r'<td class="fooleft" colspan="2"><h[23]>', t)
    pos = 0
    for p in partes[1:]:
        pos = t.find(p, pos)
        yield pos, html.unescape(re.sub(r'<[^>]+>', '', p[:re.search(r'</h[23]>', p).start()])).strip(), p

def teraincursiones():
    t = bajar('https://www.serebii.net/scarletviolet/teraraidbattleevents.shtml')
    eventos = []
    for _, titulo, b in bloques(t):
        cuerpo = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', b[:b.find('picturetd')])))
        rangos = fechas(cuerpo)
        if not rangos: continue
        estrellas = re.search(r'(\d) Star', cuerpo)
        eventos.append({'juego': 'sv', 'tipo': 'teraincursion', 'titulo': titulo, 'estrellas': int(estrellas.group(1)) if estrellas else None,
                        'brote': 'Mass Outbreak' in cuerpo, 'regiones': [['Global', a, z] for a, z in rangos],
                        'ids': nombres_en_texto(titulo + ' ' + cuerpo.split('Click here')[0])})
    return eventos

def codigos(url, juego):
    t = bajar(url)
    compartidos = t.find('<a name="shared">')
    eventos = []
    for pos, titulo, b in bloques(t):
        a = b.find('Release Dates'); fin = b.find('<p>', a)
        if a < 0: continue
        regiones = []
        for reg, txt in re.findall(r'<b>([^<:]+):</b>\s*([^<]+)', b[a:fin if fin > 0 else a + 800]):
            for x, y in fechas(txt): regiones.append([html.unescape(reg).strip(), x, y])
        if not regiones: continue
        ids = []
        for slug in re.findall(r'<a href="/pokedex-[a-z]+/([a-z0-9\'-]+)/"><img', b):
            i = SLUG.get(norm(slug))
            if i and i not in ids: ids.append(i)
        if not ids: continue
        texto = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', b)))
        codigo = re.search(r'(?:code|password)(?: is)?:?\s*([A-Z0-9]{6,16})', texto)
        compartido = 0 <= compartidos < pos
        eventos.append({'juego': juego, 'tipo': 'codigo-compartido' if compartido else 'codigo', 'titulo': titulo,
                        'regiones': regiones, 'ids': ids, 'shiny': '/Shiny/' in b, 'alfa': 'Alpha' in texto[texto.find('Release Dates'):],
                        'codigo': codigo.group(1) if (codigo and compartido) else None})
    return eventos

def main():
    hoy = datetime.date.today()
    limite = (hoy - datetime.timedelta(days=3)).isoformat()
    todos = []
    for f, args in ((teraincursiones, ()), (codigos, ('https://www.serebii.net/scarletviolet/serialcode.shtml', 'sv')),
                    (codigos, ('https://www.serebii.net/legendsz-a/serialcode.shtml', 'za'))):
        try:
            todos += f(*args)
        except Exception as e:
            print('Fallo al leer', f.__name__, args, e)
    eventos = [e for e in todos if e['ids'] and max(r[2] for r in e['regiones']) >= limite]
    json.dump({'actualizado': hoy.isoformat(), 'fuente': 'Serebii.net', 'eventos': eventos},
              open(os.path.join(RAIZ, 'datos', 'eventos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(todos), 'eventos leídos;', len(eventos), 'activos o próximos')

if __name__ == '__main__':
    main()
