# Explain in detail, with examples, the .replace() method applied to strings 
string = "gato perro loro pez gallo"
print(f"\nOriginal: {string}")
new_string = string.replace("gato", "tortuga")
print(f"Reemplazado: {new_string}")

text = "I like apples and blueberry are tasty."
new_text = text.replace("apples", "mango").replace("tasty", "delicious")
print(new_text)


# Resultados esperados:
#Original: gato perro loro pez gallo
#Reemplazado: tortuga perro loro pez gallo
#I like mango and blueberry are delicious.