class Logger:

    @staticmethod
    def debug(msg, val=None):
        if val is None:
            print("DEBUG: " + str(msg))
        else:
            print("DEBUG: " + str(msg) + " = " + str(val))

    @staticmethod
    def error(msg, val=None):
        if val is None:
            print("ERROR:" + str(msg))
        else:
            print("ERROR: " + str(msg) + " = " + str(val))
