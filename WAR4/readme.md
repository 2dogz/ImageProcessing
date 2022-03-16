##running via windows
```console
git clone https://github.com/2dogz/ImageProcessing.git
py -m venv env
.\env\Scripts\activate
cd WAR4
pip install -r requirements.txt
cd website
python app.py
```

##running via raspberry pi
```console
docker pull codebad/python3-opencv
docker run --rm --privileged -it -p 5000:5000 codebad/python3-opencv # for interactive terminal for local development
docker-compose up
```
