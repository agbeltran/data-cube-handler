import pandas as pd
import numpy as np

TAB = '\t'


def table2m_sq(table_filename):
    """
    Convert a table to a pivoted table with index 'M' and columns 'S' and 'Q'
    :param table_filename:
    :return:
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, index=['chemical entities'], columns=['samples', 'quantitation types'], values='data points')
    return pivot_table

def m_sq2table(m_sq_filename):
    #df = pd.read_csv(m_sq_filename, sep=TAB, header=None)
    #table = df.set_index(['samples']) #, 'quantitation types'])#.unstack('quantitation types')
    df = pd.read_table(m_sq_filename, index_col=[0,1])
    print(df)
    print("-----")
    print(df.index)


def table2ms_q(table_filename):
    """

    :param table_filename:
    :return:
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['chemical entities', 'samples'], columns=['quantitation types'])
    return pivot_table

def table2sm_q(table_filename):
    """

    :param table_filename:
    :return:
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['samples', 'chemical entities'],
                                 columns=['quantitation types'])
    return pivot_table

def table2sq_m(table_filename):
    """

    :param table_filename:
    :return:
    """
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['samples', 'quantitation types'],
                                 columns=['chemical entities'])
    return pivot_table



def ms_q2table(ms_q_filename):
    """
    Convert an MS_Q pivoted table to an unpivoted table.
    :param ms_q_filename:
    :return:
    """
    df = pd.read_csv(ms_q_filename, sep=TAB)
    print(df)
    #df.set_index(['chemical entities' ,'samples']).unstack('quantitation types').fillna(0)
    #table = df.unstack('quantitation types')
    table = df.set_index(['chemical entities' ,'samples']).unstack('quantitation types')
    print("-------")
    print(table)


def m_qs2table(m_qs_filename):
    df = pd.read_csv(m_qs_filename, sep=TAB, header=None)
    print(df)
    table = df.set_index(['chemical entities']).unstack('quantitation types', 'samples')
    return table


def m_qs2ms_q(m_qs_filename):
    df = pd.read_csv(m_qs_filename, sep=TAB, header=None)

    print("------------")
    #row_idx = pd.MultiIndex.from_tuples(df['chemical entities'])
    print(df)
    print("------------")

    df = df.unstack()
    print(df)



def m_sq2sm_q(m_sq_filename):
    df = pd.read_csv(m_sq_filename, sep=TAB, header=None)
    print(df)
    df.unstack(level=[1,2])
    print("------------")
    print(df)



def m_sq2sq_m(m_sq_filename):
    df = pd.read_csv(m_sq_filename, sep=TAB)
    print(df)
    (df.T).to_csv('output.tsv', sep=TAB, index=False)

def read_pivoted():
    m_sq_filename = "m_sq_cube.tsv"

    df = pd.read_table(m_sq_filename, header=None)

    array1 = df.ix[:0, 1:].values.tolist()[0]
    array2 = df.ix[1:1, 1:].values.tolist()[0]

    arrays = [array1, array2]

    tuples = list(zip(*arrays))

    name1 = df.ix[0:0, 0:0].values.tolist()[0][0]
    name2 = df.ix[1:1, 0:0].values.tolist()[0][0]

    columns = pd.MultiIndex.from_tuples(tuples, names=[name1, name2])

    name3 = df.ix[2:2, 0:0].values.tolist()[0][0]

    array3 = df.ix[3:, 0:0].values.tolist()
    # flatten list
    array3 = [item for sublist in array3 for item in sublist]

    index = pd.Index(array3, name=name3)

    values_subset = df.ix[3:, 1:]
    # values = [tuple( map(lambda x: round(x, 2), t) ) for t in values_subset.values.astype(np.float128)]
    values = [tuple(t) for t in values_subset.values.astype(np.float128)]

    df_pivoted = pd.DataFrame(values, index=index, columns=columns)
    return df_pivoted


if __name__ == '__main__':

    pivot_table = table2m_sq("table.tsv")

    pivot_table.to_csv("m_sq_output.tsv", sep=TAB)

    print("--------  pivot_table")
    print(pivot_table)

    print("----- columns  ")
    print(pivot_table.columns)

    print("----- index  ")
    print(pivot_table.index)

    pivot_table = pivot_table.reset_index()
    print("--------  pivot_table after resetting index")

    print(pivot_table)

    m_sq2table("m_sq_cube.tsv")
    df_pivoted = read_pivoted()
    print(df_pivoted)

    #
    #pivot_table = table2ms_q("table.tsv")
    #pivot_table.to_csv("ms_q_output.tsv", sep=TAB)
    #
    # pivot_table = table2sm_q("table.tsv")
    # pivot_table.to_csv("sm_q_output.tsv", sep=TAB)
    #
    # pivot_table = table2sq_m("table.tsv")
    # pivot_table.to_csv("sq_m_output.tsv", sep=TAB)

    #m_sq2sm_q("m_sq_cube.tsv")
    # m_sq2sq_m("m_sq_cube.tsv")

    #m_qs2ms_q("m_qs_cube.tsv")

    #ms_q2table("ms_q_cube.tsv")

    #table = m_qs2table("m_sq_cube.tsv")
    #table.to_csv('m_qs2table_output.tsv', sep=TAB)
