class Logger:

    @staticmethod
    def debug(msg, val=None):
        if val is None:
            print("DEBUG: " + str(msg))
        else:
            print("DEBUG: " + str(msg) + " = " + str(val))
