import os
import shutil

# Caminhos para as pastas de entrada e saída, baseados nos volumes montados
entrada_pasta = '/usr/src/app/entrada'
saida_pasta = '/usr/src/app/saida'

# Verifique se a pasta de entrada existe
if not os.path.exists(entrada_pasta):
    print(f'A pasta de entrada "{entrada_pasta}" não foi encontrada.')
    exit(1)

# Verifique se a pasta de saída existe, se não, crie
if not os.path.exists(saida_pasta):
    os.makedirs(saida_pasta)
    print(f'A pasta de saída "{saida_pasta}" foi criada.')

# Mova os arquivos da pasta de entrada para a pasta de saída
for arquivo in os.listdir(entrada_pasta):
    caminho_entrada = os.path.join(entrada_pasta, arquivo)
    caminho_saida = os.path.join(saida_pasta, arquivo)

    # Verifique se é um arquivo (não uma pasta)
    if os.path.isfile(caminho_entrada):
        try:
            shutil.move(caminho_entrada, caminho_saida)
            print(f'Arquivo "{arquivo}" movido com sucesso.')
        except Exception as e:
            print(f'Erro ao mover o arquivo "{arquivo}": {e}')
    else:
        print(f'Ignorando item não arquivo: "{arquivo}"')

print('Processo de movimentação de arquivos concluído.')
