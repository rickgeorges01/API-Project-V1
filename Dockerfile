FROM python:3.9

#Création du dossier de l'application du projet 
WORKDIR /app

#Création d'un fichier (requirements) pour lister les dépendances du projet
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/code

EXPOSE 80

#Serveur python, Dossier du fichier python,écoute sur tout les URL, reload à retirer lorsqu'on mettra le serveur en production.
CMD ["uvicorn", "code.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]