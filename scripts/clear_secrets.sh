#!/bin/bash
echo "🔐 Buscando posibles secretos..."
grep -r -i 'token\|password\|api_key\|secret' . --exclude-dir={.git,env,venv,.venv} --color
echo "⚠️ Revisa los resultados y elimina o agrega al .gitignore según convenga."
