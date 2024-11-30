from connection_settings import conexao_string, nome_container, url_endpoint, chave_acesso
from file_uploader import enviar_arquivo
from document_processor import processar_documento
from fraud_detection import detectar_fraude, verificar_autenticidade

def pipeline_principal():
    caminho_arquivo = "meuarquivo.pdf"

    # Envio do arquivo
    enviar_arquivo(caminho_arquivo, conexao_string, nome_container)

    # Processamento do documento
    resultado = processar_documento(caminho_arquivo, url_endpoint, chave_acesso)

    # Detecção de fraudes e verificação de autenticidade
    detectar_fraude(resultado)
    verificar_autenticidade(resultado)

if __name__ == "__main__":
    pipeline_principal()
