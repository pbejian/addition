# Addition

<p align="center">
  <img src="docs/vignette.jpg" alt="Addition de deux nombres" width="480">
</p>

Mini-application Streamlit : deux nombres, un bouton, leur somme.

Elle sert surtout à valider de bout en bout la chaîne de déploiement :
du code Python au conteneur Docker, servi en HTTPS sur mon propre serveur.

- **Démo en ligne :** https://addition.bejian.fr
- **Page du projet dans mon portfolio :** https://www.bejian.fr/project/addition
- **Portfolio :** https://www.bejian.fr

## Lancer en local

    uv sync
    uv run streamlit run app.py

## Lancer avec Docker

    docker build -t addition .
    docker run -p 8501:8501 addition

## Déploiement

Image Docker sur un VPS, derrière un reverse proxy Caddy (HTTPS automatique).

## Stack

Python 3.14 · Streamlit · uv · Docker · Caddy

---

Pierre BÉJIAN · [bejian.fr](https://bejian.fr)
