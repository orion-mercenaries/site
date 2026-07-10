from staticjinja import Site
from livereload import Server

from om_lib.template_code import render_template_code

# Initialize staticjinja Site (pointing to a 'templates' directory and outputting to 'build')
site = Site.make_site(
    searchpath="templates",
    outpath="build",
    staticpaths=["assets", "robots.txt", "favicon.ico"],
    env_globals={
        "BASE_URL": "/",
        "render_template_code": render_template_code,
    },
)

# Build the site initially
site.render()

# Start the Livereload server
server = Server()

# Watch the templates folder and rebuild the site when changes occur
server.watch("templates/", site.render)

# Serve the static files on localhost:8000
server.serve(root="build", port=8000)
