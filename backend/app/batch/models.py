from dataclasses import dataclass


@dataclass(slots=True)
class BatchProgress:
    batch_id: str
    total: int
    completed: int = 0
    failed: int = 0
    processing: int = 0
    status: str = "Pending"

    @property
    def percentage(self):
        if self.total == 0:
            return 0

        return round((self.completed + self.failed) / self.total * 100, 2)

    def to_dict(self):
        return {
            "batch_id": self.batch_id,
            "status": self.status,
            "total": self.total,
            "completed": self.completed,
            "failed": self.failed,
            "processing": self.processing,
            "percentage": self.percentage,
        }