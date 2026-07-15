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

## Useful Resources

- [PvX Wiki](https://gwpvx.fandom.com/wiki/PvX_wiki)
- [GW1 BUilds](https://www.gw1builds.com/)
- [GW Memorial Template Decoder](https://www.gw-memorial.net/templateDecoder/)
- [GW Memorial Interacive Maps](https://www.gw-memorial.net/interactive-maps/)
