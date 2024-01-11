import subprocess

def load_cmake_args():
    try:
        subprocess.run(["CMAKE_ARGS='-DLLAMA_CUBLAS=on'", "-DFORCE_CMAKE=1"], shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting CMake arguments: {e}")

def create_virtualenv():
    try:
        print('creando entorno virtual')
        subprocess.run(["python", "-m", "venv", "venv"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")

def install_packages():
    print('instalando paquetes necesarios')
    subprocess.run(["pip", "install", "-r", "requirements.txt"], shell=True,check=True)

def activate_venv(opt):
    if opt:
        print('activando entorno virtual (Windows)')
        subprocess.run([".\\venv\\Scripts\\Activate.ps1"], check=True)
    else:
        print('activando entorno virtual (Linux/macOS)')
        subprocess.run(["source", "./venv/bin/activate"], check=True,shell=True)  # Still using shell for source

def main():
    try:
        load_cmake_args()
        print('Su dispositivo es Windows? (y/n)')
        _opt = input()
        opt = _opt.lower() == "y"
        create_virtualenv()
        activate_venv(opt)
        install_packages()
        print('paquetes instalados...')
    except Exception as e:
        print(f"Error during setup: {e}")
        return

    try:
        import model
    except Exception as e:
        print(f'Error durante la carga del modelo: {e}')
main()
