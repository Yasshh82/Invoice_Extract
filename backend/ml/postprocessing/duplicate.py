class DuplicateResolver:
    @staticmethod
    def choose(values):
        if not values:
            return None

        # Choose the value with the highest confidence
        return max(values, key=lambda x: x.confidence)