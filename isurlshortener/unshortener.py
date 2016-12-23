# -*- coding: utf-8 -*-

"""Unshortener Documentation

This module unshortens URLs

"""

import re
import http
from urllib.parse import urlparse
from http import client

from isurlshortener.exceptions import PathMissing, UnhandledHTTPStatusCode, LocationHeaderMissing, ProtocolException


class Unshortener(object):
    @staticmethod
    def unshorten_url(url: str) -> str:
        """Tries to unshorten an URL by requesting it and checking HTTP status

        Args:
            url: URL to check
        Returns:
            True or False
        Raises:
            IsUrlShortener.LocationHeaderMissing: Server did not return a Location
            IsUrlShortener.UnhandledHTTPStatusCode: Unsupported HTTP status code

        """
        url = Unshortener._prepare_url(url)

        if url.path is '' or url.path is '/':
            raise PathMissing()

        server_connection = Unshortener._get_connection(url)
        server_connection.request('GET', url.path)
        response = server_connection.getresponse()

        if response.status in range(300, 309):
            for header_field in response.getheaders():
                if header_field[0] == 'Location':
                    return header_field[1]
            raise LocationHeaderMissing()
        elif response.status in range(200, 201):
            return url.geturl()
        else:
            raise(UnhandledHTTPStatusCode(response.status))

    @staticmethod
    def _prepare_url(url: str) -> dict:
        """Prepares a given URL strict for the unshortener

        Args:
            url: URL prepare
        Returns:
            Dict with the prepared URL information
        Raises:
            IsUrlShortener.ProtocolException: http/https protocol prefix is missing

        """
        if not re.findall('^(http[s]?://)', url):
            raise ProtocolException('Invalid protocol or no protocol given')

        return urlparse(url)

    @staticmethod
    def _get_connection(url: dict) -> [http.client.HTTPConnection, http.client.HTTPSConnection]:
        """Prepares a connection to a given server

        Args:
            url: URL with server information
        Returns:
            Connection to the server
        Raises:
            IsUrlShortener.ProtocolException: Protocol not supported

        """
        if url.scheme == 'http':
            return http.client.HTTPConnection(url.netloc)
        elif url.scheme == 'https':
            return http.client.HTTPSConnection(url.netloc)
        else:
            raise ProtocolException('Protocol Exception: "{}"'.format(url.scheme))
