# A Porta Remendada 🚪🔥

Convite interativo para um churrasco de 25 anos. O visitante precisa tirar os entulhos
da frente de uma porta remendada até ela ceder — aí o convite aparece.

**Site:** https://ruantgoncalves.github.io/Convite-Aniverssario/

## Como funciona

| Ato | O que acontece |
|---|---|
| 1. A porta | 5 entulhos clicáveis (supino, cone de cachorro, fita de bug, tábuas, cadeado), cada um com tremida de tela, efeito de impacto, som 8-bit e uma piada. Barra de integridade de 100% a 0%. |
| 2. Revelação | A porta racha, cai com poeira e revela o quintal. O aniversariante aparece animado; cutuque-o para ver outras poses (a 4ª é um easter egg). |
| 3. Convite | Data, hora, endereço com link do Maps e contagem regressiva ao vivo. |
| 4. Confirmação | Formulário que monta uma mensagem formatada, em dois passos: copiar e colar no grupo do WhatsApp. |
| 5. Painel | Área privada em `#painel`: lista de confirmados com check-in e cálculo de compras. |

## ⚙️ O link do grupo

A confirmação acontece no grupo do WhatsApp. O link está no `href` do
elemento `#grupo`, dentro do `index.html`.

Links de convite de grupo (`chat.whatsapp.com`) **não aceitam mensagem
pré-preenchida** — só links de conversa direta (`wa.me`) aceitam `?text=`.
Por isso o fluxo é em dois passos: a página monta a mensagem, a pessoa
copia e cola no grupo depois de entrar.

## Painel do organizador

Acesse a URL do site com `#painel` no final. A lista fica salva no `localStorage`
do seu navegador (só sua, não é compartilhada) e calcula carne, pão de alho,
bebida, gelo e carvão a partir do número de pessoas.

## Foto de perfil do grupo

`avatar/avatar-grupo.png` — 640×640, o tamanho recomendado pelo WhatsApp.
O texto foi posicionado dentro da área que sobrevive ao recorte circular.

Para mudar os dizeres, edite as chamadas de `centralizar()` em
`avatar/montar_avatar.py` e rode da raiz do projeto:

```bash
python avatar/montar_avatar.py
```

Ele confere sozinho se o texto cabe no círculo. A fonte pixel não tem
acentos — use só letras sem acento.

## Estrutura

```
index.html              página inteira (HTML + CSS + JS, sem dependências)
assets/
  personagem/           8 direções + 5 animações de 5 frames
  porta/                3 estados (completa, rachando, caída)
  barricadas/           5 objetos isolados, encostados na porta
  cenario/              quintal do churrasco
  vfx/                  impacto, poeira, fumaça
  ui/                   moldura, placa de botão, fonte pixel
CONTEXTO.md             decisões do projeto
ROADMAP.md              fases e o que foi entregue
```

Toda a arte foi gerada em pixel art com [PixelLab](https://pixellab.ai) e ajustada à mão.
A fonte `Churrasco Pixel` não tem acentos, por isso aparece só em números e rótulos ASCII.
