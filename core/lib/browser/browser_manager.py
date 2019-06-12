class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        uniq_id = cls.__name__
        exists = cls._instances.get(uniq_id, False)

        if not exists:
            cls._instances[uniq_id] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[uniq_id]


class BrowserManager(metaclass=Singleton):

    def __init__(self):
        self._cache = {}

    def get(self, cls, host, port):
        hash_id = (cls.__name__, host, port)
        exists = self._cache.get(hash_id, False)

        if not exists:
            self._cache[hash_id] = cls(host, port)

        return self._cache[hash_id]

    def remove(self, cls, host, port):
        hash_id = (cls.__name__, host, port)
        exists = self._cache.get(hash_id, False)

        if exists:
            del self._cache[hash_id]
