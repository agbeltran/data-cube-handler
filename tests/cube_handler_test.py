import os
import unittest
from unittest.util import safe_repr
from datacube import cube_handler


class TestCubeHandler(unittest.TestCase):

    def setUp(self):
        self._data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.TAB = '\t'
        self.table_file_name = os.path.join(self._data_dir, "table.tsv")

    def assertTrue(self, expr, msg=None):
        """Check that the expression is true."""
        if not expr:
            msg = self._formatMessage(msg, "%s is not true" % safe_repr(expr))
            raise self.failureException(msg)

    def test_table2msq(self):
        pivot_table = cube_handler.table2m_sq(self.table_file_name)
        pivot_table.to_csv("m_sq_output.tsv", sep=self.TAB)
        self.assertTrue()

