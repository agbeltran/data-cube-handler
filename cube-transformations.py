import pandas as pd

TAB = '\t'

def table2m_sq(table_filename, output_filename):
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['chemical entities'], columns=['samples', 'quantitation types'])
    pivot_table.to_csv(output_filename, sep=TAB)

def table2ms_q(table_filename, output_filename):
    df = pd.read_csv(table_filename, sep=TAB)
    pivot_table = pd.pivot_table(df, values='data points', index=['chemical entities', 'samples'], columns=['quantitation types'])
    print(pivot_table)
    pivot_table.to_csv(output_filename, sep=TAB)


def m_sq2sm_q(m_sq_filename):
    df = pd.read_csv(m_sq_filename, sep=TAB)


def m_sq2sq_m(m_sq_filename):
    df = pd.read_csv(m_sq_filename, sep=TAB)
    print(df)
    (df.T).to_csv('output.tsv', sep=TAB, index=False)

if __name__ == '__main__':
    #m_sq2sm_q("m_sq_cube.tsv")
    #m_sq2sq_m("m_sq_cube.tsv")
    table2m_sq("table.tsv", "m_sq_output.tsv")
    table2ms_q("table.tsv", "ms_q_output.tsv")

