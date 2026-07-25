import os
import glob

from staticjinja import Site

from om_lib.template_code import decode_gw1_template

if __name__ == "__main__":
    # Collect paths to static assets using a wildcard
    favicon_paths = glob.glob('templates/**/favicon.ico', recursive=True)
    favicons = [os.path.relpath(x, 'templates') for x in favicon_paths]

    site = Site.make_site(
        searchpath="templates",
        outpath="..",
        staticpaths=["assets", "robots.txt", *favicons],
        env_globals={
            "BASE_URL": "/site/",
            "decode_gw1_template": decode_gw1_template,
        },
    )
    site.render()
