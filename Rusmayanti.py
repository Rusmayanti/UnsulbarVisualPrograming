class Prajurit:
    def _init_(self, inputNama, inputKuat, inputPangkat):
        self.nama = inputNama
        self.kekuatan = inputKuat
        self.pangkat = inputPangkat

Tentara1 = Prajurit("Sniper",100, "Sersan")
Tentara2 = Prajurit("Infantri",150,"Kopral")

print(Tentara1.pangkat)
