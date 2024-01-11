# noa-chat
un chat de voz interactiva en tiempo real


## instalacion


### paso 1 instalar python 3.11.7
* debian:
```bash
apt install python=3.11.7 python3-dev
```
* arch:
```bash
pacman -S python=3.11.7 python3-dev
```
* macOs: 
```bash
brew install python=3.11.7 python3-dev
```
* windows: [instalador de python](https://www.python.org/downloads/release/python-3117/ 'instala python 3.11.7')
>[!IMPORTANT]
>windows tiene que instalar visual studio con "Desarrollo de escritorio con C++"
>puede instalarlo con el siguiente [link](https://visualstudio.microsoft.com/es/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&passive=false&cid=2030 'descarga Visual Studio 2022')


-----
### paso 2 preparar el entorno para python
1. preparar entorno de escririo
```bash
python -m venv venv
```
2. activar el entorno

  * windows
  1. cmd
```shell
venv\Scripts\activate.bat
```
  2. powershell
```shell
venv\Scripts\Activate.ps1
```
  * linux y MacOs
```shell
source venv/bin/activate
```

-----
### paso 3 instalar las dependencias
```shell
pip install -r requirements.txt
```

-----
### paso 4 ejecutar el programa
```shell
python main.py
```



