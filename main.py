from Document import SustDocument, MornDocument
import pandas as pd


def create_corpus_data(docs: list) -> list:
    docs_data = []
    for doc in docs:
        row_data = [
            doc.get_corpus_id(),
            doc.get_file_name(),
            doc.get_matched_flag(),
            doc.get_matched_doc().get_file_name()
            if doc.get_matched_flag()
            else "No match",
        ]
        docs_data.append(row_data)
    return docs_data


def create_corpus_df(data: list) -> pd.DataFrame:
    df = pd.DataFrame(
        data,
        columns=[
            "corpus_id",
            "file_name",
            "_matched_flag",
            "matched_doc_file_name",
        ],
    )
    return df


if __name__ == "__main__":
    b = SustDocument("2.txt", "AR")
    c = MornDocument("3.txt", 1234)
    d = SustDocument("4.txt", "CSR")
    
    b.set_match(c)

    docs = [b, c, d]

    corpus_data = create_corpus_data(docs)
    corpus_df = create_corpus_df(corpus_data)
