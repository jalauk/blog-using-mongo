class UnprocessableEntryException(Exception):
    
    def __init__(self, errors: dict):
        Exception.__init__(self)
        self.errors = errors