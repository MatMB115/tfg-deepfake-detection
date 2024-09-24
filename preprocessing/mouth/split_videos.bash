#!/bin/bash

VIDEO_DIR="/home/maysuwk/Documentos/TCC/preprocessing/Celeb-synthesis/"

OUTPUT_DIR_PREFIX="/home/maysuwk/Documentos/TCC/preprocessing/"
threads=8

for (( i=1; i<=threads; i++ ))
do
    mkdir -p "${OUTPUT_DIR_PREFIX}_$i"
done

total_videos=$(ls -1 "$VIDEO_DIR" | wc -l)

videos_por_pasta=$((total_videos / threads))
resto=$((total_videos % threads))

indice=1
for video in "$VIDEO_DIR"/*
do
    pasta=$(( (indice - 1) % threads + 1 ))

    mv "$video" "${OUTPUT_DIR_PREFIX}_$pasta/"

    indice=$((indice + 1))
done

echo "Vídeos distribuídos nas pastas."
