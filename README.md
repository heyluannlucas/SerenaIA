# Documentação – Primeira Entrega: SerenaIA

## Objetivo do Projeto

O projeto SerenaIA tem como finalidade criar uma **assistente virtual empática**, capaz de manter uma conversa acolhedora com usuários que estejam buscando um espaço de escuta e conforto emocional.

> **Importante:** SerenaIA **não é um substituto para acompanhamento psicológico ou psiquiátrico profissional**. Ela atua como uma ferramenta de acolhimento inicial — um ponto de escuta e apoio para quem busca um momento de diálogo respeitoso.

---

## Por que criar a SerenaIA?

Em momentos de angústia, ansiedade ou solidão, muitas pessoas não sabem com quem conversar ou se sentem constrangidas em procurar ajuda de imediato. SerenaIA foi pensada como:

- Uma **ponte de acolhimento inicial**  
- Uma **companhia virtual** para escutar, acolher e oferecer mensagens positivas  
- Um **instrumento complementar**, nunca substitutivo, ao cuidado com a saúde mental

---

## Sobre SerenaIA

- **Nome:** SerenaIA  
- **Personalidade:** Calma, gentil, compreensiva  
- **Tom:** Acolhedor, respeitoso, empático  
- **Função:** Escutar e responder de forma emocionalmente inteligente

Ela reforça, com sensibilidade, que:

> “Conversar comigo pode aliviar um pouco, mas buscar apoio de um psicólogo ou outro profissional de saúde mental é sempre um passo muito importante.”

---

## Como funciona

- Interface via **linha de comando** e **API REST (Flask)**
- A geração de respostas é feita por IA com base no modelo **`deepseek/deepseek-chat-v3-0324:free`** via OpenRouter
- A IA recebe contexto das últimas mensagens e responde de forma coerente e acolhedora
- As mensagens são preparadas com instruções explícitas para garantir:
  - Empatia  
  - Clareza sobre seu papel como apoio complementar  
  - Encaminhamento sutil à ajuda profissional quando necessário

---

## Componentes do Sistema

Usuário (CLI ou Web)
       │
       ▼
API Flask (/chat)
       │
       ▼
responder.py
   (Monta prompt + contexto)
       │
       ├──────────────► OpenRouter API
       │                    │
       │                    ▼
       └──────────────► odelo: deepseek-chat-v3-0324:free
                             │
                             ▼
Geração de resposta empática (SerenaIA)
       │
       ▼
Retorno ao usuário



## Observações para a banca

- SerenaIA **não faz diagnósticos, nem dá conselhos clínicos**
- Toda a experiência foi desenhada com responsabilidade social e ética
- O projeto pode ser expandido com memória por sessão, logs e interface gráfica
