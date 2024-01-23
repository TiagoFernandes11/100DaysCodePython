import smtplib

email = "insira email aqui"
password = "insira senha aqui"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(email, password)
connection.sendmail(from_addr=email, to_addrs="insira o e-mail destino", msg="Subject:Teste de disparo de email"
                                                                                        "\n\nBom dia")

connection.close()
