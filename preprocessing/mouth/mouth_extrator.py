import cv2
import dlib
import os
import argparse
from tqdm import tqdm  # Importar a biblioteca tqdm para a barra de progresso

# Inicializar o detector de face e preditor de landmarks
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Função para extrair a região da boca
def extract_mouth(image, landmarks):
    mouth_points = list(range(48, 68))
    mouth_coords = [(landmarks.part(i).x, landmarks.part(i).y) for i in mouth_points]
    x_min = min([x for x, y in mouth_coords])
    y_min = min([y for x, y in mouth_coords])
    x_max = max([x for x, y in mouth_coords])
    y_max = max([y for x, y in mouth_coords])

    mouth_img = image[y_min:y_max, x_min:x_max]
    mouth_img_resized = cv2.resize(mouth_img, (224, 224))
    return mouth_img_resized

# Função para processar um vídeo e salvar as bocas extraídas
def process_video(video_path, output_dir, label, max_frames):
    # Criar diretório de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Obter o nome do vídeo original (sem extensão)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Ler o vídeo
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Evitar divisão por zero
    frame_interval = max(1, total_frames // max_frames)

    frame_count = 0
    processed_frames = 0

    while processed_frames < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            for face in faces:
                landmarks = predictor(gray, face)
                mouth_img = extract_mouth(frame, landmarks)

                # Salvar a imagem da boca no formato label_frame_nomeDoVideo.jpg
                output_path = os.path.join(output_dir, f"{label}_frame{frame_count}_{video_name}.jpg")
                cv2.imwrite(output_path, mouth_img)
                processed_frames += 1

                if processed_frames >= max_frames:
                    break
        
        frame_count += 1

    cap.release()

# Função principal para processar vários vídeos
def process_dataset(video_dir, output_dir, label, max_frames, pbar):
    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.avi', '.mov'))]
    for video_file in video_files:
        video_path = os.path.join(video_dir, video_file)
        process_video(video_path, os.path.join(output_dir, label), label, max_frames)
        pbar.update(1)  # Atualizar a barra de progresso para cada arquivo processado

# Função para lidar com os argumentos da linha de comando
def main():
    parser = argparse.ArgumentParser(description="Processa vídeos para extrair a boca e separar em pastas fake e real")
    parser.add_argument('--real', type=str, help="Diretório com vídeos reais")
    parser.add_argument('--fake', type=str, help="Diretório com vídeos falsos")
    parser.add_argument('--output_dir', type=str, default='processed_mouth', help="Diretório de saída para as bocas extraídas")
    parser.add_argument('--max_frames', type=int, default=50, help="Número máximo de frames a serem processados por vídeo")

    args = parser.parse_args()

    # Contar o número total de vídeos que serão processados
    total_videos = 0

    if args.real:
        real_videos = [f for f in os.listdir(args.real) if f.endswith(('.mp4', '.avi', '.mov'))]
        total_videos += len(real_videos)

    if args.fake:
        fake_videos = [f for f in os.listdir(args.fake) if f.endswith(('.mp4', '.avi', '.mov'))]
        total_videos += len(fake_videos)

    # Barra de progresso global baseada no número de vídeos
    with tqdm(total=total_videos, desc="Processamento Global", unit="vídeo") as pbar:
        # Processar vídeos reais e falsos
        if args.real:
            process_dataset(args.real, args.output_dir, 'real', args.max_frames, pbar)
        if args.fake:
            process_dataset(args.fake, args.output_dir, 'fake', args.max_frames, pbar)

if __name__ == "__main__":
    main()
