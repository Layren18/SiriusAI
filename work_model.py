import pickle
import pandas as pd


def predict(data: dict):
    data = [data]
    print(data)
    df = pd.DataFrame.from_dict(data)
    print(df)
    Xtest = df
    with open('pickle_model.pkl', 'rb') as file:
        pickle_model = pickle.load(file)
        Ypredict = pickle_model.predict(Xtest)
        return Ypredict[0]


# if __name__ == "__main__":
#     data = {'full_sq': 0,
#             'life_sq': 0,
#             'floor': 0,
#             'max_floor': 0,
#             'material': 0,
#             'build_year': 0,
#             'num_room': 0,
#             'kitch_sq': 0,
#             'state': 0
#             }
#     print(predict(data))
