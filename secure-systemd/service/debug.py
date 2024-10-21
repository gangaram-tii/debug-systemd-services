# Global flag to control printing
ENABLE_TRACE = False

def enable_traces():
    global ENABLE_TRACE
    ENABLE_TRACE = True

def trace(*args, **kwargs):
    global ENABLE_TRACE
    if ENABLE_TRACE:
        print(*args, **kwargs)
