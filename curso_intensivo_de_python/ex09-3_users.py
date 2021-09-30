# USUÁRIOS
# criando classe ("bloco modelo")
class User:
    def __init__(self, first_name, last_name, age, city, marital_status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.marital_status = marital_status
        self.login_attempts = 1

    def describe_user(self):
        print(f"Name: {self.first_name.title()} {self.last_name.title()}\n"
              f"Age: {self.age}\n"
              f"City: {self.city.title()}\n"
              f"Marital status: {self.marital_status}\n")

    def greet_user(self):
        print(f'"Welcome, {self.first_name.title()}!"\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for n, privilege in enumerate(self.privileges):
            print(f'Privilege nº{n + 1}: {privilege.capitalize()}')


class Admin(User, Privileges):
    # representa os aspectos específicos da classe User
    def __init__(self, first_name, last_name, age, city, marital_status):
        # inicializa os atributos da classe-pai
        super().__init__(first_name, last_name, age, city, marital_status)
        # ///self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()


# 9.3 Usuários
print('#9.3 Usuários')
user_01 = User('alef', 'alencar', 25, 'ibiuna', 'single')
user_02 = User('mak', 'alencar', 22, 'ibiuna', 'married')
user_03 = User('ray', 'ap', 15, 'ibiuna', 'single')
user_04 = User('pri', 'luz', 30, 'piedade', 'married')

user_01.describe_user()
user_01.greet_user()
user_02.describe_user()
user_02.greet_user()
user_03.describe_user()
user_03.greet_user()
user_04.describe_user()
user_04.greet_user()

# 9.5 Tentativas de login
print('#9.5 Tentativas de login')
user_01.increment_login_attempts()
user_01.increment_login_attempts()
print(f"Login attempts: {user_01.login_attempts}")
user_01.reset_login_attempts()
print(f"Login attempts: {user_01.login_attempts}")

# 9.7 Admin
print('\n#9.7 Admin')
# criar uma instância de Admin
admin_00 = Admin('alef', 'camargo', 25, 'ibiuna', 'married')
admin_00.describe_user()
# chame o método show_privileges
admin_00.privileges.show_privileges()  # 9.8, alterado de: admin_00.privileges

# 9.8 Privilégios
print('\n#9.8 Privilégios')
