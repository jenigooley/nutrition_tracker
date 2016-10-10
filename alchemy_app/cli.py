import logic_cli


def main():
    """ interface takes user input for login or signup"""

    username = raw_input('Hello. Username: ')
    LOGGED_IN = 1
    WRONG_PASSWORD = 2
    NEW_USER = 3

    while True:
        password = raw_input('Password: ')
        login = logic_cli.verify_login(username, password)
        if login == logic_cli.WRONG_PASSWORD:
            print('Wrong password.')
        else:
            break

    if login == LOGGED_IN:
        logic_cli.access_granted(username)

    # if login == 'WRONG_PASSWORD':
    # print('Wrong Password')

    if login == NEW_USER:
        signup = raw_input('Would you like to sign up? ')
        confirm = logic_cli.confirm_signup(signup)
        if not confirm:
            print('bye')
            return

        username = raw_input('Username: ')
        while True:
            password = raw_input('Password: ')
            verify = raw_input('Verify Password: ')
            if not logic_cli.validate_password(password, verify):
                print ('bad password')
            else:
                break
        while True:
            email = raw_input('Email: ')
            if not logic_cli.validate_email(email):
                print ('bad email')
            else:
                break
        height = raw_input('Height: ')
        weight = raw_input('Weight: ')

        logic_cli.signup_user(username, password, verify, email, height, weight)
    logic_cli.access_granted(username)

if __name__ == '__main__':
    main()
