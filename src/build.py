from staticjinja import Site

if __name__ == "__main__":
    site = Site.make_site(
        searchpath="templates",
        outpath="..",
        staticpaths=["assets", "robots.txt", "favicon.ico"],
        env_globals={
            "BASE_URL": "/site/",
        },
    )
    site.render()
