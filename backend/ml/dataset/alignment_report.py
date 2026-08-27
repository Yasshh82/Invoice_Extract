from collections import Counter


def print_alignment_report(diagnostics):

    status_counter = Counter()

    entity_counter = Counter()

    for result in diagnostics:
        status_counter[result.status] += 1
        entity_counter[(result.entity_label, result.status)] += 1

    print("\nAlignment Status")

    for status, count in status_counter.items():
        print(f"{status}: {count}")

    print("\nEntity Alignment")

    for key, count in entity_counter.items():
        label, status = key

        print(
            f"{label:15} "
            f"{status:20} "
            f"{count}"
        )