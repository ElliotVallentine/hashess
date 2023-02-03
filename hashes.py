import os
import hashlib
import sqlite3

pasta_arquivos = './img/'
database_folder = './db/'


def gerador_hash():
    # [] listar todos os arquivos dentro da pasta img
    nomes_arquivos = os.listdir(pasta_arquivos)
    for nome_arquivo in nomes_arquivos:
        caminho_arquivo = os.path.join(pasta_arquivos, nome_arquivo)
    # [] extrair os bytes do arquivo atual listado.
        with open(caminho_arquivo, 'rb') as data_byte:
            image_byte = data_byte.read()
    # [] gerar um md5 do byte do arquivo atual listado
        hashs = hashlib.md5(image_byte).hexdigest()
    # [] imprimir no terminal o hash gerado
        print(f'hashes: {hashs}')
    # [] estabelecer contato com a database
    if not os.path.exists(database_folder):
        os.makedirs(database_folder)
    conection_database = sqlite3.connect(f'{database_folder}hashes.db')
    cursor = conection_database.cursor()
    # [ ] criar parâmetro na database
    cursor.execute("CREATE TABLE IF NOT EXISTS images(hashes)")
    # [ ] enviar arquivos de database
    response = cursor.execute("SELECT name FROM sqlite_master")
    cursor.execute(f"""
    INSERT INTO images VALUES ('{hashs}')""") 
    conection_database.commit()
    response = cursor.execute("SELECT hashes FROM images")
    print(f'\n{response.fetchall()}')
    # [ ] acessar database
    conection_database.close()
    new_conection_database = sqlite3.connect(f'{database_folder}hashes.db')
    new_cursor = new_conection_database.cursor()
    response = new_cursor.execute("SELECT hashes FROM images")



gerador_hash()
