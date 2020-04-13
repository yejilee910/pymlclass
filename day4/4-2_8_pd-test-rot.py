import pandas as pd
tbl = pd.DataFrame([
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
    ["J", "K", "L"]
])
print(tbl)
print("---")
print(tbl.T)  # Transpose 전치행렬 (행,렬 전환)
