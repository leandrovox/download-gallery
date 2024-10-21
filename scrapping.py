import os
import subprocess

def download_deviantart_gallery(url, output_dir):
    # Verifica se o diretório de saída existe, senão cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Comando para usar o gallery-dl com qualidade alta
    command = [
        "gallery-dl",
        "--config", "gallery-dl.conf",
        "--directory", output_dir,  # Define o diretório de saída
        url
    ]

    # Executa o comando e baixa a galeria
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Download concluído!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar a galeria: {e.stderr.decode()}")

# URL da galeria DeviantArt e diretório de destino
gallery_url = ""
output_directory = ""

# Chama a função para baixar a galeria
download_deviantart_gallery(gallery_url, output_directory)
