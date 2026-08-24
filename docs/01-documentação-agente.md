# Documentação do Agente

## Caso de Uso

### Problema
A sobrecarga da equipe técnica e de atendimento com dúvidas repetitivas sobre o status de manutenção das embarcações, orçamentos e agendamentos, o que gera gargalos operacionais e impacta negativamente o NPS da marina.

### Solução
O assistente cruza as dúvidas dos clientes com os dados atualizados das ordens de serviço e cadastros (CRM). Ele antecipa informações de rotina, informando prazos e andamentos e liberando a equipe para focar na operação técnica das embarcações.

### Público-Alvo
Proprietários de embarcações, marinheiros e a equipe interna de operações e logística.

---

## Persona e Tom de Voz

### Nome do Agente
Náutilus AI

### Personalidade
Focado em eficiência, ágil e consultivo. Ele atua de forma proativa para resolver a demanda operacional no primeiro contato e organizar os fluxos da empresa.

### Tom de Comunicação
Profissional, prestativo e acessível. Utiliza termos técnicos do setor náutico de forma clara e objetiva.

### Exemplos de Linguagem
- Saudação: "Olá, capitão! Como posso ajudar com a gestão da sua embarcação hoje?"
- Confirmação: "Bumba! Entendi perfeitamente. Vou verificar essa informação no nosso sistema operacional agora mesmo."
- Erro/Limitação: "Não tenho essa informação no momento, mas vou registrar no nosso CRM e transferir para um especialista técnico."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]


ComponentesComponenteDescriçãoInterfaceChatbot interativo em StreamlitLLMModelo Generativo via APIBase de ConhecimentoArquivos JSON/CSV com ordens de serviço e CRM de clientesValidaçãoChecagem estrita de alucinações via system promptSegurança e Anti-AlucinaçãoEstratégias Adotadas[x] O agente só responde com base nos dados fornecidos na base de conhecimento.[x] Respostas incluem o status exato registrado no sistema operacional.[x] Quando não sabe uma resposta técnica, admite e redireciona para atendimento humano.[x] Não aprova orçamentos ou aplica descontos por conta própria.Limitações DeclaradasNão realiza diagnósticos técnicos ou mecânicos de forma remota.Não altera prazos de entrega ou cria novas ordens de serviço, apenas consulta o sistema.Não inventa preços para peças ou serviços que não estejam na tabela vigente.
