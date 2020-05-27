class EmailValidator:
    def __init__(self, min_length, mails=[], domains=[]):
        self.min_length = min_length
        self.__mails = mails
        self.__domains = domains

    def __validate_name(self, username):
        """"
        returns whether the name is greater than or equal to the min_length (True/False)
        """
        return len(username) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.__mails

    def __validate_domain(self, domain):
        return domain in self.__domains

    def __get_email_parts(self, email):
        at_index = email.index("@")
        dot_index = email.rindex(".")

        username = email[:at_index]
        mail = email[at_index + 1: dot_index]
        domain = email[dot_index + 1:]
        return (username, mail, domain)

    def validate(self, email):
        (username, mail, domain) = self.__get_email_parts(email)

        return self.__validate_name(username) and \
            self.__validate_mail(mail) and \
            self.__validate_domain(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
