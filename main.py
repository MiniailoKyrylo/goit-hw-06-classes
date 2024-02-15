import contacts_manager as c_m

# # Test Name Phone Email
# print(contacts_manager.Name('Jane').value)
# print(contacts_manager.Phone('0991234567').value)
# print(contacts_manager.Email('link@post.com').value)

# # Test Record.__init__ and display_job
# c_m.display_obj(c_m.Record('Jane', phones = ['0991234567',], emails = ['link@post.com']))
# c_m.display_obj(c_m.Record('Jane', id = 12, phones = [], emails = ['link@post.com']))
# c_m.display_obj(c_m.Record('Jane', phones = ['0991234567','0991234567'], emails = []))

# # Test Record add change delete
# user = c_m.Record('Jane', phones = ['0991234567',], emails = ['link@post.com'])
# c_m.display_obj(user)
# user.add_phone('0993333333')
# c_m.display_obj(user)
# user.add_email('link@meta.ua')
# user.add_email('mail@meta.ua')
# c_m.display_obj(user)
# user.change_email('link@meta.ua', 'mail@gmail.com')
# c_m.display_obj(user)
# user.change_phone('0992222222', '0994444444')
# c_m.display_obj(user)
# user.change_name('Max')
# c_m.display_obj(user)

# # Test unpacking
# user_obj = c_m.unpacking_format_str_to_record('13,Jane,0958036905;0738036905,jane@gmail.com;mail@gmail.com')
# c_m.display_obj(user_obj)
# user_str = print(c_m.unpacking_record_to_format_str(user_obj))

# # Test AdreessBook.__init__
# book = c_m.AddressBook()
# for value in book.all_contacts:
#     c_m.display_obj(value)

# # Test AdreessBook add save display find delete
# book = c_m.AddressBook()
# user = c_m.Record('Jane', phones = ['0991234567',], emails = ['link@post.com'])
# book.add_contact(user)
# book.display_contact()
# print(book.find_contact_by_phone_number('+380958036905'))
# book.delete_contact_by_phone_number('0503333333')


# # Test values for addess_book.txt
# 1,Jane,+380501111111,jane@gmail.com,
# 2,Max,+380502222222;+380992222222,max@gmail.com;max@meta.ua,
# 3,Ivan,,,
# 5,Alex,+380503333333,,
# 7,Julia,,julia@meta.ua,