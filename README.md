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
| 4. Confirmação | Formulário que monta uma mensagem formatada e abre o WhatsApp já preenchido. |
| 5. Painel | Área privada em `#painel`: lista de confirmados com check-in e cálculo de compras. |

## ⚙️ Configurar antes de divulgar

Abra `index.html` e preencha o número de WhatsApp que recebe as confirmações:

```js
var WHATSAPP = "5562999887766"; // 55 + DDD + número, só dígitos
```

Enquanto estiver vazio, o botão copia a mensagem para a área de transferência
em vez de abrir o WhatsApp — a página continua funcionando.

## Painel do organizador

Acesse a URL do site com `#painel` no final. A lista fica salva no `localStorage`
do seu navegador (só sua, não é compartilhada) e calcula carne, pão de alho,
bebida, gelo e carvão a partir do número de pessoas.

## Estrutura

```
index.html              página inteira (HTML + CSS + JS, sem dependências)
assets/
  personagem/           8 direções + 5 animações de 5 frames
  porta/                3 estados (completa, rachando, caída)
  barricadas/           5 objetos
  cenario/              quintal do churrasco
  vfx/                  impacto, poeira, fumaça
  ui/                   moldura, placa de botão, fonte pixel
  icones/               arroz, vinagrete, feijão
CONTEXTO.md             decisões do projeto
ROADMAP.md              fases e o que foi entregue
```

Toda a arte foi gerada em pixel art com [PixelLab](https://pixellab.ai) e ajustada à mão.
A fonte `Churrasco Pixel` não tem acentos, por isso aparece só em números e rótulos ASCII.
