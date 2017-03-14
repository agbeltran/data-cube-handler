import os
import unittest
from unittest.util import safe_repr
from datacube import cube_handler
from datacube import files_comparison


class TestCubeHandler(unittest.TestCase):

    def setUp(self):
        self._data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.TAB = '\t'
        self.table_file_name = os.path.join(self._data_dir, "table.tsv")
        self.m_sq = os.path.join(self._data_dir, "m_sq_cube.tsv")
        self.m_sq_output = os.path.join(self._data_dir, "m_sq_output.tsv")

    def assertTrue(self, expr, msg=None):
        """Check that the expression is true."""
        if not expr:
            msg = self._formatMessage(msg, "%s is not true" % safe_repr(expr))
            raise self.failureException(msg)

    def test_table2msq(self):
        pivot_table = cube_handler.table2m_sq(self.table_file_name)
        pivot_table.to_csv(self.m_sq_output, sep=self.TAB)
        files_comparison.compare(self.m_sq, self.m_sq_output, True)

