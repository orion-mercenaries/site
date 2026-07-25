import os
import glob

from staticjinja import Site
from livereload import Server

from om_lib.template_code import decode_gw1_template

# Collect paths to static assets using a wildcard
favicon_paths = glob.glob('templates/**/favicon.ico', recursive=True)
favicons = [os.path.relpath(x, 'templates') for x in favicon_paths]

# Initialize staticjinja Site (pointing to a 'templates' directory and outputting to 'build')
site = Site.make_site(
    searchpath="templates",
    outpath="build",
    staticpaths=["assets", "robots.txt", *favicons],
    env_globals={
        "BASE_URL": "/",
        "decode_gw1_template": decode_gw1_template,
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
