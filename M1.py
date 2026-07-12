import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def prepare_country_stats(oecd_bli, gdp_per_capita):
    # Keep total inequality rows only
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]

    # Convert indicators into columns
    oecd_bli = oecd_bli.pivot(
        index="Country",
        columns="Indicator",
        values="Value"
    )

    # Rename GDP column
    gdp_per_capita.rename(
        columns={"2015": "GDP per capita"},
        inplace=True
    )

    # Use country names as index
    gdp_per_capita.set_index("Country", inplace=True)

    # Merge datasets
    full_country_stats = pd.merge(
        left=oecd_bli,
        right=gdp_per_capita,
        left_index=True,
        right_index=True
    )

    # Sort by GDP
    full_country_stats.sort_values(
        by="GDP per capita",
        inplace=True
    )

    # Return only needed columns
    return full_country_stats[
        ["GDP per capita", "Life satisfaction"]
    ]


# =========================
# LOAD THE DATA
# =========================

oecd_bli = pd.read_csv(
    "oecd_bli_2015.csv",
    thousands=","
)

gdp_per_capita = pd.read_csv(
    "gdp_per_capita.csv",
    thousands=",",
    delimiter="\t",
    encoding="latin1",
    na_values="n/a"
)

# =========================
# PREPARE DATA
# =========================

country_stats = prepare_country_stats(
    oecd_bli,
    gdp_per_capita
)

X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

# =========================
# VISUALIZE DATA
# =========================

country_stats.plot(
    kind="scatter",
    x="GDP per capita",
    y="Life satisfaction"
)

plt.show()

# =========================
# TRAIN MODEL
# =========================

model = LinearRegression()

model.fit(X, y)

# =========================
# PREDICT CYPRUS
# =========================

X_new = [[22587]]

prediction = model.predict(X_new)

print("Predicted Life Satisfaction:")
print(prediction)