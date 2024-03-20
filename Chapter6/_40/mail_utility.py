class MailUtility:
    def send(self, message: str):
        print(message)


if __name__ == '__main__':
    mail_utility = MailUtility()
    mail_utility.send('finish to send mail')