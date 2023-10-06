from django.http import JsonResponse

STATUS_MESSAGES = {
        200: 'OK',
        204: 'No Content',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        307: 'Temporary Redirect',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        412: 'Precondition Failed',
        415: 'Unsupported Media Type',
        422: 'Unprocessable Entity',
        500: 'Internal Server Error',
        501: 'Not Implemented'
}

def sendSuccess(data, status=200):
    return JsonResponse({
        "status": "success",
        "message": STATUS_MESSAGES[status],
        "result": data 
    }, status=200)

def sendError(data, status=400):
    return JsonResponse({
        "status": "failure",
        "message": STATUS_MESSAGES[status],
        "result": data 
    }, status=status)

def validationError(data, status=422):
    return JsonResponse({
        "status": "failure",
        "message": STATUS_MESSAGES[status],
        "result": data 
    }, status=status)
    
    