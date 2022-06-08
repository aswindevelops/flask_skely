from .functions import generate_final_data
from .loggers import error_logger
import traceback
import sys
from flask import request


def handle_401(error):
    """
    Function to handle the HTTP 401 errors.
    @param error:
    @return: final_data variable in dict format
    """
    final_data = generate_final_data('UNAUTHORIZED')
    return final_data, 401


def handle_404(error):
    """
    Function to handle the HTTP 404 errors.
    @param error:
    @return: final_data variable in dict format
    """
    final_data = generate_final_data('INVALID')
    return final_data, 404


def handle_405(error):
    """
    Function to handle the HTTP 405 errors.
    @param error:
    @return: final_data variable in dict format
    """
    final_data = generate_final_data('INVALID')
    return final_data, 405


def handle_500(e):
    """
    Function to handle the internal server (HTTP 500) errors.
    @param e: Exceptions/error
    @return: final_data variable in dict format
    """
    etype, value, tb = sys.exc_info()
    original = getattr(e, "original_exception", None)
    detailed_traceback = traceback.format_exc()

    final_data = generate_final_data('ERROR')
    log_content = f'Exception Type: {etype} || Value: {value} || Traceback object: {tb} || Traceback details: {detailed_traceback}'

    if original is None:
        # If this method called by Exception handler this wil be called
        error_logger(f'Route: {request.path}').error(log_content)
        return final_data, 500

    # If this method called by a internal server 500 error handler explicitly, this will be called
    error_logger(f'Route: {request.path}').error(log_content)

    return final_data, 500
