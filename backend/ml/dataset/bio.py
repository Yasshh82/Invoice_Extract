def create_bio_labels(word_count, alignments):

    labels = ["O" for _ in range(word_count)]

    for alignment in alignments:

        if (alignment.start is None or alignment.end is None):
            continue

        label = alignment.entity_label

        labels[alignment.start] = f"B-{label}"

        for index in range(alignment.start + 1, alignment.end):
            labels[index] = (f"I-{label}")

    return labels