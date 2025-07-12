
#!/bin/bash

set -e  # Detener el script si algún comando falla

echo "=== Paso 1: Comprobando si git-filter-repo está instalado ==="
if ! command -v git-filter-repo &> /dev/null
then
    echo "git-filter-repo no está instalado. Instalando con pip..."
    if command -v pip &> /dev/null; then
        pip install --user git-filter-repo
        export PATH="$HOME/.local/bin:$PATH"
    else
        echo "ERROR: pip no está instalado. Instálalo antes o instala git-filter-repo manualmente."
        exit 1
    fi
else
    echo "git-filter-repo ya está instalado."
fi

echo "=== Paso 2: Creando archivo con rutas a eliminar ==="
cat > paths-to-remove.txt << EOF
.git-credentials
.config/gh/hosts.yml
.git_token
.bash_history
EOF

echo "=== Paso 3: Ejecutando git filter-repo para limpiar historial ==="
git filter-repo --paths-from-file paths_to_remove.txt --force

echo "=== Paso 4: Agregando reglas a .gitignore para evitar subir secretos nuevamente ==="
# Crear o añadir solo si no existe
if [ ! -f .gitignore ]; then
    touch .gitignore
fi

for path in ".git-credentials" ".config/" ".git_token" ".bash_history"; do
    if ! grep -qxF "$path" .gitignore; then
        echo "$path" >> .gitignore
    fi
done

echo "=== Paso 5: Preparando commit y push ==="
git add .gitignore
git commit -m "Agregar .gitignore para evitar subir secretos"
echo "=== Paso 6: Forzando push al repositorio remoto ==="
git push origin main --force

echo "=== LISTO! El historial está limpio y el push fue forzado exitosamente ==="
echo "IMPORTANTE: Revoca los tokens expuestos y genera nuevos desde GitHub para seguridad."
