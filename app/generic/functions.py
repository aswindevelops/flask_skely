def generate_final_data(status_code, custom_message=False, key=False):
    """
    Function to generate the final data dict that needs to be sent back to client.
    @param status_code: App specific status_code (string constants)
    @param custom_message: Custom string message
    @param key: specific key
    @return: generated final_data variable
    """
    if status_code == 'INVALID':
        final_data = {"status": "failed", "status_code": status_code, "message": "Invalid request"}

    elif status_code == 'UNAUTHORIZED':
        final_data = {"status": "failed", "status_code": status_code,
                      "message": "Unauthorized access."}

    elif status_code == 'FAILED':
        final_data = {"status": "failed", "status_code": status_code,
                      "message": "Network seems to be busy. Please try again after some time"}

    elif status_code == 'API_KEY_NOT_FOUND':
        final_data = {"status": "failed", "status_code": status_code, "message": "API Key is not provided"}

    elif status_code == 'INVALID_API_KEY':
        final_data = {"status": "failed", "status_code": status_code, "message": "Invalid API key"}

    elif status_code == 'ACCESS_KEY_NOT_FOUND':
        final_data = {"status": "failed", "status_code": status_code, "message": "Access key is not provided"}

    elif status_code == 'INVALID_ACCESS_KEY':
        final_data = {"status": "failed", "status_code": status_code, "message": "Invalid Access key"}

    elif status_code == 'CUSTOM_FAILED':
        final_data = {"status": "failed", "status_code": status_code, "message": custom_message}

    elif status_code == 'KEY_NOT_PROVIDED':
        final_data = {"status": "failed", "status_code": status_code, "message": f"The key '{key}' is not provided"}

    elif status_code == 'ERROR':
        final_data = {"status": "failed", "status_code": status_code, "message": "Please try again after some time"}

    elif status_code == 'FORM_ERROR':
        final_data = {"status": "failed", "status_code": status_code, "message": "Validation error"}

    elif status_code == 'DATA_SAVE_FAILED':
        final_data = {"status": "failed", "status_code": status_code, "message": "Failed to save the data"}

    elif status_code == 'DATA_UPDATE_FAILED':
        final_data = {"status": "failed", "status_code": status_code, "message": "Failed to update the data"}

    elif status_code == 'DATA_DELETE_FAILED':
        final_data = {"status": "failed", "status_code": status_code, "message": "Failed to delete the data"}

    elif status_code == 'SUCCESS':
        final_data = {"status": "success", "status_code": status_code, "message": "Success"}

    elif status_code == 'CUSTOM_SUCCESS':
        final_data = {"status": "success", "status_code": status_code,
                      "message": custom_message}
    elif status_code == 'DATA_FOUND':
        final_data = {"status": "success", "status_code": status_code, "message": "Data retrieved successfully"}

    elif status_code == 'DATA_NOT_FOUND':
        final_data = {"status": "success", "status_code": status_code, "message": "No data found"}

    elif status_code == 'DATA_SAVED':
        final_data = {"status": "success", "status_code": status_code, "message": "Data saved successfully"}

    elif status_code == 'DATA_UPDATED':
        final_data = {"status": "success", "status_code": status_code, "message": "Data updated successfully"}

    elif status_code == 'DATA_DELETED':
        final_data = {"status": "success", "status_code": status_code, "message": "Data deleted successfully"}

    else:
        final_data = {"status": "failed", "status_code": status_code, "message": "Invalid request"}

    return final_data


def populate_errors(errors):
    """
    Method for populating errors from WTF forms
    @param errors: Flask-WTF form errors object
    @return: Final list of errors
    """
    final = []
    for key, values in errors.items():
        final.append({'field': key, 'errors': values})
    return final
