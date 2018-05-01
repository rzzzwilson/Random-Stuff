df_train = {'SibSp': 1, 'Parch': 2}
df_train["Is_alone1"] = df_train["SibSp"].map(lambda x:1 if x == 0 else 0)
df_train["Is_alone2"] = df_train["Parch"].map(lambda x:1 if x == 0 else 0)
Is_alone=[]
def is_alone():
    for x, y in list(df_train["Is_alone1"]),list(df_train["Is_alone2"]):
        if x == 1 and y == 1:
            Is_alone.append(int(1))
        else:
            Is_alone.append(int(0))
print('Is_alone=%s' % str(Is_alone))
is_alone()
print('Is_alone=%s' % str(Is_alone))
