from __future__ import annotations


class Document:
    def __init__(self, corpus_id: int, file_name: str) -> None:
        # Set up instance variables with values
        self._corpus_id = corpus_id
        self._file_name = file_name
        # Set up shared protected attributes without values
        self._matched_flag = False
        self._matched_doc = None

    """Universal setter method inherited by child classes"""

    def set_match(self, doc_obj: type[Document]) -> bool:
        # Update matched_flag and matched_doc for the active document
        self._matched_flag = True
        self._matched_doc = doc_obj
        # Update the respective document object's matched_flag and matched_doc
        doc_obj._matched_flag = True
        doc_obj._matched_doc = self
        return True

    """Universal getter methods inherited by child classes"""

    def get_corpus_id(self) -> int:
        print("Inherited method")
        return self._corpus_id

    def get_file_name(self) -> str:
        print("Inherited method")
        return self._file_name

    def get_matched_flag(self) -> bool:
        print("Inherited method")
        return self._matched_flag

    def get_matched_doc(self) -> type[Document]:
        print("Inherited method")
        return self._matched_doc


class SustDocument(Document):
    def __init__(self, file_name: str, doc_class: str) -> None:
        super().__init__(corpus_id=1, file_name=file_name)
        self.__doc_class = doc_class

    def sust_only(self) -> None:
        print("I'm only in SustDocuments")

    def __str__(self) -> str:
        """String representation of a SustDocument object

        Returns:
            str: String representation of the SustDocument object
        """

        str_rep = (
            f"Corpus ID: {self._corpus_id} | "
            f"File name: {self._file_name} | "
            f"Doc class: {self.__doc_class}"
        )

        return str_rep


class MornDocument(Document):
    def __init__(self, file_name: str, UUID: str) -> None:
        super().__init__(corpus_id=2, file_name=file_name)
        self.__UUID = UUID

    def morn_only(self) -> None:
        print("I'm only in MornDocuments")

    def __str__(self) -> str:
        """String representation of a MornDocument object

        Returns:
            str: String representation of the MornDocument object
        """

        str_rep = (
            f"Corpus ID: {self._corpus_id} | "
            f"File name: {self._file_name} | "
            f"UUID: {self.__UUID}"
        )

        return str_rep


if __name__ == "__main__":
    a = Document(0, "1.txt")
    b = SustDocument("2.txt", "AR")
    c = MornDocument("3.txt", 1234)
    d = SustDocument("4.txt", "CSR")
    b.set_match(c)
    print("")
