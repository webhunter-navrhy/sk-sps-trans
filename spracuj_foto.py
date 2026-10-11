"""Pripraví img/ z ilustračných fotiek (podklady/stock, zdroje v podklady/stock/zdroje.json).
SPS Trans nemá vlastné fotky ani web; vzorky = textúry materiálov, priestory = hotové miestnosti."""
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
D = Path(__file__).parent
S, O = D / 'podklady' / 'stock', D / 'img'
O.mkdir(exist_ok=True)
FOTO = {  # výstup: (zdroj, výrez (l, h, p, d) v pomere 0–1 alebo None, pomer (š, v) alebo None)
    'uvod.jpg':            ('k25', None, (4, 5)),                   # svetlá kúpeľňa s obkladom
    'vz-obklad.jpg':       ('42', (0.1, 0.25, 0.9, 0.78), (1, 1)),  # biely obklad kosoštvorce
    'vz-dlazba.jpg':       ('11', None, (1, 1)),                    # terakotová dlažba šachovnica
    'vz-drevo.jpg':        ('13', None, (1, 1)),                    # svetlé dubové drevo
    'vz-omietka.jpg':      ('04', None, (1, 1)),                    # biela štruktúrovaná stena
    'vz-sadrokarton.jpg':  ('37', (0.45, 0.12, 1.0, 0.62), (1, 1)), # sadrokartón s tmelenými spojmi
    'vz-kamen.jpg':        ('26', None, (1, 1)),                    # kamenný obklad
    'vz-podklad.jpg':      ('09', None, (1, 1)),                    # betónová stierka (podklad)
    'kupelna.jpg':         ('k36', None, (4, 3)),                   # obkladačky a kladivo
    'podlaha.jpg':         ('k01', None, (4, 3)),                   # kladenie podlahy (č/b, tónované)
    'steny.jpg':           ('k29', None, (4, 3)),                   # práca v bielej miestnosti z rebríka
    'sadrokarton.jpg':     ('k24', None, (4, 3)),                   # CW profily priečok a podhľadu
    'kamen.jpg':           ('k31', None, (4, 3)),                   # škárovanie dlažby na terase
    'og.jpg':              ('k25', None, (1200, 630)),              # og:image
}
for out, (src, vyrez, pomer) in FOTO.items():
    im = ImageOps.exif_transpose(Image.open(S / f'{src}.jpg')).convert('RGB')
    if vyrez:
        w, h = im.size
        im = im.crop((int(vyrez[0] * w), int(vyrez[1] * h), int(vyrez[2] * w), int(vyrez[3] * h)))
    if pomer:
        sirka = min(im.width, round(im.height * pomer[0] / pomer[1]))
        im = ImageOps.fit(im, (sirka, round(sirka * pomer[1] / pomer[0])), Image.LANCZOS)
    im.thumbnail((2000, 2000), Image.LANCZOS)
    if src == 'k01':  # čiernobiela -> teplý duotón
        g = ImageOps.grayscale(im)
        im = ImageOps.colorize(g, black='#3a3129', white='#fbf6ee', mid='#b3a28c')
    # jednotný jas: tmavé fotky zosvetliť na úroveň úvodnej kúpeľne
    jas = sum(ImageOps.grayscale(im).resize((64, 64)).getdata()) / 4096
    if jas < 150 and not out.startswith('vz-'):
        im = ImageEnhance.Brightness(im).enhance(min(1.35, 150 / jas))
    im = ImageEnhance.Color(im).enhance(0.82)
    # jednotná gradácia: teplé svetlá (omietka), mierne zdvihnuté tiene
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * 1.015 + 3)))
    b = b.point(lambda v: int(v * 0.965 + 4))
    im = Image.merge('RGB', (r, g, b))
    im.save(O / out, quality=86, optimize=True, progressive=True)
    print(out, im.size)
