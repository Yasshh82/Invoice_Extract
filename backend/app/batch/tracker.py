from .models import BatchProgress


class BatchTracker:
    def __init__(self):
        self._batches = {}

    def create(self, batch_id, total):
        self._batches[batch_id] = BatchProgress(batch_id=batch_id, total=total, processing=total, status="Processing")

    def completed(self, batch_id):
        batch = self._batches[batch_id]
        batch.completed += 1
        batch.processing -= 1
        self._update(batch)

    def failed(self, batch_id):
        batch = self._batches[batch_id]
        batch.failed += 1
        batch.processing -= 1
        self._update(batch)

    def get(self, batch_id):
        batch = self._batches.get(batch_id)
        if batch is None:
            return None
        return batch.to_dict()

    def _update(self, batch):
        if batch.processing == 0:
            batch.status = "Completed"