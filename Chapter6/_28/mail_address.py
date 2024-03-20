import re
import idna

class MailAddress:
    def __init__(self, value: str):
        if not self.is_valid_email(value):
            raise ValueError(f"{value}はメールアドレスの形式ではありません")
        self.value = value

    @staticmethod
    def is_valid_email(email):
        if not email or email.isspace():
            return False

        try:
            # Normalize the domain
            def domain_mapper(match):
                # Use IDNA to convert Unicode domain names
                domain_name = idna.encode(match.group(2)).decode()
                return match.group(1) + domain_name

            email = re.sub(r"(@)(.+)$", domain_mapper, email, 0)

        except (re.error, ValueError):
            return False

        try:
            return re.match(
                r"^(?:(?:(?:\".+?(?<!\\)\"@)|(?:[0-9a-z](?:(?:\.(?!\.))|[-!#$%&'*+/=?^_`{|}~\w])*)(?<=[0-9a-z])@))" +
                r"(?:(?:\[(?:\d{1,3}\.){3}\d{1,3}\])|(?:[0-9a-z][-0-9a-z]*[0-9a-z]*\.)+[a-z0-9][\-a-z0-9]{0,22}[a-z0-9])$",
                email, re.IGNORECASE) is not None
        except re.error:
            return False
        

if __name__ == '__main__':
    # テストケース
    test_emails = [
        "test@example.com",
        "valid.email+alias@gmail.com",
        "not-valid@",
        "plainaddress",
        "@missingusername.com",
        "email@domain.com",
        "firstname.lastname@domain.com",
        "email@domain-one.com",
        "_______@domain.com",
        "email@domain.name",
        "email@domain.co.jp",
        "firstname-lastname@domain.com"
    ]

    for email in test_emails:
        try:
            mail_address = MailAddress(email)
            print(f"Valid: {mail_address.value}")
        except ValueError as e:
            print(f"Invalid: {e}")