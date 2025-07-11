import pandas as pd
import numpy as np

def extract_mo_yr(df):
    df["date"] = pd.to_datetime(df["date"], format='%Y%m%dT%H%M%S')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df.drop("date", axis=1, inplace=True)

def main():
    path = "src/kc_house_data.csv"
    drop_columns = ["id", "zipcode"]
    skd_vars = ["price", "sqft_living", "sqft_lot", "sqft_above", "sqft_living15", "sqft_lot15"]

    # Cargamos nuestro conjunto de datos
    df = pd.read_csv(path)

    # Removemos columnas id y zipcode
    df_prep = df.drop(drop_columns, axis=1)
    extract_mo_yr(df_prep)

    # Removemos outliers
    df_prep = df_prep[~df_prep['bedrooms'].isin([0, 33])]
    df_prep = df_prep[df_prep['bathrooms']>0]

    # Aplicamos transformación logarítimica
    df_prep[skd_vars] = df_prep[skd_vars].apply(np.log1p)
    df_prep.rename(columns={col: f"log_{col}" for col in skd_vars}, inplace=True)

    # Transformamos sqft_basement y was_renovated a variables binarias
    df_prep["has_basement"] = (df_prep["sqft_basement"]>0).astype(int)
    df_prep['was_renovated'] = (df_prep["yr_renovated"] > 0).astype(int)
    df_prep.drop(["sqft_basement", "yr_renovated"], axis=1, inplace=True)

    # Exportamos nuestro conjunto preprocesado como un archivo CSV
    df_prep.to_csv("src/preprocessed.csv", index=False)

    df_prep.info()

if __name__ == "__main__":
    main()