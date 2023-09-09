import re

pattern = r"(?P<domain>[a-zA-Z]+)(?P<symbol>@)(?P<host>[a-zA-Z]+)(?P<extension>[\.a-z]+)"
endings = [".com", ".bg", ".net", ".org"]


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


command = input()
while not command == "End":
    match = re.match(pattern, command)
    if match:
        data = match.groupdict()
        if len(data['domain']) < 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if data['extension'] not in endings:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        print("Email is valid")
    else:
        raise MustContainAtSymbolError("Email must contain @")
    command = input()
