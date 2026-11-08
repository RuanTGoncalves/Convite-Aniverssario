# Roadmap — Site "A Porta Remendada"

> Ver `CONTEXTO.md` para todas as definições do projeto.

## Fase 0 — Definições ✅ (parcial)
- [x] Data, hora, local
- [x] Estilo pixel art (manter padrão das referências)
- [x] Fotos de referência recebidas (5 fotos em `D:\Convite-Aniversário\`)
- [x] Vaquinha Pix → não vai ter, carne por conta do aniversariante
- [x] Som na página → vai ter, só efeitos 8-bit (sem música de fundo)
- [x] "De maginata" = magnata (terno/charuto)

## Fase 1 — Geração de Assets (PixelLab) 🎨
Ordem sugerida, cada item aprovado antes de seguir pro próximo:

1. [x] **Personagem (você), visual magnata** — terno, charuto, cabelo castanho escuro, aprovado — 8 direções salvas em `assets/personagem/`
   - [x] Pose parada (idle/respirando), postura confiante
   - [x] Pose acenando
   - [x] Pose segurando espeto de churrasco (de terno, sem perder a classe)
   - [x] Pose ajustando a gravata
   - [x] Easter egg: pose "quebrando" o espeto mesmo de terno
   - 5 animações (5 frames cada, direção sul) salvas em `assets/personagem/animacoes/` — geradas com v3 + imagem com cabelo castanho como quadro inicial exato, pra manter consistência (o personagem armazenado no PixelLab ainda tem cabelo preto original; usar os modos template/skeleton puxaria essa versão desatualizada)
2. [x] **Porta** — 3 estados gerados: completa com remendos / rachando / caída no chão — salvos em `assets/porta/`
3. [x] **Barricadas** (5 objetos gerados, para sumir um a um) — salvas em `assets/barricadas/`:
   - Barra de supino com anilhas
   - Cone de cachorro (colar elisabetano)
   - Fita amarela de aviso (texto "BUG — NÃO MEXER" vai como overlay HTML, já que texto fica ilegível em pixel art)
   - Tábuas pregadas
   - Cadeado com corrente (texto "Erro 404" também como overlay HTML)
4. [x] **Cenário do quintal** — churrasqueira, mesa, cooler, bandeirinhas, cerca, pôr do sol — salvo em `assets/cenario/quintal.png` (gerado sem personagens, pra servir de pano de fundo)
5. [x] **VFX** — 3 efeitos animados gerados via vfx_workbench, salvos em `assets/vfx/` (GIF + spritesheet):
   - Impacto/farpas (barricada quebrando)
   - Poeira/estrondo (porta caindo)
   - Fumaça puff (reforço churrasqueira/queda)
6. [x] **UI pixel** — salvo em `assets/ui/` e `assets/icones/`:
   - Botão em branco (reutilizável nos 3 CTAs "Bora!"/"Talvez"/"Não vou" via texto HTML)
   - Moldura/painel ornamentado
   - Fonte pixel customizada "Churrasco Pixel" (TTF + atlas)
   - 3 ícones de acompanhamento: arroz, vinagrete, feijão

✅ **Fase 1 completa.** Saldo PixelLab verificado periodicamente (~186 gerações usadas no projeto até aqui, de 1.282 restantes).

## Fase 2 — Tela da Porta (interação) ✅
- [x] Clique/toque remove barricada com tremida de tela + VFX de impacto + mensagem
- [x] Barra de "integridade da porta" decrescente (verde → amarelo → vermelho)
- [x] Botão discreto "pular introdução"
- [x] Efeitos sonoros 8-bit gerados via Web Audio (sem arquivos), mudo por padrão, liga no 1º toque, botão de mudo flutuante

## Fase 3 — Revelação e Convite ✅
- [x] Porta racha → cai → poeira → revela o quintal
- [x] Personagem com idle animado + 4 poses ao ser cutucado (easter egg na 4ª)
- [x] Bloco com data/hora/endereço + botão "Abrir no Maps"
- [x] Contagem regressiva até 15/11 às 13h (fonte pixel nos números)

## Fase 4 — Confirmação (RSVP) e Acompanhamentos ✅
- [x] Formulário: nome, vai/talvez/não vai, acompanhante (+nome), vegetariano, bebe, recado
- [x] **Envio via WhatsApp pré-preenchido** (ver decisão em CONTEXTO.md §4.1) + botão de copiar como fallback
- [x] Prévia ao vivo da mensagem que será enviada
- [x] 3 cards de acompanhamento (Arroz/Vinagrete/Feijão) selecionáveis, entram na mesma mensagem

## Fase 5 — Painel do Organizador ✅
- [x] Acessível só por `#painel` na URL
- [x] Total de pessoas (com acompanhantes), quantos chegaram
- [x] Lista com check-in, salva no localStorage do navegador
- [x] Lista de compras calculada (carne, pão de alho, bebida, gelo, carvão)

## Fase 6 — Polimento ✅
- [x] Easter egg: cutucar o personagem 4× dispara a animação de quebrar o espeto
- [x] Testado em 375px (mobile) e desktop — sem scroll horizontal, sem imagem quebrada, sem erro de console
- [x] Acessibilidade: barricadas são `<button>` (navegáveis por teclado), foco visível, `prefers-reduced-motion`
- [x] Moldura e placa de madeira com `border-image` fatiado (não deforma o pixel art)
- [x] Fonte pixel aplicada só em números/rótulos ASCII (ela não tem acentos)

## Fase 8 — Ajustes pós-publicação 🔧

### 8.1 A porta: uma só, sendo desobstruída ✅
**Problema:** cada barricada foi gerada com "blocking a doorway", então cada PNG tinha a
própria moldura de porta embutida. Empilhadas, liam-se como cinco portas.

- [x] Regerados os 5 objetos **isolados** via `create_image_pixflux` (1 geração cada,
      5 no total, contra 50 pelo caminho de objeto)
- [x] Recomposta a cena: fita e tábuas pregadas na porta, cadeado na lateral,
      halter encostado na base, cachorro de cone sentado na frente
- [x] A porta agora aparece inteira por baixo e vai sendo liberada
- [x] O cone virou um cachorro usando o cone — melhor pra piada da veterinária

### 8.2 Acompanhamentos saem ✅
- [x] Removidos os 3 cards e a pasta `assets/icones/`
- [x] O que levar virou só: **bebida alcoólica, se for beber**

### 8.3 Confirmação passa pelo grupo ✅
**Restrição:** link de grupo (`chat.whatsapp.com`) não aceita `?text=` pré-preenchido —
só `wa.me` aceita. Por isso o fluxo virou dois passos.

- [x] Passo 1: "Copiar confirmação" (a página monta a mensagem)
- [x] Passo 2: "Entrar no grupo do churrasco" com o link do grupo
- [x] Formulário mantido, alimentando a mensagem que se cola no grupo
- [x] Constante `WHATSAPP` removida (não é mais usada)

### 8.4 Fechamento ✅
- [x] Testado em 320/375px, console limpo
- [x] Publicado

## Fase 7 — Envio 🚀
- [x] Publicado no GitHub Pages: **https://ruantgoncalves.github.io/Convite-Aniverssario/**
- [x] Repositório: https://github.com/RuanTGoncalves/Convite-Aniverssario (fotos pessoais ficaram fora via `.gitignore`)
- [ ] **Colar o número de WhatsApp** na constante `WHATSAPP` no topo do `<script>` do `index.html` e dar push
- [ ] Teste com 2-3 amigos antes do envio geral
