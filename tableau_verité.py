import pandas as pd

# Creating the truth values for p, q, and r
truth_values = [(p, q, r) for p in [True, False] for q in [True, False] for r in [True, False]]

# Creating the truth table
truth_table = pd.DataFrame(truth_values, columns=['p', 'q', 'r'])
truth_table['p → q'] = truth_table.apply(lambda row: not row['p'] or row['q'], axis=1)
truth_table['¬r'] = ~truth_table['r']
truth_table['(p → q) ∧ ¬r'] = truth_table['p → q'] & truth_table['¬r']
truth_table['¬p'] = ~truth_table['p']

print(truth_table[['p', 'q', 'r', 'p → q', '¬r', '(p → q) ∧ ¬r', '¬p']])

# Updating the truth table for the new expression
truth_table = pd.DataFrame([(p, q) for p in [True, False] for q in [True, False]], columns=['p', 'q'])
truth_table['¬q'] = ~truth_table['q']
truth_table['p ∧ ¬q'] = truth_table['p'] & truth_table['¬q']
truth_table['p ∧ q'] = truth_table['p'] & truth_table['q']
truth_table['(p ∧ ¬q) ⇒ (p ∧ q)'] = truth_table.apply(lambda row: not row['p ∧ ¬q'] or row['p ∧ q'], axis=1)

print(truth_table[['p', 'q', '¬q', 'p ∧ ¬q', 'p ∧ q', '(p ∧ ¬q) ⇒ (p ∧ q)']])
