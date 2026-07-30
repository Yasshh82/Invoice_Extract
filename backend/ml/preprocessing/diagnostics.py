class AlignmentDiagnostics:

    @staticmethod
    def summarize(matches):

        matched = sum(x.status == "matched" for x in matches)

        partial = sum(x.status == "partial" for x in matches)

        unmatched = sum(x.status == "unmatched" for x in matches)

        return (matched, partial, unmatched)