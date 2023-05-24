class ResponseCode:
    responses = {
        200 : "Success",
        201 : "User Created",
        202 : "Successfully Logged in",
        203 : "Access token reset successfully",

        300 : "Username already exists",
        301 : "User already exists",
        302 : "User doesn't exists",
        303 : "Invalid credentials",
        
        304 : "Token expired",
        305 : "Invalid token",
        306 : "Token doesn't exists"
    }