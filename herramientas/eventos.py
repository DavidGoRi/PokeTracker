"""Eventos de teraincursiones de Escarlata / Púrpura (Serebii) -> datos/eventos.json.

Se ejecuta a diario con GitHub Actions (.github/workflows/eventos.yml). Solo usa la biblioteca estándar.
"""
import datetime, html, json, os, re, urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = {v.lower(): int(k) for k, v in json.load(open(os.path.join(RAIZ, 'datos', 'nombres-en.json'), encoding='utf-8')).items()}
MESES = {m: i for i, m in enumerate(['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                                      'september', 'october', 'november', 'december'], 1)}
REG = {'Hisuian': 'hisui', 'Galarian': 'galar', 'Alolan': 'alola', 'Paldean': 'paldea'}

def bajar(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (PokeTracker, uso personal)'})
    return urllib.request.urlopen(req, timeout=60).read().decode('latin-1')

def fechas(txt):
    """'August 28th 2026 - September 3rd 2026', 'October 6th - 8th 2023', 'September 1st - September 17th 2023'."""
    out = []
    pat = r'(\w+) (\d+)(?:st|nd|rd|th)?(?: (\d{4}))? - (?:(\w+) )?(\d+)(?:st|nd|rd|th)? (\d{4})'
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

def pokemon(txt):
    ids = []
    for nombre, i in sorted(EN.items(), key=lambda x: -len(x[0])):
        if re.search(r'(?<![\w-])' + re.escape(nombre) + r'(?![\w-])', txt.lower()) and i not in ids:
            ids.append(i)
    return ids

def teraincursiones():
    t = bajar('https://www.serebii.net/scarletviolet/teraraidbattleevents.shtml')
    eventos = []
    for bloque in re.split(r'<td class="fooleft" colspan="2"><h2>', t)[1:]:
        titulo = html.unescape(bloque[:bloque.find('</h2>')])
        cuerpo = html.unescape(re.sub(r'<[^>]+>', ' ', bloque[:bloque.find('picturetd')]))
        cuerpo = re.sub(r'\s+', ' ', cuerpo)
        rangos = fechas(cuerpo)
        if not rangos: continue
        estrellas = re.search(r'(\d) Star', cuerpo)
        brote = 'Mass Outbreak' in cuerpo
        ids = pokemon(titulo + ' ' + cuerpo.split('Click here')[0])
        eventos.append({'juego': 'sv', 'tipo': 'teraincursion', 'estrellas': int(estrellas.group(1)) if estrellas else None,
                        'brote': brote, 'fechas': rangos, 'ids': ids})
    return eventos

def main():
    hoy = datetime.date.today()
    eventos = [e for e in teraincursiones() if e['ids'] and max(f[1] for f in e['fechas']) >= (hoy - datetime.timedelta(days=3)).isoformat()]
    json.dump({'actualizado': hoy.isoformat(), 'fuente': 'Serebii.net', 'eventos': eventos},
              open(os.path.join(RAIZ, 'datos', 'eventos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(eventos), 'eventos activos o próximos')

if __name__ == '__main__':
    main()
