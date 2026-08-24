# Avaliação e Métricas

## Como Avaliar seu Agente
A avaliação do Náutilus AI pode ser feita de duas formas complementares:

- **Testes estruturados:** Você define perguntas e respostas esperadas simulando o contato de clientes da marina;
- **Feedback real:** Pessoas (ou a própria equipe comercial) testam o agente e dão notas para a fluidez do atendimento.

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste na Carioca Náutica |
|---|---|---|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar a diferença entre EVA e Termodeck e receber a explicação correta. |
| **Segurança** | O agente evitou inventar informações? | Perguntar o valor do m² para uma lancha não tabelada e ele pedir para consultar o comercial. |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir Termodeck para um cliente que prioriza um piso que não esquenta ao sol. |

> **Dica:** Peça para 3 a 5 pessoas (colegas da revenda ou amigos que conheçam barcos) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Caso use os arquivos da pasta `data/`, lembre-se de contextualizar os participantes sobre os modelos de embarcação cadastrados.

---

## Exemplos de Cenários de Teste
Crie testes simples para validar seu agente de vendas:

**Teste 1: Consulta de status do pedido**
- **Pergunta:** "Como tá a fabricação do piso da minha lancha?"
- **Resposta esperada:** Agente solicita o modelo da lancha e retorna o status baseado no arquivo `pedidos_piso.csv` (ex: "Em produção").
- **Resultado:** [ ] Correto  [ ] Incorreto

**Teste 2: Recomendação de material (Kapazi Náutica)**
- **Pergunta:** "Quero um piso macio e confortável. Qual vocês têm?"
- **Resposta esperada:** Produto compatível com a necessidade (EVA Soft Tech Premium).
- **Resultado:** [ ] Correto  [ ] Incorreto

**Teste 3: Pergunta fora do escopo**
- **Pergunta:** "Vocês fazem revisão de motor de popa?"
- **Resposta esperada:** Agente informa que a Carioca Náutica é focada exclusivamente na revenda de pisos náuticos Kapazi.
- **Resultado:** [ ] Correto  [ ] Incorreto

**Teste 4: Informação inexistente/restrita**
- **Pergunta:** "Quanto o meu amigo pagou no Termodeck do barco dele?"
- **Resposta esperada:** Agente recusa compartilhar dados de terceiros e se oferece para fazer um orçamento novo.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados
Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [A preencher após os testes - ex: O agente soube explicar muito bem as vantagens do piso atérmico.]

**O que pode melhorar:**
- [A preencher após os testes - ex: O agente demorou a pedir o modelo da embarcação logo na primeira interação.]

---

## Métricas Avançadas (Opcional)
Para quem quer explorar mais a fundo a operação comercial, algumas métricas técnicas de observabilidade também podem ser monitoradas:

- Latência e tempo de resposta (crucial para atendimento no WhatsApp/Site);
- Consumo de tokens e custos da API por orçamento gerado;
- Logs e taxa de erros em orçamentos.
