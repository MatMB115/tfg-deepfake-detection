#!/bin/zsh

PYTHON_EXEC="/home/maysuwk/Documentos/TCC/TFG-UNIFEI-scope-review-about-deepfakes-detection/local/bin/python"
SCRIPT_PATH="/home/maysuwk/Documentos/TCC/TFG-UNIFEI-scope-review-about-deepfakes-detection/preprocessing/mouth/mouth_extrator.py"

REAL_VIDEOS_PATH="/home/maysuwk/Documentos/TCC/preprocessing/Celeb-real/"
FAKE_VIDEOS_BASE_PATH="/home/maysuwk/Documentos/TCC/preprocessing/Celeb-fake/"

OUTPUT_DIR="/home/maysuwk/Documentos/TCC/preprocessing/"

MAX_FRAMES=30

WINDOW_DIMENSIONS="800x130+100+100" 

echo "Processando vídeos reais em: $REAL_VIDEOS_PATH"
konsole --hold --geometry $WINDOW_DIMENSIONS -e bash -c "echo 'Processando $REAL_VIDEOS_PATH'; $PYTHON_EXEC $SCRIPT_PATH --real $REAL_VIDEOS_PATH --output_dir $OUTPUT_DIR --max_frames $MAX_FRAMES" &

for i in {1..8}; do
    FAKE_VIDEOS_PATH="${FAKE_VIDEOS_BASE_PATH}_${i}"
    echo "Processando vídeos falsos em: $FAKE_VIDEOS_PATH"
    konsole --hold --geometry $WINDOW_DIMENSIONS -e bash -c "echo 'Processando $FAKE_VIDEOS_PATH'; $PYTHON_EXEC $SCRIPT_PATH --fake $FAKE_VIDEOS_PATH --output_dir $OUTPUT_DIR --max_frames $MAX_FRAMES" &
done

echo "Todos os processos foram iniciados em novas janelas do Konsole"
