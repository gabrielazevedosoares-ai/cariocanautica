# ⚓ Assistente Virtual Inteligente - Carioca Náutica

## Contexto

Este projeto é a entrega do Lab "Construa Seu Assistente Virtual Com Inteligência Artificial". O desafio original focava em um agente financeiro, mas este projeto foi **adaptado para o setor náutico**, focando na rotina operacional, contato com clientes e organização de serviços da **Carioca Náutica**.

O objetivo é criar um assistente inteligente (Náutilus AI) capaz de:
- **Agilizar o atendimento** ao cliente para dúvidas sobre embarcações.
- **Consultar o status** de ordens de serviço e manutenções.
- **Garantir segurança** nas respostas, sem inventar prazos ou preços que não estejam na base de dados.

---

## Os 6 Passos do Projeto

### 1. Documentação do Agente
- **Caso de Uso:** O agente resolve o gargalo de comunicação entre a equipe operacional e os clientes. Ele informa status de manutenção, verifica disponibilidade de peças e auxilia no agendamento de serviços.
- **Persona:** *Náutilus AI*. Tom de voz profissional, ágil e habituado aos termos técnicos de marinharia e gestão operacional.
- **Segurança:** O agente tem instruções estritas para não alucinar. Se um prazo ou preço não estiver no sistema, ele transfere para o atendimento humano.

### 2. Base de Conhecimento
Os dados utilizados para alimentar o agente refletem a rotina náutica (arquivos localizados na pasta `data/`):
- `ordens_servico.csv`: Histórico e status das manutenções das embarcações.
- `clientes.json`: Perfil dos proprietários e histórico de contato (CRM).
- `tabela_servicos.json`: Catálogo de peças, preços e serviços de marinharia.

### 3. Prompts do Agente
O *System Prompt* foi desenhado para atuar como um gestor de processos:
- **Restrição de IA:** "Você é um assistente da Carioca Náutica. Só informe preços e prazos presentes na base de conhecimento. Se não souber, diga que um técnico entrará em contato."
- **Exemplo de Interação:** Se o cliente pergunta "Minha lancha já fez a revisão?", o agente cruza o nome do cliente no `.json` com o status no `.csv` e responde o andamento exato.

### 4. Aplicação Funcional
O protótipo (localizado na pasta `src/`) foi pensado para rodar em uma interface simples de chat (como Streamlit ou Gradio), conectando o modelo de linguagem (LLM) aos arquivos locais que simulam as ferramentas de gestão (como Trello/CRM).

### 5. Avaliação e Métricas
Para garantir que o agente é útil para a Carioca Náutica, avaliamos:
- **Assertividade:** O agente acertou o status da ordem de serviço?
- **Segurança (Anti-Alucinação):** Ele inventou alguma peça ou serviço que a empresa não presta?
- **Resolução:** A resposta diminuiu o tempo de espera do cliente?

### 6. Pitch do Projeto
- **O Problema:** Na correria da rotina náutica, clientes ficam aguardando retornos simples sobre manutenções e documentações de embarcações, sobrecarregando a equipe.
- **A Solução:** O Náutilus AI, um assistente virtual que cruza a base de dados operacionais e responde o cliente na hora, 24/7.
- **O Valor:** Maior eficiência nos processos gerenciais, cliente mais satisfeito (aumento do NPS) e equipe focada no trabalho técnico em vez de responder mensagens repetitivas.
