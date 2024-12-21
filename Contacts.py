import os
from tabulate import tabulate

class Message:
    def __init__(self, Name, LastName, Number, Age):
        self.Name = Name
        self.LastName = LastName
        self.Number = Number
        self.Age = Age

    def __str__(self):
        return f"{self.Name}\t\t{self.LastName}\t\t{self.Number}\t\t{self.Age}"


class Contacts:
    def __init__(self, file_path):
        self.contacts = []

    def add_contact(self, Name, LastName, Number, Age):
        contact = Message(Name, LastName, Number, Age)
        self.contacts.append(contact)
        print("Contacto ingresado exitosamente.")
        self.view_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("\nNo hay contactos en la agenda.\n")
        else:
            headers = ["Nombre", "Apellido", "Número", "Edad"]
            data = [[c.Name, c.LastName, c.Number, c.Age] for c in self.contacts]
            print("\n" + tabulate(data, headers=headers, tablefmt="grid") + "\n")

    def saving_session(self):
        nombre_archivo = "Sesion_De_Contactos_Agregados.txt"
        
        headers = ["Nombre", "Apellido", "Número", "Edad"]
        data = [[c.Name, c.LastName, c.Number, c.Age] for c in self.contacts]

        with open(nombre_archivo, "w", encoding="utf-8") as Sesion_De_Contactos_Agregados:
            Sesion_De_Contactos_Agregados.write("\n" + tabulate(data, headers=headers, tablefmt="grid") + "\n")

    def search_contact(self, Name):
        found = [contact for contact in self.contacts if contact.Name.lower() == Name.lower()]
        if not found:
            print("\nContacto no encontrado.\n")
        else:
            headers = ["Nombre", "Apellido", "Número", "Edad"]
            data = [[c.Name, c.LastName, c.Number, c.Age] for c in found]
            print("\n" + tabulate(data, headers=headers, tablefmt="grid") + "\n")

    def modify_contact(self, Name):
        found = [contact for contact in self.contacts if contact.Name.lower() == Name.lower()]
        if not found:
            print("\nContacto no encontrado.\n")
            return
        contact = found[0]
        try: 

            option_modify = int(input("""
            1. Nombre
            2. Apellido
            3. Teléfono
            4. Edad

            Qué información desea modificar del usuario? (Elija un número): """))

            if option_modify == 1:
                contact.Name = input("Ingrese el nuevo nombre: ")
            elif option_modify == 2:
                contact.LastName = input("Ingrese el nuevo apellido: ")
            elif option_modify == 3:
                contact.Number = input("Ingrese el nuevo teléfono: ")
                while contact.Number > 12:
                    print("")  
            elif option_modify == 4:
                contact.Age = input("Ingrese la nueva edad: ")  
                while contact.Age <= 0:
                    print("ERROR!. Su edad no puede ser menor a cero. Ingrese la edad correcta: ")
            else:
                print("Opción inválida.")
                return
        except (ValueError):
            print("Este valor no es aceptado, por favor ingrese de nuevo")

        print("\nContacto modificado correctamente.\n")
        self.view_contacts()

    def remove_contact(self, Name):
        for index, contact in enumerate(self.contacts):
            if contact.Name.lower() == Name.lower():
                del self.contacts[index]
                print("\nContacto eliminado correctamente.\n")
                self.view_contacts()
                return

        print("\nContacto no encontrado.\n")

file_path = "contacts.txt"
contact_list = Contacts(file_path)

while True:
    try: 
        choice = int(input("""
        1. Agregar contacto
        2. Ver contactos
        3. Buscar contacto
        4. Modificar contacto
        5. Eliminar contacto
        6. Salir

        Elija una opción: """))

        if choice == 1:
            Name = input("Ingrese el nombre: ")
            LastName = input("Ingrese el apellido: ")

            Number = input("Ingrese el número de teléfono (sin guiones): ")
            while not Number.isdigit() or len(Number) != 10:
                Number = input("Su numero no cumple con el formato comun. Ingrese el número de teléfono correcto: ")

            Age = input("Ingrese la edad: ")
            while not Age.isdigit() or int(Age) <= 0:
                Age = input("ERROR!. Su edad no puede ser menor a cero. Ingrese la edad correcta: ")
                
            contact_list.add_contact(Name, LastName, Number, Age)

        elif choice == 2:
            contact_list.view_contacts()

        elif choice == 3:
            Name = input("Ingrese el nombre del contacto a buscar: ")
            contact_list.search_contact(Name)

        elif choice == 4:
            Name = input("Ingrese el nombre del contacto a modificar: ")
            contact_list.modify_contact(Name)

        elif choice == 5:
            Name = input("Ingrese el nombre del contacto a eliminar: ")
            contact_list.remove_contact(Name)

        elif choice == 6:

            print("\nSe guardaran los contactos ingresados\n")
            contact_list.saving_session()
            break

        else:
            print("\nOpción inválida. Por favor, intente nuevamente.\n")
    except(ValueError):
        print("Este valor no es aceptado, por favor ingrese de nuevo")