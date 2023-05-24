def httpResponse(code,message,data={}):
    return {
        "status": True if code < 300 else False,
        "code" : code,
        "message" : message,
        "data" : data
    }, code