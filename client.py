import rpyc
from constRPYC import * #-

class Client:

def __init__(self):
    self.conn = rpyc.connect(SERVER, PORT) # Connect to the server
    print (self.conn.root.exposed_value())ppend two elements
    self.conn.root.exposed_append(5)       # Call an exposed operation,
    self.conn.root.exposed_append(6)       # and a
    print (self.conn.root.exposed_value())  

def executar_operacoes(self):
       
      resultado_soma = self.conn.root.exposed_somar(5, 3)
      print(f"Soma: {resultado_soma}")
        
      resultado_mult = self.conn.root.exposed_multiplicar(4, 2)
      print(f"Multiplicação: {resultado_mult}")
        
      stats = self.conn.root.exposed_obter_estatisticas()
      print(f"Estatísticas: {stats}")
