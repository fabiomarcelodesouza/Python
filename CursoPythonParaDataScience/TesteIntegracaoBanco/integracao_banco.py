import pyodbc 

try:
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=BRZN6Y9V9R2;"
        "Database=PythonSQL"
    )

    conexao = pyodbc.connect(dados_conexao)
    comando = "select * from teste"

    cursor = conexao.cursor()   
    select = cursor.execute(comando)
    print(select)
    # cursor.commit()
except Exception as e:
    print(e)