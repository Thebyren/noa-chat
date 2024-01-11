# Define los argumentos de CMake
$env:CMAKE_ARGS = "-DLLAMA_CUBLAS=on", "-DFORCE_CMAKE=1"

# Crea el entorno virtual
Write-Host "Creando entorno virtual"
python3 -m venv venv

# Activa el entorno virtual
$opt = Read-Host "¿Su dispositivo es Windows? (y/n)"
$activateScript = if ($opt.ToLower() -eq "y") {
    ".\venv\Scripts\Activate.ps1"
} else {
    "source .\venv\bin\activate"
}
# Activa el entorno virtual
Write-Host "Activando entorno virtual"
& $activateScript
# Instala los paquetes necesarios
Write-Host "Instalando paquetes necesarios"
python3 -m pip install --upgrade pip setptools
pip install -r requirements.txt

# Muestra un mensaje indicando que los paquetes están instalados
Write-Host "Paquetes instalados..."

python3 model.py