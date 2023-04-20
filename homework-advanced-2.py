import re
import csv
class ContactFormatter:
    
    def __init__(self,contacts):
        self.contacts = contacts
    
    def get_names_formatted(self):
        for person in self.contacts:
            if len(person[0].split()) == 3:
                surname = person[0].split()
                person[0], person[1], person[2] = person[0].split()[0], surname[1], surname[2]
            if len(person[1].split()) == 2:
                name = person[1].split()
                person[1], person[2] = name[0], name[1]
            if len(person[0].split()) == 2:
                surname = person[0].split()
                person[0], person[1] = person[0].split()[0], surname[1]

        return contacts


    def get_phone_numbers_formatted(self):
        '''Приводим номера телефонов к единому формату.'''
        pattern = r"(\+7|8)?\s?\(?(\d{3}?)\)?[-\s]?(\d{3})[-\s]?(\d{2})-?(\d{2})(\s?)\(?([доб.]{4})?\s?(\d{4})?\)?"
        subst = r"+7(\2)\3-\4-\5\6\7\8"
        for person in self.get_names_formatted():
            person[5] = re.sub(pattern, subst, person[5])

        return contacts


    def join_and_remove_dubles(self):
        '''Объединяем дублирующиеся записи о человеке.'''
        for person in self.get_phone_numbers_formatted():
            for next_person in self.get_phone_numbers_formatted():
                if person[0] in next_person[0]:
                    for i in range(7):
                        if person[i] == '':
                            person[i] = next_person[i]
        formatted_contacts_list = []
        for person in contacts:
            if len(person) != 7:
                del person[7:]
            if person not in formatted_contacts_list:
                formatted_contacts_list.append(person)

        return formatted_contacts_list


if __name__ == "__main__":
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts = list(rows)
    Contacter = ContactFormatter(contacts)
    Contacter.get_names_formatted()
    Contacter.get_phone_numbers_formatted()
    formatted_contacts_list = Contacter.join_and_remove_dubles()

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(formatted_contacts_list)