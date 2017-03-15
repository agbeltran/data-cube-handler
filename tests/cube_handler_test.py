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

        self.m_sq = os.path.join(self._data_dir, "m_sq.tsv")
        self.m_sq_h5 = os.path.join(self._data_dir, "m_sq.h5")
        self.m_sq_output = os.path.join(self._data_dir, "m_sq.tsv")

        self.s_mq = os.path.join(self._data_dir, "s_mq.tsv")
        self.s_mq_h5 = os.path.join(self._data_dir, "s_mq.h5")
        self.s_mq_output = os.path.join(self._data_dir, "s_mq_output.tsv")

        self.ms_q = os.path.join(self._data_dir, "ms_q.tsv")
        self.ms_q_h5 = os.path.join(self._data_dir, "ms_q.h5")
        self.ms_q_output = os.path.join(self._data_dir, "ms_q_output.tsv")

        self.table_from_m_sq = os.path.join(self._data_dir, "table_from_m_sq.tsv")

    def assertTrue(self, expr, msg=None):
        """Check that the expression is true."""
        if not expr:
            msg = self._formatMessage(msg, "%s is not true" % safe_repr(expr))
            raise self.failureException(msg)

    ### Test for converting table into M_SQ configuration
    def test_table2m_sq(self):
        table = cube_handler.table2m_sq(self.table)
        table.to_csv(self.m_sq_output, sep=self.TAB)
        table.to_hdf(self.m_sq_h5, 'df', mode='w', format='fixed')
        self.assertTrue(files_comparison.compare(self.m_sq, self.m_sq_output, True), "Files are not the same!")

    ### Test for converting table into S_MQ configuration
    def test_table2s_mq(self):
        table = cube_handler.table2s_mq(self.table)
        table.to_csv(self.s_mq_output, sep=self.TAB)
        table.to_hdf(self.s_mq_h5, 'df', mode='w', format='fixed')
        self.assertTrue(files_comparison.compare(self.s_mq, self.s_mq_output, True), "Files are not the same!")

    def test_m_sq2s_mq(self):
        s_mq_df = cube_handler.m_sq2s_mq(self.m_sq_h5)
        s_mq_df.to_csv(self.s_mq_output, sep=self.TAB)
        self.assertTrue(files_comparison.compare(self.s_mq, self.s_mq_output, True), "Files are not the same!")

    def test_s_mq2m_sq(self):
        m_sq_df = cube_handler.s_mq2m_sq(self.s_mq_h5)
        m_sq_df.to_csv(self.m_sq_output, sep=self.TAB)
        self.assertTrue(files_comparison.compare(self.m_sq, self.m_sq_output, True), "Files are not the same!")

    def test_table2ms_q(self):
        ms_q = cube_handler.table2ms_q(self.table)
        ms_q.to_csv(self.ms_q_output, sep=self.TAB)
        ms_q.to_hdf(self.ms_q_h5, 'df', mode='w', format='fixed')
        self.assertTrue(files_comparison.compare(self.ms_q, self.ms_q_output, True), "Files are not the same!")
