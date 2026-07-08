# Orion Mercenaries Website

Static website compiled using [staticjinja](https://github.com/staticjinja/staticjinja)

## Requirements

- Python 3

## Dev Setup

```
python -m venv ve
source ve/Scripts/activate
pip install -r requirements.txt
staticjinja watch
```

## Serve Static Files
```
python -m http.server
```

## Deploy

The site is deployed using Github Pages.

To deploy, simple run the following command and then commit and push to main branch.

```
staticjinja build
```
