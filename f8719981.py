import numpy as np
import pandas as pd

dados = {
    "REGRA1": ["N", "N", "S", "N"],
    "REGRA2": ["S", "N", "S", "S"],
    "REGRA3": ["N", "N", "S", "N"],
    "REGRA4": ["N", "N", "S", "N"],
    "REGRA5": ["S", "N", "S", "N"],
}

df = pd.DataFrame(dados)

df["REGRAS"] = np.where("SSSSS" == df.apply(lambda x: "".join(x[df.columns[-5:]]), axis=1), "S", "N")

print(df)
