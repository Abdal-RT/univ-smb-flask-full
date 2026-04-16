#!/bin/bash
echo "Lancement de l'API..."
python src/flask-api/api.py &
echo "Lancement du site..."
python src/flask-website/website.py
