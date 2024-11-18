#!/bin/bash
# Script para dividir os vídeos reais em lotes de 1060 vídeos

source_folder="/run/media/maysuwk/b4918d0e-48e6-4061-a4c3-fa78b840e88c/train/0_real/"
output_base_folder="/run/media/maysuwk/b4918d0e-48e6-4061-a4c3-fa78b840e88c/train/real_batches"
batch_size=1060

mkdir -p "$output_base_folder"

total_videos=$(ls "$source_folder" | wc -l)

total_batches=$(( (total_videos + batch_size - 1) / batch_size ))

echo "Total de vídeos: $total_videos"
echo "Total de lotes: $total_batches"

videos=($(ls "$source_folder"))

for (( i=0; i<total_batches; i++ ))
do
    start=$(( i * batch_size ))
    end=$(( start + batch_size - 1 ))

    batch_folder="$output_base_folder/batch_$((i+1))"
    mkdir -p "$batch_folder"

    for video in "${videos[@]:start:batch_size}"
    do
        cp "$source_folder/$video" "$batch_folder/"
        
        echo "Copiando $video para $batch_folder"
    done
done

echo "Divisão em lotes concluída."
