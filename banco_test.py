import unittest
from banco import ContaBanco
from random import randint


class ContaBancoTestCase(unittest.TestCase):
    """ Classe base para todos os casos de testes """
    pass


class ContaBancoTest(ContaBancoTestCase):
    def setUp(self):
        self.conta = ContaBanco(randint(1000, 9999), "Eric Ohtake")

    def test_extrato(self):
        self.conta.abrirconta("CP")
        self.conta.depositar(50)
        self.conta.sacar(20)
        self.conta.pagarmensalidade()
        self.assertEqual(self.conta.statusatual(), "============== FIM DO EXTRATO ===========")


class AbrirContaTest(ContaBancoTest):
    def test_abertura_de_conta_cp(self):
        self.conta.abrirconta("CP")
        self.assertEqual(self.conta.tipoconta, "CP")
        self.assertTrue(self.conta.status)
        self.assertEqual(self.conta.saldo, 150)

    def test_abertura_de_conta_cc(self):
        self.conta.abrirconta("CC")
        self.assertEqual(self.conta.tipoconta, "CC")
        self.assertTrue(self.conta.status)
        self.assertEqual(self.conta.saldo, 50)

class DepositarTest(ContaBancoTest):
    def setUp(self):
        self.conta = ContaBanco(randint(1000, 9999), "Eric Ohtake")
        self.conta.abrirconta("CC")

    def test_depositar_na_conta(self):
        self.conta.depositar(150)
        self.assertEqual(self.conta.saldo, 200)

    def test_depositar_na_conta_com_saldo(self):
        self.conta.depositar(150)
        self.conta.depositar(150)
        self.assertEqual(self.conta.saldo, 350)

    def test_depositar_da_conta_fechada(self):
        self.conta.sacar(50)
        self.conta.fecharconta()
        self.assertEqual(self.conta.depositar(100), "Não é possível depositar. A conta foi encerrada.")


class SacarTest(ContaBancoTest):
    """ Ao abrir a conta, ela comecara com 50"""
    def setUp(self):
        self.conta = ContaBanco(randint(1000, 9999), "Eric Ohtake")
        self.conta.abrirconta("CC")

    def test_sacar_da_conta(self):
        self.assertEqual(self.conta.sacar(50), "Seu saldo é de: %d " % 0)

    def test_sacar_da_conta_com_saldo(self):
        self.conta.depositar(100)
        self.assertEqual(self.conta.sacar(100), "Seu saldo é de: %d " % 50)

    def test_sacar_da_conta_sem_saldo(self):
        self.assertEqual(self.conta.sacar(51), "Desculpa amigão, mas você está sem grana!")

    def test_sacar_da_conta_fechada(self):
        self.conta.sacar(50)
        self.conta.fecharconta()
        self.assertEqual(self.conta.sacar(50), "Não é possível sacar. A conta foi encerrada.")


class FecharContaTest(ContaBancoTest):
    """ Ao abrir a conta, ela comecara com 150"""
    def setUp(self):
        self.conta = ContaBanco(randint(1000, 9999), "Eric Ohtake")
        self.conta.abrirconta("CP")

    def test_fechar_a_conta(self):
        self.conta.sacar(150)
        self.assertEqual(self.conta.fecharconta(), "A conta foi fechada. Volte sempre!")

    def test_fechar_a_conta_com_saldo(self):
        self.assertEqual(self.conta.fecharconta(), "A conta ainda tem saldo de %d. Não é possível fechar." % 150)

    def test_fechar_a_conta_com_debito(self):
        self.conta.saldo = -1
        self.assertEqual(self.conta.fecharconta(), "A conta possui débito. Não é possível fechar.")


class PagarMensalidadeTest(ContaBancoTest):
    def setUp(self):
        self.conta = ContaBanco(randint(1000, 9999), "Eric Ohtake")

    def test_paga_mensalidade_conta_cp(self):
        self.conta.abrirconta("CP")
        self.assertEqual(self.conta.pagarmensalidade(), "Você pagou {0} de mensalidade e seu saldo e de {1}.".format(20, 130))

    def test_paga_mensalidade_conta_cc(self):
        self.conta.abrirconta("CC")
        self.assertEqual(self.conta.pagarmensalidade(),
                         "Você pagou {0} de mensalidade e seu saldo e de {1}.".format(12, 38))

    def test_paga_mensalidade_conta_cc_sem_saldo(self):
        self.conta.abrirconta("CC")
        self.conta.sacar(40)
        self.assertEqual(self.conta.pagarmensalidade(),
                         "Desculpa amigão, mas você está sem grana pra pagar a mensalidade!")

    def test_paga_mensalidade_conta_cp_sem_saldo(self):
        self.conta.abrirconta("CP")
        self.conta.sacar(131)
        self.assertEqual(self.conta.pagarmensalidade(),
                         "Desculpa amigão, mas você está sem grana pra pagar a mensalidade!")

    def test_paga_mensalidade_conta_fechada(self):
        self.conta.abrirconta("CC")
        self.conta.sacar(50)
        self.conta.fecharconta()
        self.assertEqual(self.conta.pagarmensalidade(),
                         "Sua conta está fechada. Não há mensalidades para serem pagas.")


if __name__ == '__main__':
    unittest.main()





















