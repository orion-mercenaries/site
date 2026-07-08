from staticjinja import Site

if __name__ == "__main__":
    site = Site.make_site(env_globals={
        'BASE_URL': '/',
    })
    site.render(use_reloader=True)
