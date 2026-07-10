from staticjinja import Site

from om_lib.template_code import decode_gw1_template

if __name__ == "__main__":
    site = Site.make_site(
        searchpath="templates",
        outpath="..",
        staticpaths=["assets", "robots.txt", "favicon.ico"],
        env_globals={
            "BASE_URL": "/site/",
            "decode_gw1_template": decode_gw1_template,
        },
    )
    site.render()
