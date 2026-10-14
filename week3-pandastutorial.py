# import pandas as pd
# print("hello world")
#
# d = {'one':pd.Series([1,2,3], index=['a', 'b','c']),
# 'two':pd.Series([3,4,5], index=['a', 'b','c'])}
#
# df = pd.DataFrame(d)
# df2 = {'one':pd.Series([100,200,300], index=['x', 'y','z'])}
#
# df2 = pd.DataFrame(df2)
# df_updated = pd.concat([df, df2])
#
# print(df_updated)



# #  RIGHT: pd.concat([df, df2])
# df_updated = pd.concat([df, df2])
#
#
# df.concat(df2,df2)
# print(df)
# # print(df[1:3])

#
# import pandas as pd
#
# # Define first DataFrame
# d = {
#     'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#     'two': pd.Series([3, 4, 5], index=['a', 'b', 'c'])
# }
# df = pd.DataFrame(d)
#
# # Define second DataFrame
# d2 = {
#     'one': pd.Series([100, 200, 300], index=['x', 'y', 'z'])
# }
# df2 = pd.DataFrame(d2)
#
# # FIX 1: Use pd.concat instead of .append()
# df_updated = pd.concat([df, df2])
#
# # FIX 2: Print the updated variable, not the original 'df'
# print(df_updated)


import ssl
# Bypass SSL verification checks globally
ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
import seaborn as sns
df = sns.load_dataset('tips')

print(df.iloc[3,2])
print(df)
# print(df.iloc[10:20])



