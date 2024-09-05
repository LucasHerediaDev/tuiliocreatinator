import os
from twilio.rest import Client
from datetime import datetime
import schedule
import time

# Configurar suas credenciais do Twilio
account_sid = 'AC7df5f8666413158f67d972c57aa9cb62'
auth_token = '89e4e5fcbe92b3b5e588f29d361de0b2'
twilio_number = 'whatsapp:+14155238886'
destino = 'whatsapp:+5511959025596'

cliente = Client(account_sid, auth_token)

def enviar_mensagem_diaria():
    mensagem = "Olá Adam Agustinks, tudo bem? Sou o Tuilio, assistente do LukaoFacao! Vim lembrá-lo de tomar creatina. Tenha um bom dia!"
    cliente.messages.create(
        to=destino,
        from_=twilio_number,
        body=mensagem
    )
    print(f"Mensagem diária enviada para {destino} em {datetime.now()}")

def enviar_mensagem_sexta():
    mensagem = "É sexta-feira dos cria! Aproveite seu dia!"
    cliente.messages.create(
        to=destino,
        from_=twilio_number,
        body=mensagem
    )
    print(f"Mensagem de sexta-feira enviada para {destino} em {datetime.now()}")

def agendar_mensagens():
    # Agenda o envio da mensagem diária para todos os dias às 10:00
    schedule.every().day.at("19:39").do(enviar_mensagem_diaria)
    # Agenda o envio da mensagem de sexta-feira para toda sexta às 10:00
    schedule.every().friday.at("19:40").do(enviar_mensagem_sexta)

def main():
    agendar_mensagens()  # Chama a função para agendar as mensagens

    print("Agendador iniciado. Aguardando para enviar as mensagens...")

    while True:
        schedule.run_pending()  # Verifica se há tarefas agendadas para serem executadas
        time.sleep(1)  # Aguarda um segundo antes de verificar novamente

if __name__ == "__main__":
    main()