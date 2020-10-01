# -*- coding: utf-8 -*-


def application(environ, start_response):
    output = "<p>Test web python</p>"

    start_response('200 OK',[('Content-Type', 'text/html; charset=utf-8' )])

    return output
