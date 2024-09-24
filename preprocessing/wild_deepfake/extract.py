import os
import shutil
import random
import argparse
import json
from tqdm import tqdm

def copy_sample_images_random(source_base, dest_base, folder_type, num_images=10):
    total_folders = 0
    for index_1 in os.listdir(source_base):
        path_index_1 = os.path.join(source_base, index_1)
        if os.path.isdir(path_index_1):
            path_target = os.path.join(path_index_1, folder_type)
            if os.path.isdir(path_target):
                total_folders += len([f for f in os.listdir(path_target)])

    with tqdm(total=total_folders, desc="Processamento", unit="pasta") as pbar:
        for index_1 in os.listdir(source_base):
            path_index_1 = os.path.join(source_base, index_1)

            if os.path.isdir(path_index_1):
                path_target = os.path.join(path_index_1, folder_type)

                if os.path.isdir(path_target):
                    for index_2 in os.listdir(path_target):
                        path_index_2 = os.path.join(path_target, index_2)

                        if os.path.isdir(path_index_2):
                            image_files = [f for f in os.listdir(path_index_2) if f.endswith(('.png', '.jpg', '.jpeg'))]

                            if len(image_files) >= num_images:
                                sample_files = random.sample(image_files, num_images)
                            else:
                                sample_files = image_files

                            for image in sample_files:
                                new_image_name = f"{index_2}_{image}"
                                source_image_path = os.path.join(path_index_2, image)
                                dest_image_path = os.path.join(dest_base, new_image_name)
                                shutil.copy(source_image_path, dest_image_path)

                            pbar.update(1)

def reorganize_samples_images(source_base, dest_base, folder_type):
    total_folders = 0
    for index_1 in os.listdir(source_base):
        path_index_1 = os.path.join(source_base, index_1)
        if os.path.isdir(path_index_1):
            path_target = os.path.join(path_index_1, folder_type)
            if os.path.isdir(path_target):
                total_folders += len([f for f in os.listdir(path_target)])

    with tqdm(total=total_folders, desc="Reorganizando", unit="pasta") as pbar:
        for index_1 in os.listdir(source_base):
            path_index_1 = os.path.join(source_base, index_1)

            if os.path.isdir(path_index_1):
                path_target = os.path.join(path_index_1, folder_type)

                if os.path.isdir(path_target):
                    for index_2 in os.listdir(path_target):
                        path_index_2 = os.path.join(path_target, index_2)

                        if os.path.isdir(path_index_2):
                            # Criação da nova pasta com o nome index_1_index2
                            new_folder_name = f"{index_1}_{index_2}"
                            new_folder_path = os.path.join(dest_base, new_folder_name)
                            os.makedirs(new_folder_path, exist_ok=True)

                            image_files = [f for f in os.listdir(path_index_2) if f.endswith(('.png', '.jpg', '.jpeg'))]

                            for image in image_files:
                                new_image_name = image
                                source_image_path = os.path.join(path_index_2, image)
                                dest_image_path = os.path.join(new_folder_path, new_image_name)
                                shutil.copy(source_image_path, dest_image_path)

                            pbar.update(1)

def generate_wild_test_json(root_dir, output_dir, output_json="wild_test.json"):
    wild_test_data = []

    real_dir = os.path.join(root_dir, "real")
    fake_dir = os.path.join(root_dir, "fake")

    for subdir in os.listdir(real_dir):
        full_path = os.path.join(real_dir, subdir)
        if os.path.isdir(full_path): 
            wild_test_data.append(f"real/{subdir}")

    for subdir in os.listdir(fake_dir):
        full_path = os.path.join(fake_dir, subdir)
        if os.path.isdir(full_path):  
            wild_test_data.append(f"fake/{subdir}")

    output_json_path = os.path.join(output_dir, output_json)

    with open(output_json_path, "w") as json_file:
        json.dump(wild_test_data, json_file, indent=4)
    
    print(f"JSON file '{output_json_path}' generated successfully.")

def main():
    parser = argparse.ArgumentParser(description="Copiar ou reorganizar imagens em uma estrutura de diretórios.")
    parser.add_argument('--source', type=str, required=True, help="Diretório de origem das imagens")
    parser.add_argument('--destination', type=str, required=True, help="Diretório de destino para as imagens copiadas")
    parser.add_argument('--type', type=str, required=True, help="Tipo de pasta ('real' ou 'fake')")
    parser.add_argument('--frames', type=int, default=10, help="Número de imagens a serem copiadas por pasta (padrão: 10)")
    parser.add_argument('--mode', type=str, required=True, choices=['copy', 'reorganize', 'generate'], help="Modo de execução: 'copy' para copiar imagens aleatórias, 'reorganize' para reorganizar as imagens.")

    args = parser.parse_args()

    os.makedirs(args.destination, exist_ok=True)

    if args.mode == 'copy':
        copy_sample_images_random(args.source, args.destination, args.type, args.frames)
    elif args.mode == 'reorganize':
        reorganize_samples_images(args.source, args.destination, args.type)
    elif args.mode == 'generate':
        generate_wild_test_json(args.source, args.destination)

if __name__ == "__main__":
    main()
