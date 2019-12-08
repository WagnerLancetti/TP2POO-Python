import ModeloCarro as ModeloCarro

class ControleMenuCarro():
    def __init__(self):
        self.Modelo = ModeloCarro.ModeloMenuCarro()

    def verificacaoCadastro(self,placa,marca,cor,modelo,ano,locadora): # Controle
        verifica = 0
        mensagem = ""
        if (placa == ''):
            mensagem = "*Digite uma Placa"
            verifica = verifica + 1
        if (marca == ''):
            mensagem = mensagem + "\n*Digite uma Marca"
            verifica = verifica + 1
        if (cor == ''):
            mensagem = mensagem + "\n*Digite uma Cor*" 
            verifica = verifica + 1
        if (modelo == ''):
            mensagem = mensagem + "\n*Digite um Modelo*"
            verifica = verifica + 1
        if (ano.get() == ''):
            mensagem = mensagem + "\n*Digite o ano*"
        if (verifica == 0):
            if(self.Modelo.CadastraCarro(marca,placa,cor,modelo,int(ano.get()),locadora)):
                mensagem = "Carro Cadastrado com Sucesso!"
            else:
                mensagem = "Essa placa já existe no sistema."
            return mensagem
        else:
            return mensagem 
    
    def RemoveCarro(self,indice,mensagem,locadora):
        self.Modelo.RemoverCarro(indice,locadora)
        mensagem = "Carro removido com sucesso!"
        return mensagem

    def BuscarCarros(self,opcao,locadora,verifica):
        if (opcao == "Id" or opcao == "Ano"):
            especificidade = self.Modelo.BuscarCarros(locadora,opcao,int(verifica))
        else:
            especificidade = self.Modelo.BuscarCarros(locadora,opcao,verifica)
        if (len(especificidade) == 0):
            return "Nao exisite nenhum carro com essa especificacao."
        else:
            i = 0
            mensagem = ""
            while(i < len(especificidade)):
                mensagem = mensagem + especificidade[i].toString() + "\n"
                i = i + 1
            del (especificidade[:])
        return mensagem
