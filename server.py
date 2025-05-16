import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_somar(self, a, b):
        return a + b
    
  def exposed_multiplicar(self, a, b):
        return a * b
    
  def exposed_obter_estatisticas(self):
        return {
            "tamanho": len(self.lista),
            "soma": sum(self.lista),
            "media": sum(self.lista) / len(self.lista) if self.lista else 0
        }

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

