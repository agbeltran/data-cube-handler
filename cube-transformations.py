import pandas as pd

TAB = '\t'

def table2m_sq(table_filename):
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['chemical entities'], columns=['samples', 'quantitation types'])
    return pivot_table

def table2ms_q(table_filename):
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['chemical entities', 'samples'], columns=['quantitation types'])
    return pivot_table

def table2sm_q(table_filename):
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['samples', 'chemical entities'],
                                 columns=['quantitation types'])
    return pivot_table

def table2sq_m(table_filename):
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['samples', 'quantitation types'],
                                 columns=['chemical entities'])
    return pivot_table


def m_sq2sm_q(m_sq_filename):
    df_pivot = pd.read_csv(m_sq_filename, sep=TAB)
    print(df_pivot)

    df = pd.melt(df_pivot, id_vars=['chemical entities'])
    print("------------")
    print(df)



def m_sq2sq_m(m_sq_filename):
    df = pd.read_csv(m_sq_filename, sep=TAB)
    print(df)
    (df.T).to_csv('output.tsv', sep=TAB, index=False)

if __name__ == '__main__':

    pivot_table = table2m_sq("table.tsv")
    pivot_table.to_csv("m_sq_output.tsv", sep=TAB)

    pivot_table = table2ms_q("table.tsv")
    pivot_table.to_csv("ms_q_output.tsv", sep=TAB)

    pivot_table = table2sm_q("table.tsv")
    pivot_table.to_csv("sm_q_output.tsv", sep=TAB)

    pivot_table = table2sq_m("table.tsv")
    pivot_table.to_csv("sq_m_output.tsv", sep=TAB)

    #m_sq2sm_q("m_sq_cube.tsv")
    # m_sq2sq_m("m_sq_cube.tsv")