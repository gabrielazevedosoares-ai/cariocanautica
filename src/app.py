import streamlit as st
from agente import responder_cliente

# Configuração da página
st.set_page_config(page_title="Náutilus AI - Carioca Náutica", page_icon="⚓")

st.title("⚓ Náutilus AI - Carioca Náutica")
st.write("Assistente Virtual de Suporte Operacional e Atendimento")
st.markdown("---")

# Inicializar o histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir as mensagens anteriores na tela
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de texto para o usuário digitar
if prompt := st.chat_input("Como posso ajudar com sua embarcação hoje?"):
    
    # Salva e exibe a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Chama a lógica do nosso agente (Náutilus AI)
    resposta = responder_cliente(prompt)
    
    # Salva e exibe a resposta do assistente
    with st.chat_message("assistant"):
        st.markdown(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
