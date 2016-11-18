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
        else:
            return "Não é possível sacar. A conta foi encerrada."


    def pagarmensalidade(self):
        taxa_cp = 20
        taxa_cc = 12
        if self.status:
            if self.tipoconta == "CP":
                if self.saldo > 0 and self.saldo >= taxa_cp:
                    self.saldo -= taxa_cp
                    return "Você pagou {0} de mensalidade e seu saldo e de {1}.".format(taxa_cp, self.saldo)
                else:
                    print("Seu saldo é de: %d " % self.saldo)
                    return "Desculpa amigão, mas você está sem grana pra pagar a mensalidade!"

            elif self.tipoconta == "CC":
                if self.saldo > 0 and self.saldo >= taxa_cc:
                    self.saldo -= taxa_cc
                    return "Você pagou {0} de mensalidade e seu saldo e de {1}.".format(taxa_cc, self.saldo)
                else:
                    print("Seu saldo é de: %d " % self.saldo)
                    return "Desculpa amigão, mas você está sem grana pra pagar a mensalidade!"
        else:
            return "Sua conta está fechada. Não há mensalidades para serem pagas."
