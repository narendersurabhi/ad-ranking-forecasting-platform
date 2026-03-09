class InMemoryMetrics:
    def __init__(self):
        self.counters = {}

    def inc(self, key: str, val: int = 1):
        self.counters[key] = self.counters.get(key, 0) + val

    def snapshot(self):
        return dict(self.counters)
