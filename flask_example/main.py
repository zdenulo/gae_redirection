import logging
from urlparse import urlparse, urlunparse
from flask import request, redirect, Flask, Response

DOMAIN_NAME = 'mytestdomain.net'

app = Flask('testapp')


@app.before_request
def redirect_nonwww():
    """Redirect requests from naked to www subdomain."""
    url = request.url
    urlparts = urlparse(url)
    if urlparts.netloc == DOMAIN_NAME:
        urlparts_list = list(urlparts)
        urlparts_list[1] = 'www.' + DOMAIN_NAME
        new_url = urlunparse(urlparts_list)
        logging.debug("redirecting from {} to {}".format(url, new_url))
        return redirect(new_url, code=301)


@app.route('/')
def main():
    return Response('Hello world from Flask')


@app.route('/test')
def test():
    return Response('Test url')
