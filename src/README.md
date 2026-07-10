# Orion Mercenaries Website

Static website compiled using [staticjinja](https://github.com/staticjinja/staticjinja)

[Orion Mercenaris](https://orion-mercenaries.github.io/site/)

## Requirements

- Python 3

## Dev Setup

```
cd src
python -m venv ve
source ve/Scripts/activate
pip install -r requirements.txt
python watch.py
```

## Deploy

The site is deployed using Github Pages.

To deploy, simple run the following command and then commit and push to main branch.

```
python build.py
```
