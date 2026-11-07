# Contexto do Projeto — Convite de Aniversário (25 anos)

## 1. O aniversariante
- Veterinário e também estudante/profissional de engenharia de software (projeto pessoal paralelo)
- Frequenta academia (físico atlético, corpo definido)
- **Fama de quebrar tudo que toca** — essa é a piada central do site
- Referências visuais: 5 fotos em `D:\Convite-Aniversário\` (arquivos `WhatsApp Image 2026-11-07...jpeg`)

### Características físicas (para gerar o personagem pixel art)
- Cabelo curto, escuro (preto/castanho escuro), levemente ondulado, penteado para cima/lado
- Pele morena/tom médio (bronzeado)
- Olhos castanhos escuros
- Barba rala estilo cavanhaque + bigode fino (não é barba cheia)
- Sem óculos nas fotos de referência
- Porte atlético, academia (ombros/peito definidos — visto na foto de praia)
- Sorriso aberto, expressão simpática/extrovertida

## 2. Evento
- **Data:** dia 15
- **Horário:** 13h (13 hora da tarde)
- **Local:** Rua das Orquídeas, Condomínio Villaggio Jardins 3
- **Tipo:** Churrasco de aniversário — 25 anos
- **Carne:** o aniversariante paga (sem vaquinha de dinheiro)
- **Acompanhamentos:** lista cômica de "ajuda" para quem quiser contribuir trazendo/fazendo arroz, vinagrete ou feijão (ver seção 5.1)
- Som na página: confirmado que vai ter — ver seção 6.1 para opções

## 3. Conceito criativo
**Tema:** "A Porta Remendada" — piada visual sobre a fama de quebrar tudo.

### Mecânica
1. Usuário abre o link e vê uma **porta de madeira cheia de remendos** (fita silver, durepoxi, pregos tortos, plaquinha "consertado por mim, não encoste")
2. Na frente da porta, **barricadas temáticas** cobrindo partes da vida do aniversariante:
   - 🏋️ Barra de supino travando a porta (academia) → "Supino de 120kg? Quebrou o banco junto."
   - 🐶 Cone de cachorro elisabetano gigante (veterinária) → "Até o paciente fugiu dessa porta."
   - 💻 Fita amarela "BUG — NÃO MEXER" (engenharia de software) → "Funciona na minha máquina."
   - 🪵 Tábuas pregadas → "Pregou, quebrou, pregou de novo."
   - 🔒 Cadeado com "Erro 404" → "Cadeado não encontrado."
3. Cada clique remove uma barricada, com tremida de tela, partículas de farpa/poeira e a mensagem correspondente
4. Barra de "integridade da porta" diminuindo a cada clique (estilo barra de vida de chefe de jogo)
5. Último clique: **a porta cai inteira** → revela o aniversariante em pixel art no quintal do churrasco, vestido de **magnata** (terno, charuto, talvez chapéu/relógio de luxo) — contraste cômico com a fama de quebrar tudo
6. Abaixo da revelação: informações do evento, contagem regressiva, formulário de confirmação

### Easter eggs planejados
- Clicar várias vezes no personagem → cadeira quebra
- Botão "Não vou" foge do mouse (ou dá uma resposta engraçada ao ser clicado)
- Botão discreto de "pular introdução" para quem tiver pressa (acessibilidade/paciência)

## 4. Estilo visual
- Pixel art, paleta quente (tons de churrasco: laranja, vermelho, marrom madeira) + verde do quintal
- Resolução: personagem ~64px, cenário estilo 16-bit
- Mobile-first (maioria vai abrir pelo link do WhatsApp)

## 4.1 ⚠️ Decisão de arquitetura (importante)
A ideia original era gravar as confirmações num banco compartilhado do Artifact do claude.ai.
**Isso não é possível:** a plataforma só permite escrita de quem está na mesma organização
Claude (nível "Contributor" ou acima). Visitantes externos com o link ficam em "somente leitura",
mesmo com as regras mais abertas — a própria API recusa `write: "view"` na publicação.

**Decisão final:** o site é um **HTML standalone** (`index.html`, sem dependência do claude.ai)
e a confirmação é enviada por **link de WhatsApp pré-preenchido**. A pessoa preenche o
formulário, o site monta a mensagem formatada e abre o WhatsApp com ela pronta.
Zero conta, zero login, funciona pra qualquer amigo.

O painel do organizador virou uma área privada acessível por `#painel` na URL, onde o
aniversariante anota manualmente quem foi confirmando (salvo no `localStorage` do navegador dele)
e vê o cálculo automático de carne, bebida, pão de alho, gelo e carvão.

## 5. Funcionalidade de confirmação (RSVP)

### 5.1 Lista de ajuda com acompanhamentos (substitui a vaquinha)
A carne é por conta do aniversariante — não tem vaquinha de dinheiro. Em vez disso, uma seção cômica tipo **"Resgate de Acompanhamentos"**, encaixando no tom de "eu quebro tudo, mas não cozinho tudo sozinho":
- Texto de abertura (algo como): *"Eu já quebrei liquidificador, fogão e um pedaço da minha dignidade tentando fazer arroz. Se alguém quiser salvar o churrasco..."*
- 3 cards/itens disponíveis: **Arroz 🍚**, **Vinagrete 🥗**, **Feijão 🫘**
- Cada item tem um botão "Eu levo/faço esse!" — ao clicar, a pessoa digita o nome e o item fica marcado como reservado (via banco de dados compartilhado, pra não duplicar)
- Se os 3 já estiverem reservados, mostra algo tipo "Prato dos sonhos realizado. Agora é só rezar pra carne não queimar."
- Campo opcional de item "outro", caso alguém queira levar outra coisa (sobremesa, bebida, etc.)

Cada resposta captura:
1. Nome de quem confirma
2. Vai? → "Bora! 🍖" / "Talvez 🤔" / "Não vou 😢"
3. Leva acompanhante? → Sozinho(a) / +1 (namorado/namorada), com campo de nome do acompanhante
4. Opcional: restrição alimentar (vegetariano), bebe álcool
5. Campo livre de recado para o aniversariante

### Painel do organizador (visão separada)
- Total de confirmados contando acompanhantes
- Lista de "talvez" para cobrar
- Calculadora automática de carne (~400g/pessoa) e bebida
- Lista nome + acompanhante para check-in no dia do evento

## 6. Stack / Ferramentas

### 6.1 Como o som vai funcionar
- Efeitos sonoros curtos estilo 8-bit/chiptune (sem música com direito autoral — tudo gerado/royalty-free)
- Por política dos navegadores, som não pode tocar sozinho ao abrir a página: só começa a tocar depois do primeiro clique do usuário (encaixa perfeitamente com a mecânica de clicar na porta)
- Botão de mudo sempre visível, e começa **mudo por padrão** (silencioso) até a pessoa decidir ativar
- Candidatos de efeito:
  - Som de impacto/rachadura em cada clique na barricada
  - Estrondo + poeira quando a porta cai
  - "Ding" de confirmação ao enviar o RSVP
  - Chiacoalho/crepitar de fogo ambiente na tela da revelação (opcional, em loop baixo)
- **Decidido: só efeitos sonoros, sem música de fundo/chiptune**

- **Artifact (claude.ai)** como página publicada (HTML + capability de banco de dados compartilhado para o RSVP)
- **PixelLab MCP** para gerar os assets: personagem, porta (3 estados), barricadas individuais, cenário, VFX (farpas, poeira, fumaça), UI em pixel font
- Skills já carregadas no projeto: `artifact-design`, `artifact-capabilities`, `dataviz` (para o painel do organizador)

## 7. Pendências a confirmar com o usuário
- [x] Vaquinha via Pix → **não vai ter**; carne por conta do aniversariante
- [x] Som na página → **vai ter**, só efeitos 8-bit (sem música de fundo) (ver 6.1)
- [ ] Aprovação do personagem pixel art antes de gerar o resto dos assets
- [x] "De maginata" = **magnata** — personagem vestido de terno/charuto na revelação
- [x] Cor do cabelo ajustada para **castanho escuro** (edição manual de pixel, sem gastar geração do PixelLab) — 8 direções salvas em `assets/personagem/magnata_*.png`
