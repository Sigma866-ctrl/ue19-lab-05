# 1. Image de base
# Utilise une image officielle légère de Python (3.11 est un bon choix stable)
FROM python:3.11-slim-buster

# 2. Variables d'environnement et métadonnées (optionnel mais recommandé)
# Définir l'encodage pour éviter les problèmes avec les caractères français
ENV PYTHONIOENCODING=utf-8

# 3. Répertoire de travail
# Crée un répertoire de travail dans le conteneur où l'application résidera
WORKDIR /app

# 4. Copier et installer les dépendances
# Copie le fichier requirements.txt
COPY requirements.txt .

# Installe les dépendances Python spécifiées dans requirements.txt
# L'option --no-cache-dir réduit la taille finale de l'image
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier l'application
# Copie votre script Python dans le répertoire de travail (/app)
COPY blague.py .

# 6. Commande d'exécution
# Commande par défaut à exécuter au démarrage du conteneur
# 'python blague.py' sera exécuté
CMD ["python", "blague.py"]
