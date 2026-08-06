from .models import ExtractedField


class PredictionDecoder:

    def decode(self, words, predictions, confidence, encoder, boxes=None, page_numbers=None):

        entities = []

        current_label = None
        current_words = []
        current_boxes = []
        current_pages = []
        scores = []

        for index, (word, prediction, score) in enumerate(zip(words, predictions, confidence)):

            label = encoder.decode(prediction)

            if label == "O":
                if current_label:
                    entities.append(self._build_entity(current_label, current_words, current_boxes, current_pages, scores))

                current_label = None
                current_words = []
                current_boxes = []
                current_pages = []
                scores = []

                continue

            prefix, entity = label.split("-", 1)

            if (prefix == "B" or entity != current_label):

                if current_label:
                    entities.append(self._build_entity(current_label, current_words, current_boxes, current_pages, scores))

                current_label = entity
                current_words = [word]
                current_boxes = [self._box_for_index(index, boxes)]
                current_pages = [self._page_for_index(index, page_numbers)]
                scores = [score]

            else:
                current_words.append(word)
                current_boxes.append(self._box_for_index(index, boxes))
                current_pages.append(self._page_for_index(index, page_numbers))
                scores.append(score)

        if current_label:
            entities.append(self._build_entity(current_label, current_words, current_boxes, current_pages, scores))

        return entities

    def _build_entity(self, label, words, boxes, pages, scores):
        return ExtractedField(
            label=label,
            value=" ".join(words),
            confidence=sum(scores) / len(scores),
            page=self._first_value(pages),
            tokens=list(words),
            bbox=self._merge_bbox(boxes),
        )

    def _box_for_index(self, index, boxes):
        if boxes is None:
            return None
        if index < 0 or index >= len(boxes):
            return None
        return boxes[index]

    def _page_for_index(self, index, page_numbers):
        if page_numbers is None:
            return None
        if index < 0 or index >= len(page_numbers):
            return None
        return page_numbers[index]

    def _first_value(self, values):
        for value in values:
            if value is not None:
                return value
        return None

    def _merge_bbox(self, boxes):
        valid_boxes = [box for box in boxes if box is not None]
        if not valid_boxes:
            return None

        x1 = min(box[0] for box in valid_boxes)
        y1 = min(box[1] for box in valid_boxes)
        x2 = max(box[2] for box in valid_boxes)
        y2 = max(box[3] for box in valid_boxes)
        return [x1, y1, x2, y2]