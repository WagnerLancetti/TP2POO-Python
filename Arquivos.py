import Locacao as Locacao
import Carro as Carro

class Arquivos:
    __instancia = None

    @staticmethod
    def instancias():
        if (Arquivos.__instancia == None):
            Arquivos.__instancia = Arquivos()
        return Arquivos.__instancia


    def Leitura_Arquivo(self,locadora):
        entrada = open("Locadora.txt","r")
        VLinha = entrada.readline()
        linhaCars = " "
        linhaAluga = " "
        linhaLoca = " "
        if (VLinha == "Cars\n"):
            for linhaCars in entrada:
                if (linhaCars == "CarsAlugados\n"):
                    break
                else:
                    carros = Carro.Carro()
                    valores = linhaCars.split()
                    carros.identificador = int(valores[0])
                    carros.setMarca(valores[1])
                    carros.setPlaca(valores[2])
                    carros.setCor(valores[3])
                    carros.setModelo(valores[4])
                    carros.setAno(int(valores[5]))
                    if (valores[6] == "False"):
                        carros.setAlugado(False)
                    else:
                        carros.setAlugado(True)
                    locadora.cars.append(carros)

        if (linhaCars == "CarsAlugados\n"):
            for linhaAluga in entrada:
                if (linhaAluga == "Locacoes\n"):
                    break
                else:
                    carros = Carro.Carro()
                    valores = linhaAluga.split()
                    carros.identificador = int(valores[0])
                    carros.setMarca(valores[1])
                    carros.setPlaca(valores[2])
                    carros.setCor(valores[3])
                    carros.setModelo(valores[4])
                    carros.setAno(int(valores[5]))
                    if (valores[6] == "False"):
                        carros.setAlugado(False)
                    else:
                        carros.setAlugado(True)
                    locadora.carsAlugados.append(carros)

        if (linhaAluga == "Locacoes\n"):
            for linhaLoca in entrada:
                tam = 0
                locacao = Locacao.Locacao()
                valores = linhaLoca.split()
                locacao.identificador = int(valores[0])
                locacao.setCliente(valores[1])
                locacao.setData(valores[2])
                tam = int (valores[3])
                i = 0
                k = 4
                while (i < tam):
                    carros = Carro.Carro()
                    carros.identificador = int(valores[k])
                    k = k + 1
                    carros.setMarca(valores[k])
                    k = k + 1
                    carros.setPlaca(valores[k])
                    k = k + 1
                    carros.setCor(valores[k])
                    k = k + 1
                    carros.setModelo(valores[k])
                    k = k + 1
                    carros.setAno(int(valores[k]))
                    k = k + 1
                    if (valores[k] == "False"):
                        carros.setAlugado(False)
                    else:
                        carros.setAlugado(True)
                    k = k + 1
                    i = i + 1
                    locacao.addCarros(carros)
                locadora.locacoes.append(locacao)
        entrada.close()

    def Escrita_Arquivo(self,locadora):
        saida = open ("Locadora.txt","w")
        i = 0
        if (len(locadora.cars) > 0):
            saida.write("Cars\n")
            while (i < len(locadora.cars)):
                saida.write(str(locadora.cars[i].identificador)+" ")
                saida.write(locadora.cars[i].getMarca()+" ")
                saida.write(locadora.cars[i].getPlaca()+" ")
                saida.write(locadora.cars[i].getCor()+" ")
                saida.write(locadora.cars[i].getModelo()+" ")
                saida.write(str(locadora.cars[i].getAno())+" ")
                saida.write(str(locadora.cars[i].isAlugado())+"\n")
                i = i + 1
        if (len(locadora.carsAlugados) > 0):
            saida.write("CarsAlugados\n")
            i = 0
            while (i < len(locadora.carsAlugados)):
                saida.write(str(locadora.carsAlugados[i].identificador)+" ")
                saida.write(locadora.carsAlugados[i].getMarca()+" ")
                saida.write(locadora.carsAlugados[i].getPlaca()+" ")
                saida.write(locadora.carsAlugados[i].getCor()+" ")
                saida.write(locadora.carsAlugados[i].getModelo()+" ")
                saida.write(str(locadora.carsAlugados[i].getAno())+" ")
                saida.write(str(locadora.carsAlugados[i].isAlugado())+"\n")
                i = i + 1
        if (len(locadora.locacoes) > 0):
            saida.write("Locacoes\n")
            i = 0
            while (i < len(locadora.locacoes)):
                saida.write(str(locadora.locacoes[i].identificador)+" ")
                saida.write(locadora.locacoes[i].getCliente()+" ")
                saida.write(locadora.locacoes[i].getData()+" ")
                saida.write(str(locadora.locacoes[i].getTam())+" ")
                j = 0
                while (j < locadora.locacoes[i].getTam()):
                    saida.write(str(locadora.locacoes[i].getCarro(j).identificador)+" ")
                    saida.write(locadora.locacoes[i].getCarro(j).getMarca()+" ")
                    saida.write(locadora.locacoes[i].getCarro(j).getPlaca()+" ")
                    saida.write(locadora.locacoes[i].getCarro(j).getCor()+" ")
                    saida.write(locadora.locacoes[i].getCarro(j).getModelo()+" ")
                    saida.write(str(locadora.locacoes[i].getCarro(j).getAno())+" ")
                    saida.write(str(locadora.locacoes[i].getCarro(j).isAlugado())+" ")
                    j = j + 1
                saida.write("\n")
                i = i + 1
        saida.close()
