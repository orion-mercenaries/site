from staticjinja import Site

if __name__ == "__main__":
    site = Site.make_site(env_globals={
        'STATIC_URL': '/site/',
    })
    site.render()