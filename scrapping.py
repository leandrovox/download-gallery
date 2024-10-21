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

    try:
        print("Download está iniciando, aguarde a conclusão...")
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Download concluído!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar a galeria: {e.stderr.decode()}")

def __get_path_name(url):
    # removendo o deviantart
    url_splitted = url.split('.com/')
    # quebrando o resto da url nas barras
    url_splitted = url_splitted[1].split('/')
    # retornar o path completo
    return f"{url_splitted[0]}/{url_splitted[-1]}"

if __name__ == "__main__":
    continue_scrapping = True
    while continue_scrapping:
        gallery_url = input("Digite a URL da galeria DeviantArt: ")
        output_directory = f"./galerias/{__get_path_name(gallery_url)}"
        print(output_directory)
        download_deviantart_gallery(gallery_url, output_directory)

        continue_scrapping = input("Deseja continuar o scrapping? (s/n): ").lower() == "s"
