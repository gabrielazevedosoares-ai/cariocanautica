# Base de Conhecimento

## Dados Utilizados
Para este projeto, substituímos os dados financeiros originais por dados operacionais do setor náutico, focados estritamente na revenda e instalação de pisos náuticos:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|----------------------|
| `historico_clientes.json` | JSON | Contextualizar interações anteriores, preferências de cor/material e dados do CRM. |
| `pedidos_piso.csv` | CSV | Informar o status atualizado dos pedidos (ex: envio do molde, fabricação, agendamento de instalação). |
| `catalogo_pisos.json` | JSON | Consultar valores por metro quadrado, gabaritos de embarcações, cores e texturas disponíveis (ex: EVA, Teka). |

## Adaptações nos Dados
Os dados mockados originais foram 100% modificados para espelhar a realidade de uma revenda de pisos náuticos. Em vez de perfil de investidor e transações financeiras, criamos listas simulando o fluxo de vendas e operação, contendo status como "Aguardando Molde", "Em Produção" e "Agendado para Instalação". 

## Estratégia de Integração

**Como os dados são carregados?**
Os arquivos JSON e CSV são carregados na memória no início da sessão da aplicação utilizando bibliotecas padrão do Python (como `json` e `pandas`). 

**Como os dados são usados no prompt?**
Os dados são consultados dinamicamente. O agente não carrega o banco de dados inteiro no prompt. Quando o usuário informa o modelo da embarcação, o sistema filtra apenas as opções de piso e o status do pedido correspondente nos arquivos e injeta essas informações específicas como contexto adicional no envio da mensagem para a IA.

## Exemplo de Contexto Montado
Quando um cliente entra em contato, os dados são formatados para o agente da seguinte maneira antes de gerar a resposta:

**Dados do Cliente e Embarcação:**
- Nome: Carlos Eduardo
- Embarcação: Lancha Focker 240
- Preferência Registrada: Piso em EVA cor Madeira/Preto

**Último Pedido Ativo:**
- Data do Pedido: 20/08
- Serviço: Confecção e instalação de piso completo
- Status Atual: Em Produção (Molde já retirado e aprovado)
- Previsão de Instalação: 28/08 na Marina
