from random import randint


class ContaBanco(object):
    tipoconta = ""
    status = bool
    saldo = 0

    def __init__(self, numconta, dono):
        self.numconta = numconta
        self.dono = dono

    def __repr__(self):
        return "Dono da conta: %s" \
               " Tipo de conta: %s" \
               " Conta aberta: %s" \
               " Saldo: %s" % (self.dono, self.tipoconta, self.status, self.saldo)

    def statusatual(self):
        print("============= INICIO DO EXTRATO =========")
        print("Número da conta: %d" % self.numconta)
        print("Titular da conta: %s" % self.dono)
        print("Tipo de conta: %s" % self.tipoconta)
        print("Saldo da conta: %d" % self.saldo)
        print("Status da conta: %s" % self.status)
        return "============== FIM DO EXTRATO ==========="

    def abrirconta(self, tipo):
        self.tipoconta = tipo
        self.status = True
        if tipo == "CC":
            self.saldo = 50
        elif tipo == "CP":
            self.saldo = 150

    def fecharconta(self):
        if self.saldo > 0:
            return "A conta ainda tem saldo de %d. Não é possível fechar." % self.saldo
        elif self.saldo < 0:
            return "A conta possui débito. Não é possível fechar."
        else:
            self.status = False
            return "A conta foi fechada. Volte sempre!"

    def depositar(self, valor):
        if self.status:
            self.saldo += valor
            return "Você depositou: %s" % valor
        else:
            return "Não é possível depositar. A conta foi encerrada."

    def sacar(self, valor):
        if self.status:
            if self.saldo > 0 and self.saldo >= valor:
                self.saldo -= valor
                print("Você sacou: %d " % valor)
                return "Seu saldo é de: %d " % self.saldo
            else:
                print("Seu saldo é de: %d " % self.saldo)
                return "Desculpa amigão, mas você está sem grana!"

    def pagarmensalidade(self):
        CP = 20
        CC = 12
        if self.status:
            if self.tipoconta == "CP":
                if self.saldo > 0 and self.saldo >= CP:
                    self.saldo -= CC
                    print("Você pagou %d de mensalidade. " % CP)
                    return "Seu saldo é de: %d " % self.saldo
                else:
                    print("Seu saldo é de: %d " % self.saldo)
                    return "Desculpa amigão, mas você está sem grana pra pagar a mensalidade!"

            elif self.tipoconta == "CC":
                if self.saldo > 0 and self.saldo >= CC:
                    self.saldo -= CC
                    print("Você pagou %d de mensalidade. " % CC)
                    return "Seu saldo é de: %d " % self.saldo
                else:
                    print("Seu saldo é de: %d " % self.saldo)
                    return "Desculpa amigão, mas você está sem grana pra pagar a mensalidade!"
        else:
            return "Sua conta está fechada. Não há mensalidades para serem pagas."

acc_num = randint(1000, 9999)

eric_cc = ContaBanco(acc_num, "Eric Ohtake")

eric_cc.abrirconta("CC")

print("A conta está aberta: %s" % eric_cc.status)
print("Cliente: %s" % eric_cc.dono)
print("Número da conta: %s" % eric_cc.numconta)
print("Tipo de conta: %s" % eric_cc.tipoconta)
print("Saldo: %s" % eric_cc.saldo)
print(eric_cc.fecharconta())
print("A conta está aberta: %s" % eric_cc.status)
print(eric_cc.depositar(1500))
print("Saldo: %s" % eric_cc.saldo)
#print(eric_cc.sacar(2000))
print(eric_cc.sacar(100))
print(eric_cc.fecharconta())
print(eric_cc.pagarmensalidade())

print(eric_cc.statusatual())

print(eric_cc) # IMPRIME O METODO __REPR__
