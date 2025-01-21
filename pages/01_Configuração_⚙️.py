import json
import streamlit as st
from configuracoes import get_config
from utils import PASTA_ARQUIVOS, cria_chain_conversa

def config_page():
    st.header('Configurações', divider=True)

    model_name = st.text_input('API', value=get_config('model_name'))
    retrieval_search_type = st.text_input('Retrieval do sistema', value=get_config('retrieval_search_type'))
    retrieval_kwargs = st.text_input('Parâmetros de retrieval', value=json.dumps(get_config('retrieval_kwargs')))
    prompt = st.text_area('Prompt do Sistema', height=500, value=get_config('prompt'))

    if st.button('salvar alterações', use_container_width=True):
            retrieval_kwargs = json.loads(retrieval_kwargs.replace("'", '"'))
            st.session_state['model_name'] = model_name
            st.session_state['retrieval_search_type'] = retrieval_search_type
            st.session_state['retrieval_kwargs'] = retrieval_kwargs
            st.session_state['prompt'] = prompt
            st.rerun()

    if st.button('Salvar', use_container_width=True):
        if len(list(PASTA_ARQUIVOS.glob('*.pdf'))) == 0 and len(list(PASTA_ARQUIVOS.glob('*.docx'))) == 0:
            st.error('Adicione arquivos para atualizar PDF ou DOCX')
            cria_chain_conversa()
            st.rerun()


config_page()
