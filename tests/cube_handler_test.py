import os
import unittest
from unittest.util import safe_repr
from datacube import cube_handler
from datacube import files_comparison


class TestCubeHandler(unittest.TestCase):

    def setUp(self):
        self._data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.TAB = '\t'
        self.table = os.path.join(self._data_dir, "table.tsv")
        self.m_sq = os.path.join(self._data_dir, "m_sq_cube.tsv")
        self.m_sq_output = os.path.join(self._data_dir, "m_sq_output.tsv")
        self.table_from_m_sq = os.path.join(self._data_dir, "table_from_m_sq.tsv")

    def assertTrue(self, expr, msg=None):
        """Check that the expression is true."""
        if not expr:
            msg = self._formatMessage(msg, "%s is not true" % safe_repr(expr))
            raise self.failureException(msg)

    def test_table2m_sq(self):
        pivot_table = cube_handler.table2m_sq(self.table)
        pivot_table.to_csv(self.m_sq_output, sep=self.TAB)
        self.assertTrue(files_comparison.compare(self.m_sq, self.m_sq_output, True), "Files are not the same!")
        #------
        #print(pivot_table.index)
        #### output:
        #### Index(['chem1', 'chem2', 'chem3', 'chem4', 'chem5'], dtype='object', name='chemical entities')
        # -----
        #print(pivot_table.columns)
        #### output:
        # MultiIndex(levels=[['sample1', 'sample2'], ['qt1', 'qt2', 'qt3']],
        #   labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
        #   names=['samples', 'quantitation types'])
        # -----
        # print("--------  pivot_table before resetting index")
        # print(pivot_table)
        # pivot_table = pivot_table.reset_index()
        # print("--------  pivot_table after resetting index")
        # print(pivot_table)
        # -----

    def test_m_sq2table(self):
        table = cube_handler.m_sq2table(self.m_sq)
        table.to_csv(self.table_from_m_sq, sep=self.TAB)
        self.assertTrue(files_comparison.compare(self.table, self.table_from_m_sq, True), "Files are not the same!")