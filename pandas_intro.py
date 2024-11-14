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

print("-- data frame")
print(df)

print("-- 'rocket' column")
print(df['rocket'])

print("-- rockets with more than 5 lauches")
print(df[df['launches'] > 5])

# add new column

df['success_rate'] = [.4, .98, 1.0]

print("-- new column")
print(df)