import os
import shutil

# Definir o caminho para as pastas de origem e o destino final
source_path = '/home/maysuwk/Documentos/TCC/preprocessing/WildDeepfake/real/'  # Substitua com o caminho correto para a pasta 'fake' e 'real'
dest_path = '/home/maysuwk/Documentos/TCC/preprocessing/WildDeepfake/sample_train_data'  # Substitua com o caminho para o diretório arbitrário

# Criação das novas pastas no diretório de destino
sets = ['test', 'train', 'valid']
for set_name in sets:
    os.makedirs(os.path.join(dest_path, set_name, 'real'), exist_ok=True)
    os.makedirs(os.path.join(dest_path, set_name, 'fake'), exist_ok=True)

# Função para copiar os arquivos de forma recursiva
def copy_files_recursive(src_dir, dest_dir):
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file_name in files:
                full_file_path = os.path.join(root, file_name)
                if os.path.isfile(full_file_path):
                    # Copiando para a pasta de destino mantendo o mesmo nome
                    shutil.copy(full_file_path, dest_dir)

# Copiar arquivos de 'fake' e 'real' para as novas pastas organizadas
for set_name in sets:
    fake_src = os.path.join(source_path, 'fake', set_name)
    real_src = os.path.join(source_path, 'real', set_name)
    
    fake_dest = os.path.join(dest_path, set_name, 'fake')
    real_dest = os.path.join(dest_path, set_name, 'real')
    
    # Copiando arquivos da pasta fake (recursivamente)
    copy_files_recursive(fake_src, fake_dest)
    
    # Copiando arquivos da pasta real (recursivamente)
    copy_files_recursive(real_src, real_dest)

print(f"Estrutura de pastas reorganizada e copiada para {dest_path}")
