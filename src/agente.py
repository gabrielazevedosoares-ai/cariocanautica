# Se for usar a API real da OpenAI, você usaria estas bibliotecas:
# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def responder_cliente(mensagem_usuario):
    """
    Função que processa a dúvida do cliente e cruza com as regras de gestão da Carioca Náutica.
    """
    
    # O System Prompt define a "personalidade" e as regras de negócio
    system_prompt = """
    Você é o Náutilus AI, assistente da Carioca Náutica.
    Seu objetivo é agilizar o atendimento, melhorar o NPS e organizar a rotina operacional.
    Só forneça prazos e valores que estejam na nossa base de conhecimento.
    Nunca invente dados. Se não souber, direcione para o atendimento humano.
    """
    
    # SIMULAÇÃO DE RESPOSTA (Para rodar e testar para o projeto da DIO de forma rápida)
    mensagem = mensagem_usuario.lower()
    
    if "revisão" in mensagem or "manutenção" in mensagem:
        return "Consultei nossa base de ordens de serviço. A revisão da sua embarcação está na fase de testes de motor. Previsão de liberação: amanhã às 14h."
    
    elif "peça" in mensagem or "valor" in mensagem or "preço" in mensagem:
        return "Para cotação de peças específicas, preciso confirmar o modelo exato no nosso CRM. Vou transferir você para um de nossos especialistas em rotinas operacionais."
    
    elif "agendar" in mensagem or "passeio" in mensagem:
        return "Ótimo! Para iniciarmos o processo de agendamento e liberação da embarcação, por favor, me informe a data desejada e o nome do proprietário registrado."
    
    else:
        return "Olá! Sou o Náutilus AI da Carioca Náutica. Posso ajudar com o status da sua ordem de serviço, manutenções ou dúvidas operacionais. O que você precisa hoje?"

    # ==========================================
    # CÓDIGO REAL DA API (Comentado para referência)
    # ==========================================
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": system_prompt},
    #         {"role": "user", "content": mensagem_usuario}
    #     ]
    # )
    # return response.choices[0].message.content
