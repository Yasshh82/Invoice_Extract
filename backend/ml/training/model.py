from transformers import LayoutLMv3ForTokenClassification
from ml.preprocessing.label_encoder import LabelEncoder

def create_model(config, label_map_path):
    encoder = LabelEncoder.load(label_map_path)

    return LayoutLMv3ForTokenClassification.from_pretrained(
        config.model_name,
        num_labels=len(encoder.label_to_id),
        id2label=encoder.id_to_label,
        label2id=encoder.label_to_id,
    )