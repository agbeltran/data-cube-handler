import pandas as pd
import numpy as np

TAB = '\t'

# M stands for metabolites/chemical entities
# S stands for samples
# Q stands for quantitation types

# The two most important configurations are M_SQ and S_MQ

def table2m_sq(table_filename):
    """
    Convert a table to a pivoted table with index 'M' and columns 'S' and 'Q'
    :param table_filename:
    :return: data frame
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, index=['chemical entities'], columns=['samples', 'quantitation types'], values='data points')
    return pivot_table


def m_sq2s_mq(m_sq_h5_filename):
    df = pd.read_hdf(m_sq_h5_filename, 'df')
    t_df = df.stack().stack().reset_index()
    t_df.columns = ['chemical entities', 'quantitation types', 'samples', 'data points']
    pivot_table = pd.pivot_table(t_df, values='data points', index=['samples'],
                                 columns=['chemical entities', 'quantitation types'])
    return pivot_table

def s_mq2m_sq(s_mq_h5_filename):
    df = pd.read_hdf(s_mq_h5_filename, 'df')
    t_df = df.stack().stack().reset_index()
    t_df.columns = ['chemical entities', 'quantitation types', 'samples', 'data points']
    pivot_table = pd.pivot_table(t_df, values='data points', index=['chemical entities'],
                                 columns=['samples', 'quantitation types'])
    return pivot_table


def table2ms_q(table_filename):
    """
    Convert a table to a pivoted table with index 'M' and 'S' and column 'Q'
    :param table_filename:
    :return: data frame
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['chemical entities', 'samples'], columns=['quantitation types'])
    return pivot_table

def table2m_qs(table_filename):
    """
    Convert a table to a pivoted table with index 'M' and columns 'Q' and 'S'
    :param table_filename:
    :return: data frame
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, index=['chemical entities'], columns=['quantitation types', 'samples'], values='data points')
    return pivot_table


def table2mq_s(table_filename):
    """
    Convert a table to a pivoted table with index 'M' and 'Q' and column 'S'
    :param table_filename:
    :return: data frame
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, index=['chemical entities', 'quantitation types'], columns=['samples'], values='data points')
    return pivot_table


def table2sm_q(table_filename):
    """
    Convert a table to a pivoted table with index 'S' and 'M' and column 'Q'
    :param table_filename:
    :return: data frame
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['samples', 'chemical entities'],
                                 columns=['quantitation types'])
    return pivot_table


def table2s_mq(table_filename):
    """
    Convert a table to a pivoted table with index 'S' and columns 'M' and 'Q'
    :param table_filename:
    :return: data frame
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['samples'],
                                 columns=['chemical entities', 'quantitation types'])
    return pivot_table


def table2s_qm(table_filename):
    """
    Convert a table to a pivoted table with index 'S'  and columns 'Q' and 'M'
    :param table_filename:
    :return: data frame
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['samples', ],
                                 columns=['quantitation types', 'chemical entities'])
    return pivot_table



def table2sq_m(table_filename):
    """
    Convert a table to a pivoted table with index 'S' and 'Q' and column 'M'
    :param table_filename:
    :return: data frame
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['samples', 'quantitation types'],
                                 columns=['chemical entities'])
    return pivot_table



