#!/bin/bash

ROOT=$(pwd)
CARPETAS=( "scripts" "docs" "tests" "src" "data" "configs" "notebooks" "logs" "outputs" )

echo "📁 Creando estructura de carpetas en: $ROOT"

for carpeta in "${CARPETAS[@]}"; do
  if [ ! -d "$ROOT/$carpeta" ]; then
    mkdir -p "$ROOT/$carpeta"
    echo "✅ Carpeta creada: $carpeta"
  else
    echo "⚠️ Ya existe: $carpeta"
  fi
done

echo "🎉 Estructura base lista. ¡Listo para construir el Hub!"
