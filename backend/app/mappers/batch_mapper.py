from app.schemas.batch import (
    BatchResponse,
)

class BatchMapper:

    @staticmethod
    def to_response(batch):

        finished = batch.completed + batch.failed

        return BatchResponse(
            id=batch.id,
            status=batch.status,
            total=batch.total,
            completed=batch.completed,
            failed=batch.failed,
            percentage=round(finished / batch.total * 100, 2),
            created_at=batch.created_at,
            finished_at=batch.finished_at,
        )
