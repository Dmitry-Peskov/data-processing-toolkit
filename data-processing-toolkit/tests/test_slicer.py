from data_processing_toolkit.slicer import cut_into_slices


class TestCutIntoSlices:

    test_string = "Строка для тестирования функции cut_into_slices."
    test_list = ["Строка", "для", "тестирования", "функции", "cut_into_slices."]
    test_tuple = ("Строка", "для", "тестирования", "функции", "cut_into_slices.")
    test_set = {"Строка", "для", "тестирования", "функции", "cut_into_slices."}
    test_empty_string = ""
    test_empty_list = []
    test__empty_tuple = ()
    test_empty_set = {}
    even_size = 2
    odd_size = 3

    def test_string_even_size(self):
        assert cut_into_slices(self.test_string, self.even_size) == [
            "Ст",
            "ро",
            "ка",
            " д",
            "ля",
            " т",
            "ес",
            "ти",
            "ро",
            "ва",
            "ни",
            "я ",
            "фу",
            "нк",
            "ци",
            "и ",
            "cu",
            "t_",
            "in",
            "to",
            "_s",
            "li",
            "ce",
            "s.",
        ]

    def test_string_odd_size(self):
        assert cut_into_slices(self.test_string, self.odd_size) == [
            "Стр",
            "ока",
            " дл",
            "я т",
            "ест",
            "иро",
            "ван",
            "ия ",
            "фун",
            "кци",
            "и c",
            "ut_",
            "int",
            "o_s",
            "lic",
            "es.",
        ]

    def test_empty_string_even_size(self):
        assert cut_into_slices(self.test_empty_string, self.even_size) == []

    def test_empty_string_odd_size(self):
        assert cut_into_slices(self.test_empty_string, self.odd_size) == []

    def test_list_even_size(self):
        assert cut_into_slices(self.test_list, self.even_size) == [
            ["Строка", "для"],
            ["тестирования", "функции"],
            ["cut_into_slices."],
        ]

    def test_list_odd_size(self):
        assert cut_into_slices(self.test_list, self.odd_size) == [
            ["Строка", "для", "тестирования"],
            ["функции", "cut_into_slices."],
        ]

    def test_empty_list_even_size(self):
        assert cut_into_slices(self.test_empty_list, self.even_size) == []

    def test_empty_list_odd_size(self):
        assert cut_into_slices(self.test_empty_list, self.odd_size) == []
