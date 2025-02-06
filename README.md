![image](https://github.com/user-attachments/assets/255fffd3-4a7c-4a47-9c45-2dd06d9f2f86)
![image](https://github.com/user-attachments/assets/80f79062-6e8e-4a6f-ac8e-7bec8481a466)


# Modelo RAG (Retrieval-Augmented Generation)

Este é um projeto básico que implementa um sistema de Resposta Baseada em Recuperação (RAG - Retrieval-Augmented Generation) utilizando Streamlit e LangChain. Ele permite carregar documentos em formato PDF ou DOCX e iniciar um chatbot que analisa e responde perguntas com base no conteúdo dos arquivos fornecidos. O sistema é altamente configurável e inclui funções de depuração para validação e ajuste.

## Visão Geral

Este projeto combina Streamlit e LangChain para criar um sistema de interação direta com arquivos PDF e DOCX. Ele permite consultas claras e detalhadas com base no conteúdo dos documentos, mantendo precisão e consistência ao longo da conversa. Diferentemente de modelos como ChatGPT, Claude e Gemini, este sistema não sofre com alucinações ou perda de informações ao longo do diálogo, sendo ideal para análise e interpretação de documentos no dia a dia.

## Características Principais

1. **Suporte a múltiplas APIs**: Compatível com OpenAI e Groq para processamento de linguagem.
2. **Interface interativa**: Upload de arquivos e chat diretamente no navegador.
2. **Armazenamento vetorial eficiente**: Implementado com FAISS para busca por similaridade.
2. **Personalização total**: Parâmetros do modelo, tipo de busca e prompt podem ser ajustados.
2. **Depuração integrada**: Ferramentas para inspecionar o contexto e o histórico de interação.

## Limitações

- O desempenho depende da qualidade e do tamanho dos documentos carregados.
- Não suporta processamento de imagens ou documentos não estruturados.

## Como Executar

1. **Clone o repositório**:
```bash
git clone <repository-url>
cd <repository-folder>
```

2. **Instale as dependências**: Certifique-se de ter Python 3.8+ instalado.
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente**: Crie um arquivo .env na raiz do projeto com sua chave de API:
```bash
OPENAI_API_KEY=<sua-chave-api>
GROQ_API_KEY=<sua-chave-api>
```

4. **Inicie a aplicação:**:
```bash
streamlit run Principal.py
```







  
