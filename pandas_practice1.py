import pandas as pd 
 
#how to make a dataframe from a dictionary in pandas

df = pd.DataFrame(
    {
        "Name": [
            "kshitij", "alice",
            "bob", "charlie"
            ],
        "Age": [20,18,22,24],
        "City":["amd","delhi", "bnglr","mumbai"]

    }
)

print(df)