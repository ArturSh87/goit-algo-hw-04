def input_error(handler):
    def wrapped (*args, **kwargs):
        try:
            return handler(*args, **kwargs) 
        except ValueError:
            return "Wrong number of arguments."
        except IndexError:
            return "Missing argument."
    return wrapped    
        