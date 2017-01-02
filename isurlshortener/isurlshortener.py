# -*- coding: utf-8 -*-

"""IsUrlShortener Documentation

This module answer the question if a given URL is a URL from an URL shortener service

"""

import os
import re


class IsUrlShortener(object):

    """IsUrlShortener

    This class contains all required program logic.
    """

    @staticmethod
    def is_url_shortener(url: str) -> bool:
        """Checks if a given URL is from an active URL shortener

        Args:
            url: URL to check
        Returns:
            True or False
        """
        return IsUrlShortener._is_in_servicelist(url, 'data/shortener_services.txt')

    @staticmethod
    def is_disabled_url_shortener(url: str) -> bool:
        """Checks if a given URL is from an inactive URL shortener

        Args:
            url: URL to check
        Returns:
            True or False
        """
        return IsUrlShortener._is_in_servicelist(url, 'data/former_shortener_services.txt')

    @staticmethod
    def is_or_was_from_url_shortener(url: str) -> bool:
        """Checks if a given URL or domain is from an in-/active URL shortener

        Args:
            url: URL to check
        Returns:
            True or False
        """
        return IsUrlShortener.is_disabled_url_shortener(url) or \
               IsUrlShortener.is_url_shortener(url)

    @staticmethod
    def _is_in_servicelist(service_domain: str, servicelist: str) -> bool:
        """Checks if a given URL is included in a given service list

        Args:
            url: URL to check
            servicelist: File containing the services to consider
        Returns:
            True or False
        Raises:
            FileNotFoundError: If servicelist is not found
        """
        if not service_domain:
            return False

        with open(os.path.join(os.path.dirname(__file__), servicelist), 'r') as shortener_list:
            for shortener in shortener_list:
                regex = '(http[s]?://)?{}(/.*)?'.format(shortener.rstrip().replace('.', '\.'))
                if len(re.findall(regex, service_domain)) > 0:
                    return True
        return False
