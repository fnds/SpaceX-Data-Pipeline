import pandas as pd

data = {
    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy'
    ],
    'launches': [5, 100, 3]
}

df = pd.DataFrame(data)

print(df)

print(df['rocket'])

df_falcon9 = df[df['rocket'] == 'Falcon 9']

print(df_falcon9)