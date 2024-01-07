import pandas as pd

# Creating the truth values for p, q, and r
truth_values = [(p, q, r) for p in [True, False] for q in [True, False] for r in [True, False]]

# Creating the truth table
truth_table = pd.DataFrame(truth_values, columns=['p', 'q', 'r'])
truth_table['p → q'] = truth_table.apply(lambda row: not row['p'] or row['q'], axis=1)
truth_table['¬r'] = ~truth_table['r']
truth_table['(p → q) ∧ ¬r'] = truth_table['p → q'] & truth_table['¬r']
truth_table['¬p'] = ~truth_table['p']

truth_table[['p', 'q', 'r', 'p → q', '¬r', '(p → q) ∧ ¬r', '¬p']]
