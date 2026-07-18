from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando e-mail: {mensagem}")

class NotificacaoSMS(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class NotificacaoFactory:
    @staticmethod
    def criar(tipo):
        if tipo.lower() == 'email':
            return NotificacaoEmail()
        elif tipo.lower() == 'sms':
            return NotificacaoSMS()
        else:
            raise ValueError(f"Tipo de notificação desconhecido: {tipo}")

def main():
    notificador1 = NotificacaoFactory.criar("email")
    notificador1.enviar("Olá, seja bem-vindo!")
    
    notificador2 = NotificacaoFactory.criar("sms")
    notificador2.enviar("Seu código é 1234")

if __name__ == '__main__':
    main()
