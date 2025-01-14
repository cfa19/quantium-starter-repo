import pandas as pd
import os

data_folder = "C:\Users\cfa\Desktop\asd\quantium-starter-repo\data"

csv_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith(".csv")]

combined_data = pd.DataFrame()
for file in csv_files:
    data = pd.read_csv(file)
    # Filtrar por producto "Pink Morsels"
    data = data[data["product"] == "Pink Morsels"]
    # Calcular ventas totales
    data["sales"] = data["quantity"] * data["price"]
    # Seleccionar las columnas necesarias
    data = data[["sales", "date", "region"]]
    # Añadir al conjunto combinado
    combined_data = pd.concat([combined_data, data], ignore_index=True)


output_file = "formatted_output.csv"
combined_data.to_csv(output_file, index=False)

print(f"Archivo procesado y guardado como {output_file}")
