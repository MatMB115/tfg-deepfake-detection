import os
import shutil


source_path = '/home/maysuwk/Documentos/TCC/preprocessing/WildDeepfake/real/' 
dest_path = '/home/maysuwk/Documentos/TCC/preprocessing/WildDeepfake/sample_train_data' 

sets = ['test', 'train', 'valid']
for set_name in sets:
    os.makedirs(os.path.join(dest_path, set_name, 'real'), exist_ok=True)
    os.makedirs(os.path.join(dest_path, set_name, 'fake'), exist_ok=True)

def copy_files_recursive(src_dir, dest_dir):
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file_name in files:
                full_file_path = os.path.join(root, file_name)
                if os.path.isfile(full_file_path):
                    shutil.copy(full_file_path, dest_dir)

for set_name in sets:
    fake_src = os.path.join(source_path, 'fake', set_name)
    real_src = os.path.join(source_path, 'real', set_name)
    
    fake_dest = os.path.join(dest_path, set_name, 'fake')
    real_dest = os.path.join(dest_path, set_name, 'real')

    copy_files_recursive(fake_src, fake_dest)
    
    copy_files_recursive(real_src, real_dest)

print(f"Estrutura de pastas reorganizada e copiada para {dest_path}")
