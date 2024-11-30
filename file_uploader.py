from azure.storage.blob import BlobServiceClient

def enviar_arquivo(caminho_arquivo, conexao_string, nome_container):
    # Criação do cliente do serviço Blob
    cliente_blob = BlobServiceClient.from_connection_string(conexao_string)
    cliente_container = cliente_blob.get_container_client(nome_container)
    
    # Envia o arquivo para o container
    with open(caminho_arquivo, "rb") as dados:
        cliente_container.upload_blob(name="meuarquivo.pdf", data=dados)
