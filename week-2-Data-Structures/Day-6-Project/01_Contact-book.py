import json

# ── Load existing contacts (or start empty on first run) ──
try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}   # first run — file doesn't exist yet


# ── Save helper (avoids repeating the 2 lines) ──
def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)


while True:
    print("\n==== Contact Book ====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All")
    print("5. Exit")

    choice = input("Enter Choice (1-5): ").strip()

    # ── 1. Add ──
    if choice == "1":
        print("==== New Contact ====")
        name    = input("Enter name: ").lower().strip()
        contact = input("Enter Contact Number: ").strip()
        email   = input("Enter email: ").strip()
        city    = input("Enter city name: ").strip().lower()

        if name in contacts:
            print("❌ Contact already exists!")
        else:
            contacts[name] = {"contact": contact, "email": email, "city": city}
            save_contacts(contacts)              # ← save after add ✅
            print(f"✅ Contact '{name}' added.")

    # ── 2. Search ──
    elif choice == "2":
        print("==== Search Contact ====")
        target = input("Enter name: ").lower().strip()

        if target in contacts:
            info = contacts[target]
            print(f"\n👤 {target.title()}")
            print('─' * 40)
            for field, value in info.items():
                print(f"   {field.capitalize():<10}: {value}")
            print('─' * 40)
        else:
            print(f"❌ No contact named '{target}'.")

    # ── 3. Delete ──
    elif choice == "3":
        name = input("Enter name to delete: ").lower().strip()
        if name in contacts:
            contacts.pop(name, None)
            save_contacts(contacts)              # ← save after delete ✅
            print(f"✅ Contact '{name}' deleted.")
        else:
            print(f"❌ No contact named '{name}'.")

    # ── 4. View all ──
    elif choice == "4":
        if not contacts:
            print("📭 Contact book is empty.")
        else:
            for name, info in contacts.items():
                print(f"\n👤 {name.title()}")
                print('─' * 40)
                for field, value in info.items():
                    print(f"   {field.capitalize():<10}: {value}")
                print('─' * 40)

    # ── 5. Exit ──
    elif choice == "5":
        print("\n\tGood Luck 👋")
        break

    else:
        print("❌ Invalid choice. Enter 1-5.")
