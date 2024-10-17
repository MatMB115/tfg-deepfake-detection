import os
import argparse
import shutil

def copy_selected_files(video_folder, destination_folder, num_to_keep, tipo):
    first_number_files = {}

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(video_folder):
        if filename.endswith('.mp4'):
            if(tipo == "fake"):
                first_number = filename.split('--')[1]
            else:
                first_number = filename.split('-')[0]
            if first_number not in first_number_files:
                first_number_files[first_number] = [filename]
            else:
                first_number_files[first_number].append(filename)

    for first_number, files in first_number_files.items():
        files_to_copy = files[:num_to_keep]
        
        for file_to_copy in files_to_copy:
            src_path = os.path.join(video_folder, file_to_copy)
            dest_path = os.path.join(destination_folder, file_to_copy)
            shutil.copy2(src_path, dest_path)
            print(f'Copiado: {src_path} -> {dest_path}')

    print("Processo de cópia concluído!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copiar arquivos com número inicial repetido para outra pasta.")
    parser.add_argument("--src", help="Caminho para a pasta dos vídeos")
    parser.add_argument("--dest", help="Caminho para a pasta de destino")
    parser.add_argument("--number", type=int, help="Número de arquivos a manter para cada número inicial")
    parser.add_argument("--t", help="tipo")

    args = parser.parse_args()

    copy_selected_files(args.src, args.dest, args.number, args.t)
