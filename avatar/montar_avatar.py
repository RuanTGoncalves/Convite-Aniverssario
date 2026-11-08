"""Monta a foto de perfil do grupo: 640x640, texto dentro da area circular."""
from PIL import Image, ImageDraw, ImageFont

# Para mudar o texto, edite as chamadas de centralizar() mais abaixo.
# A fonte pixel nao tem acentos: use so letras sem acento.
# Rode da raiz do projeto:  python avatar/montar_avatar.py
import os

LADO = 640
AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
CENA = os.path.join(AQUI, "avatar-cena.png")
FONTE = os.path.join(BASE, "assets", "ui", "fonte_churrasco_pixel.ttf")
SAIDA = os.path.join(AQUI, "avatar-grupo.png")

# cena 256x256 ampliada por 2.5 -> 640, vizinho mais proximo pra manter o pixel nitido
cena = Image.open(CENA).convert("RGBA").resize((LADO, LADO), Image.NEAREST)
img = Image.new("RGBA", (LADO, LADO), (20, 13, 10, 255))
img.alpha_composite(cena)

# faixa escura por baixo do texto, so na parte de baixo
faixa = Image.new("RGBA", (LADO, LADO), (0, 0, 0, 0))
fd = ImageDraw.Draw(faixa)
TOPO_FAIXA = 420
for y in range(TOPO_FAIXA, LADO):
    t = (y - TOPO_FAIXA) / (LADO - TOPO_FAIXA)
    fd.line([(0, y), (LADO, y)], fill=(11, 7, 5, int(248 * (t ** 0.75))))
img.alpha_composite(faixa)

d = ImageDraw.Draw(img)


def centralizar(texto, fonte, y, cor, sombra=(0, 0, 0, 255), desloc=5):
    caixa = d.textbbox((0, 0), texto, font=fonte)
    larg = caixa[2] - caixa[0]
    x = (LADO - larg) // 2 - caixa[0]
    d.text((x, y + desloc), texto, font=fonte, fill=sombra)
    d.text((x, y), texto, font=fonte, fill=cor)
    return larg


f_grande = ImageFont.truetype(FONTE, 58)
f_pequena = ImageFont.truetype(FONTE, 30)

l1 = centralizar("BEM-VINDO", f_grande, 452, (255, 206, 84, 255))
l2 = centralizar("AO GRUPO", f_grande, 522, (255, 206, 84, 255))
l3 = centralizar("25 ANOS", f_pequena, 34, (255, 243, 224, 255), desloc=4)

img.convert("RGB").save(SAIDA, "PNG")

# conferencia: o texto cabe dentro do circulo que o WhatsApp recorta?
import math
R = LADO / 2
def meia_largura(y):
    dy = abs(y - R)
    return math.sqrt(max(R * R - dy * dy, 0))

for nome, larg, y in [("BEM-VINDO", l1, 452 + 29), ("AO GRUPO", l2, 522 + 29), ("25 ANOS", l3, 34 + 15)]:
    cabe = larg / 2 <= meia_largura(y)
    print(f"{nome}: {larg:.0f}px de largura, limite do circulo {meia_largura(y)*2:.0f}px -> {'ok' if cabe else 'ESTOURA'}")

print("salvo em", SAIDA)
