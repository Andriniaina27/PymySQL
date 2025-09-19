colonne = ["nom", "prenom"]
params = ("Luca", "Amada")
table = "Touriste"
pk = f"id_{table}"
param = ", ".join([f"{col} = %s" for col in colonne])
values = params + (id,)
query = f"UPDATE {table} SET {param} WHERE {pk} = %s"
print(query)