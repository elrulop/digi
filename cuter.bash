#!/bin/bash

input_file="video.mp4"  # Nombre del archivo de entrada
output_file="video_recortado.mp4"  # Nombre del archivo de salida
duration="00:01:30"    # Duración del recorte (por ejemplo, 1 minuto y 30 segundos)

ffmpeg -i "$input_file" -t "$duration" -c:v copy -c:a copy "$output_file"
