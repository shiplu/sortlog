import re
from unittest import TestCase

from sortlog.cli import sorted_lines


class TestSortedLines(TestCase):
    def test_sorted_lines(self):
        input_log_1 = [
            "2019-05-08 08:44:21,159 : 1 line 1",
            "2019-05-08 08:44:22,996 : 1 line 2",
            "line 2.1",
            "line 2.2",
            "2019-05-08 08:44:27,000 : 1 line 3",
        ]
        input_log_2 = [
            "2019-05-08 08:44:21,158 : 2 line 1",
            "2019-05-08 08:44:22,995 : 2 line 2",
            "2019-05-08 08:44:26,000 : 2 line 3",
            "line 3.1",
            "line 3.2",
        ]

        input_log_3 = [
            "line 0.1",
            "line 0.2",
            "line 0.3",
            "2019-05-08 08:45:00,000 : 3 line 2",
            "2019-05-08 08:46:00,000 : 3 line 3",
        ]
        expected_output = [
            "2019-05-08 08:44:21,158 : 2 line 1",
            "2019-05-08 08:44:21,159 : 1 line 1",
            "2019-05-08 08:44:22,995 : 2 line 2",
            "2019-05-08 08:44:22,996 : 1 line 2\nline 2.1\nline 2.2",
            "2019-05-08 08:44:26,000 : 2 line 3\nline 3.1\nline 3.2",
            "2019-05-08 08:44:27,000 : 1 line 3",
            "2019-05-08 08:45:00,000 : 3 line 2",
            "2019-05-08 08:46:00,000 : 3 line 3",
        ]

        output = list(
            sorted_lines(
                [input_log_2, input_log_1, input_log_3],
                re.compile("(%s)" % r"^[\d :-]{19},\d+"),
            )
        )

        assert output == expected_output
