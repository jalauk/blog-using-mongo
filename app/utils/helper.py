from app.utils.responseCode import ResponseCode
def httpResponse(code,message="",data={},http_code = 200):
    return {
        "status": True if code < 300 else False,
        "code" : code,
        "message" : message if message else ResponseCode.responses[code],
        "data" : data
    }, http_code if code < 400 else code 