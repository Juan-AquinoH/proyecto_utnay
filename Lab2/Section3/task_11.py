# Explain in detail, with examples, the .replace() method applied to strings 
string = "gato perro loro pez gallo"
print(f"\nOriginal: {string}")
new_string = string.replace("gato", "tortuga")
print(f"Reemplazado: {new_string}")

text = "I like apples and blueberry are tasty."
new_text = text.repl("apples", "mango").replace("tasty", "delicious")
print(new_text)

no se escribe bien replace  por repl  y el error es el siguiente:
    
    Traceback (most recent call last):
  File "c:\Users\Lenovo\Desktop\proyecto_utnay\Lab2\task_11.py", line 8, in <module>
    new_text = text.repl("apples", "mango").replace("tasty", "delicious")
               ^^^^^^^^^
AttributeError: 'str' object has no attribute 'repl'