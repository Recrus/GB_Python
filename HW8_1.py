def add_contact(phonebook):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'patronymic': patronymic,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print("Запись добавлена.")


def search_contacts(phonebook):
    search_key = input("Введите фамилию, имя или номер телефона: ")
    found_contacts = []
    for contact in phonebook:
        if (
            search_key.lower() in contact['last_name'].lower() or
            search_key.lower() in contact['first_name'].lower() or
            search_key in contact['phone_number']
        ):
            found_contacts.append(contact)
    if found_contacts:
        print("Результаты поиска:")
        for contact in found_contacts:
            print_contact(contact)
    else:
        print("Записи не найдены.")


def print_contact(contact):
    print("Фамилия:", contact['last_name'])
    print("Имя:", contact['first_name'])
    print("Отчество:", contact['patronymic'])
    print("Номер телефона:", contact['phone_number'])
    print()


def export_contacts(phonebook):
    file_name = input("Введите имя файла для экспорта (без расширения .txt): ")
    with open(file_name + ".txt", 'w') as file:
        for contact in phonebook:
            file.write(f"Фамилия: {contact['last_name']}\n")
            file.write(f"Имя: {contact['first_name']}\n")
            file.write(f"Отчество: {contact['patronymic']}\n")
            file.write(f"Номер телефона: {contact['phone_number']}\n")
            file.write("\n")
    print("Данные экспортированы в файл.")


def import_contacts(phonebook):
    file_name = input("Введите имя файла для импорта (с расширением .txt): ")
    try:
        with open(file_name, 'r') as file:
            contact_data = file.read().split('\n\n')
            for data in contact_data:
                if data:
                    contact_lines = data.strip().split('\n')
                    contact = {}
                    for line in contact_lines:
                        key, value = line.split(': ')
                        contact[key.strip()] = value.strip()
                    phonebook.append(contact)
        print("Данные импортированы из файла.")
    except FileNotFoundError:
        print("Файл не найден.")


def print_menu():
    print("Телефонный справочник")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Экспорт контактов в файл")
    print("4. Импорт контактов из файла")
    print("5. Выйти")


def main():
    phonebook = []
    while True:
        print_menu()
        choice = input("Введите номер операции: ")
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contacts(phonebook)
        elif choice == '3':
            export_contacts(phonebook)
        elif choice == '4':
            import_contacts(phonebook)
        elif choice == '5':
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер операции из списка.")


if __name__ == '__main__':
    main()
