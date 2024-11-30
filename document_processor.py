from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def processar_documento(caminho_arquivo, url_endpoint, chave_acesso):
    # Criação do cliente de análise de documentos
    cliente_analise = DocumentAnalysisClient(
        endpoint=url_endpoint, 
        credential=AzureKeyCredential(chave_acesso)
    )
    
    # Abre o arquivo para análise
    with open(caminho_arquivo, "rb") as arquivo:
        poller = cliente_analise.begin_analyze_document("prebuilt-document", document=arquivo)
        resultado = poller.result()
    
    return resultado
