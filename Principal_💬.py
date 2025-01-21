import time
import streamlit as st
from utils import cria_chain_conversa
from utils import PASTA_ARQUIVOS


def sidebar():
    uploaded_files = st.file_uploader(
        'Adicione seus arquivos pdf ou docx', 
        type=['pdf', 'docx'], 
        accept_multiple_files=True
        )
    if not uploaded_files is None:
        for arquivo in list(PASTA_ARQUIVOS.glob('*.pdf')) + list(PASTA_ARQUIVOS.glob('*.docx')):
            arquivo.unlink()
        for pdf in uploaded_files:
            with open(PASTA_ARQUIVOS / pdf.name, 'wb') as f:
                f.write(pdf.read())
    
    label_botao = 'Inicializar Chat'
    if 'chain' in st.session_state:
        label_botao = 'Atualizar Chat'
    if st.button(label_botao, use_container_width=True):
        if len(list(PASTA_ARQUIVOS.glob('*.pdf'))) == 0 and len(list(PASTA_ARQUIVOS.glob('*.docx'))) == 0:
            st.error('Adicione arquivos .pdf ou .docx para inicializar')
        else:
            st.success('Inicializando o Chat...')
            cria_chain_conversa()
            st.rerun()




def chat_window():
    st.header(' 📚 Bem-vindo ao Chat-Analisador', divider=True)

    if not 'chain' in st.session_state:
        st.error('Faça o carregamento de documentos para começar!:)')
        st.stop()

    chain = st.session_state['chain']
    memory = chain.memory

    mensagens = memory.load_memory_variables({})['chat_history']

    container = st.container()
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    nova_mensagem = st.chat_input('Converse com seus dados...')
    if nova_mensagem:
        chat = container.chat_message('human')
        chat.markdown(nova_mensagem)
        chat = container.chat_message('ai')
        chat.markdown('Gerando resposta, aguarde um momento')

        resposta = chain.invoke({'question': nova_mensagem})
        st.session_state['ultima_resposta'] = resposta
        st.rerun()










def main():
    with st.sidebar:
        sidebar()
    chat_window()

if __name__ == '__main__':
    main()
