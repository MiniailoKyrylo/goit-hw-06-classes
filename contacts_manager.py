import re

class Field:
    
    ''' Базовый класс для сущностей '''

    # Конструктор
    def __init__(self, value: str) -> None:
        self.value = value

    # Строчное представление
    def __str__(self) -> str:
        return self.value
    
    # Сравнение двух экземпляров одного класса
    def __eq__(self, other: object) -> bool:
        return self.value == other.value if isinstance(other, type(self) ) else False

class Name(Field):
    
    ''' Класс для хранения имени '''
    
    pass

class Phone(Field):

    ''' Класс для хранения номера телефона '''

    # Конструктор
    def __init__(self, value: str) -> None:
        self.validation_phone(value)

    # Валидация номера телефона украинских операторов
    def validation_phone(self, value: str) -> None:
        if bool(re.fullmatch(r'^(?:\+?380|0|80)\d{9}$', value)) or not(value): 
            value = '+38' + re.search(r"\d{10}(?:$)", value).group()
            self.value = value
        else:
           raise ValueError(value, "Неправильний формат номера телефону")
    


class Email(Field):

    ''' Класс для хранения адреса электронной почты '''

    # Конструктор
    def __init__(self, value: str) -> None:
        self.validation_email(value)
        
    # Валидация адреса электронной почты 'name@post.com'
    def validation_email(self, value:str) -> None:
        if bool(re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value)) or not(value):
            self.value = value.casefold()
        else:            
            raise ValueError(value, "Неправильний формат электронной почты")
    
class Record:

    ''' Класс для создания и работы с контактом '''

    # Конструктор
    def __init__(self, name: str, id: int = 0, phones: list = [], emails: list = []) -> None:

        # Переменные для идентификатора и имени контакта
        self.id = id
        self.name = Name(name)

        # Список для хранения номеров телефонов контакта
        self.phones = [] 
        if phones:
            if all(isinstance(phone, Phone) for phone in phones):
                for phone in phones:
                    self.phones.append(phone)
            else:
                for phone in phones:
                    self.phones.append(Phone(phone))

        # Список для хранения адресов єлектронной почты
        self.emails = [] 
        if emails:
            if all(isinstance(email, Email) for email in emails):
                for email in emails:
                    self.emails.append(email)
            else:
                for email in emails:
                    self.emails.append(Email(email))
    
    # Добавление нового номера телефона контактa
    def add_phone(self, phone: str) -> None:
        if Phone(phone):
            self.phones.append(Phone(phone))

    # Добавление нового адреса єлектронной почты контактa
    def add_email(self, email: str) -> None:
        if Email(email):
            self.emails.append(Email(email))
    # Удаляет номер телефона у контакта
    def delete_phone(self, phone):
        if Phone(phone) in self.phones:
            self.phones.remove(Phone(phone))
        else:
            print(f"{phone} не найдено для удаления")

    # Удаляет адрес єлектронной почты у контакта
    def delete_email(self, email):
        
        if Email(email) in self.emails:
            self.emails.remove(Email(email))
        else:
            print(f"{email} не найдено для удаления")
    
    # Заменяет номер телефона контакта на новый
    def change_phone(self, old_phone: str, new_phone: str) -> None:
        if Phone(old_phone) in self.phones:
            index = self.phones.index(Phone(old_phone))
            self.phones[index] = Phone(new_phone)
        else:
            print(f"{old_phone} не найдено для редактирования")
    
    # Заменяет адрес электронной почты контакта на новый
    def change_email(self, old_email: str, new_email: str) -> None:
        if Email(old_email) in self.emails:
            index_change = self.emails.index(Email(old_email))
            self.emails[index_change] = Email(new_email)
        else:
            print(f"{old_email} не найдено для редактирования")
    
    # Заменяет имя контакта на новое
    def change_name(self, value: str) -> None:
        self.name = value

class AddressBook:

    ''' Класс отвечающий за хранение и редактирование адресной книги '''

    # Конструктор
    def __init__(self):
        self.all_contacts = []  # Пустой список для контактов
        self.load_contacts_from_file()  # Вызов метода для загрузки контактов из уже существующей адресной книги
    
    # Загружает список всех контактов из существующей адресной книги и конвертирует значения из строк в объекты классов
    def load_contacts_from_file(self, path: str = 'address_book.txt') -> None: 
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    # Генерируем словарь {идентификатор: Record(имя, [номера телефонов],[адреса електронной почты])}
                    self.all_contacts.append(unpacking_format_str_to_record(line))

        except FileNotFoundError:
            print(f'Файл с адресной книгой не найден')

    # Добавляет новый контакт в адресную книгу и перезаписывает ее
    def add_contact(self, new_contact: Record) -> None:

        id_contacts = [contact.id for contact in self.all_contacts]
        while any(contact_id == new_contact.id for contact_id in id_contacts):
            new_contact.id += 1
             
        self.all_contacts.append(new_contact)
        self.save_contact_changes()
    
    # Ищет среди адресной книги совпадение номеру телефона
    def find_contact_by_phone_number(self, value):
        
        value = Phone(value)
        for contact in self.all_contacts:
            for phone in contact.phones:
                if value == phone:
                    return contact
        
        print(f'По запросу "{value}" в адресной книге совпадений не найдено')
    
    # Удаляет контакт по номеру телефона
    def delete_contact_by_phone_number(self, value):

        find_contact = self.find_contact_by_phone_number(value)
        
        if find_contact:
            self.all_contacts.remove(find_contact)
            self.save_contact_changes()

    # Сохраняет внесенные изменения в адресной книге
    def save_contact_changes(self): 
        try:
            with open('address_book.txt', 'w') as file:
                for contact in self.all_contacts:
                    
                    file.write(unpacking_record_to_format_str(contact) + '\n')
            print("Изменения успешно сохранены")
        except Exception as e:
            print("Ошибка при сохранении файла:", str(e))

    def display_contact(self) -> None:
        for contact in self.all_contacts:
            display_obj(contact)

# Функция выводит на экран значения объекта класса Record
def display_obj(obj: Record) -> None:
    div_strip = '-' * 50
    print(div_strip)
    for attribute_name, attribute_value in vars(obj).items():
        if isinstance(attribute_value, list):
            print(f'{attribute_name.upper()}: ', end='')
            if attribute_value:
                for index, item in enumerate(attribute_value):
                    if index != len(attribute_value) - 1:
                        print(item, end=', ')
                    else:
                        print(item)
            else:
                print()
        else:
            print(f'{attribute_name.upper()}: {attribute_value.__str__()}')    
    print(div_strip)

# Функция распаковывает объект Record в форматированную строку   
def unpacking_record_to_format_str(obj: Record) -> str:

    format_str = ''
    for attribute_name, attribute_value in vars(obj).items():
        if isinstance(attribute_value, list):
            for index, item in enumerate(attribute_value):
                format_str += str(item)
                if index != len(attribute_value) - 1:
                    format_str += ';'
        else:
            format_str += str(attribute_value.__str__())
        format_str += ','

    return format_str

# Функция преобразует форматированную строку в объект Record
def unpacking_format_str_to_record(format_str: str) -> dict:

    contact_data = format_str.strip().split(',')  # Разделяем рядок файла по разделителю
    contact_id = int(contact_data[0])
    contact_name = Name(contact_data[1]) # Преобразуем значение имени в объект и сохраняем
    contact_phones_data = contact_data[2].split(';')  # Разделяем рядок номеров телефонов по разделителю

    # Преобразуем значение номеров телефонов в объекты и сохраняем и сохраняем в список
    contact_phones = [] 
    for contact_phone in contact_phones_data:
        if contact_phone:
            contact_phones.append(Phone(contact_phone))
    
    contact_emails_data = contact_data[3].split(';')  # Разделяем рядок адресов электронной почты по разделителю
    
    # Преобразуем значение адресов электронной почты в объекты и сохраняем в список
    contact_emails = [] 
    for contact_email in contact_emails_data:
        if contact_email:
            contact_emails.append(Email(contact_email)) 
         
    return Record(contact_name, contact_id, contact_phones, contact_emails)