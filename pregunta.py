"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    data = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = data.copy()

    df["sexo"] = df["sexo"].str.lower()
    df["sexo"] = df["sexo"].str.strip()

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.strip()

    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.strip("")
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ", regex=False)
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ", regex=False)
    #df["idea_negocio"] = df["idea_negocio"].str.replace(r'\bde\s+\w+\b', "", regex=True)
    #df["idea_negocio"] = df["idea_negocio"].str.replace(r'\bde\b', "", regex=True)

    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.strip("")
    df["barrio"] = df["barrio"].str.replace("-", " ")
    df["barrio"] = df["barrio"].str.replace("_", " ")

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].str.split('/').map(
            lambda x: "{}/{}/{}".format(x[0], x[1], x[2]) 
            if len(x[0]) <= 2  else "{}/{}/{}".format(x[2], x[1], x[0])
            )

    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.strip()
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)

    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.strip("")
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ")
    
    df = df.drop_duplicates()
    df = df.dropna()

    return df
