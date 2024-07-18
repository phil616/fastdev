
class SharedMemory(dict):
    """
    This is a shared memory for all the process.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SharedMemory, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        ...
    def get(self,key:str):
        return self[key]
        
    def set(self,key:str,value):
        self[key] = value


class GlobalState:
    def __init__(self):
        self.runtime = SharedMemory()

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__.get(item)

GlobalStateObject = GlobalState()

def get_global_state() -> GlobalState:
    return GlobalStateObject
