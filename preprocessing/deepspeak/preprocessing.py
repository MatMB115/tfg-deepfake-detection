import os
import cv2
import json
import shutil
import random
import string
import mediapipe as mp
import argparse
from tqdm import tqdm
from math import floor

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def get_frame_interval(total_frames, num_frames):
    return max(1, total_frames // num_frames)

def extract_faces_from_video(video_path, face_output_dir, log_file, num_frames=15, is_fake=False):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = get_frame_interval(total_frames, num_frames)
    count = 0
    extracted_frame_count = 0

    os.makedirs(face_output_dir, exist_ok=True)

    video_filename = os.path.splitext(os.path.basename(video_path))[0]

    with open(log_file, 'a') as log, mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        with tqdm(total=num_frames, desc=f"Processando {video_filename}", unit="frame") as pbar:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                if count % frame_interval == 0 and extracted_frame_count < num_frames:
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    result = face_detection.process(rgb_frame)

                    if result.detections:
                        for i, detection in enumerate(result.detections):
                            bboxC = detection.location_data.relative_bounding_box
                            ih, iw, _ = frame.shape
                            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

                            face_img = frame[y:y+h, x:x+w]
                            
                            if face_img.size > 0:
                                face_resized = cv2.resize(face_img, (224, 224))

                                face_filename = f"{video_filename}_frame_{extracted_frame_count}.jpg"

                                face_path = os.path.join(face_output_dir, face_filename)
                                cv2.imwrite(face_path, face_resized)
                            else:
                                log.write(f"Erro: A face extraída no frame {extracted_frame_count} é inválida.\n")
                    else:
                        log.write(f"Nenhuma face detectada no frame {extracted_frame_count} do vídeo {video_filename}.\n")

                    extracted_frame_count += 1
                    pbar.update(1)

                count += 1

    cap.release()

def process_videos(video_dir, output_dir, log_file, num_frames=15, is_fake=False):
    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.avi', '.mov'))]

    with tqdm(total=len(video_files), desc="Processando vídeos", unit="vídeo") as pbar_videos:
        for video_file in video_files:
            video_path = os.path.join(video_dir, video_file)
            extract_faces_from_video(video_path, output_dir, log_file, num_frames, is_fake)
            pbar_videos.update(1)

def split_data(src_dir, dest_dir, train_ratio=0.8, valid_ratio=0.15, test_ratio=0.05):
    train_dir = os.path.join(dest_dir, 'train')
    valid_dir = os.path.join(dest_dir, 'valid')
    test_dir = os.path.join(dest_dir, 'test')
    
    for category in ['fake', 'real']:
        category_src = os.path.join(src_dir, category)

        all_images = os.listdir(category_src)
        random.shuffle(all_images)

        total_images = len(all_images)
        train_count = floor(train_ratio * total_images)
        valid_count = floor(valid_ratio * total_images)
        test_count = total_images - train_count - valid_count

        train_images = all_images[:train_count]
        valid_images = all_images[train_count:train_count + valid_count]
        test_images = all_images[train_count + valid_count:]

        def move_images(images, source, destination):
            os.makedirs(destination, exist_ok=True)
            for img in images:
                shutil.move(os.path.join(source, img), os.path.join(destination, img))

        move_images(train_images, category_src, os.path.join(train_dir, category))
        move_images(valid_images, category_src, os.path.join(valid_dir, category))
        move_images(test_images, category_src, os.path.join(test_dir, category))

    print("Imagens reorganizadas com sucesso!")

def generate_deepspeak_json(root_dir, output_dir, output_json="deepspeak.json"):
    deepspeak_data = []

    real_dir = os.path.join(root_dir, "real")
    fake_dir = os.path.join(root_dir, "fake")

    for video in os.listdir(real_dir):
        deepspeak_data.append(f"real/{video}")


    for video in os.listdir(fake_dir):
        deepspeak_data.append(f"fake/{video}")

    output_json_path = os.path.join(output_dir, output_json)

    with open(output_json_path, "w") as json_file:
        json.dump(deepspeak_data, json_file, indent=4)
    
    print(f"JSON file '{output_json_path}' generated successfully.")

def anonymize_filenames(video_dir):
    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.avi', '.mov'))]
    anonymized_videos = {}

    for video_file in video_files:
        new_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + os.path.splitext(video_file)[1]
        old_path = os.path.join(video_dir, video_file)
        new_path = os.path.join(video_dir, new_name)

        os.rename(old_path, new_path)
        anonymized_videos[video_file] = new_name

    print(f"Anonymized {len(video_files)} video files.")
    return anonymized_videos

def main():
    parser = argparse.ArgumentParser(description="Processar vídeos ou organizar imagens.")
    parser.add_argument('--source', type=str, required=True, help="Diretório onde os vídeos/imagens estão localizados.")
    parser.add_argument('--output', type=str, required=True, help="Diretório onde as informações serão salvas.")
    parser.add_argument('--log', type=str, default="processing_log.txt", help="Arquivo de log para salvar os erros e frames ignorados.")
    parser.add_argument('--num_frames', type=int, default=15, help="Número de frames a serem processados de cada vídeo (padrão: 15).")
    parser.add_argument('--fake', action='store_true', help="Especificar se os vídeos ou imagens processadas são fake.")
    parser.add_argument('--task', type=str, choices=['process_videos', 'organize_images', 'generate_json', 'anonymize_videos'], required=True, help="Escolha a tarefa.")

    args = parser.parse_args()

    if args.task == 'process_videos':
        process_videos(args.source, args.output, args.log, args.num_frames, args.fake)
    elif args.task == 'organize_images':
        split_data(args.source, args.output)
    elif args.task == 'generate_json':
        generate_deepspeak_json(args.source, args.output)
    elif args.task == 'anonymize_videos':
        anonymize_filenames(args.source)
    else:
        print("Invalid Task.")

if __name__ == "__main__":
    main()
