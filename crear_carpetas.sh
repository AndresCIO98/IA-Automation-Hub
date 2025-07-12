#!/bin/bash

# Script para crear carpetas desde una lista

INPUT="data/nombres.txt"
LOG="data/logs/registro_creacion.log"

echo "🟢 Iniciando creación de carpetas..." > "$LOG"
while IFS= read -r line; do
    mkdir -p "data/$line"
    echo "✅ Carpeta creada: data/$line" >> "$LOG"
done < "$INPUT"

echo "🏁 Proceso finalizado." >> "$LOG"

