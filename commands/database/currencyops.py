import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.Certificate("./commands/database/python-database-ef82c-firebase-adminsdk-rud55-5c94416b43.json")
fireapp = firebase_admin.initialize_app(credential)

db = firestore.client()
users_ref = db.collection("users")
settings_ref = db.collection("settings")

users_list = []
for user in users_ref.get():
    users_list.append(user.id)

def create_account(user):
    if user not in users_list:
        users_ref.document(str(user)).set({
            "credit": 0
        })
    else: 
        return "Conta não criada!"
    
def get_user_wealth(user):
    amount = users_ref.document(str(user)).get().to_dict()["credit"]
    return float(amount)

def get_current_wage():
    wage = settings_ref.document("currencydata").get().to_dict()["wage"]
    return float(wage)

def work(user):
    users_ref.document(str(user)).update({
        "credit": get_user_wealth(str(user)) + get_current_wage()
    })
    return get_current_wage()

def transfer_money(user, target_account, amount):
    users_ref.document(user).update({
        "credit": get_user_wealth(user) - float(amount)
    })

    users_ref.document(target_account).update({
        "credit": get_user_wealth(target_account) + float(amount)
    })

def get_inflation():
    current_inflation = settings_ref.document("currencydata").get().to_dict()["inflation"]
    return float(current_inflation)

def inflation(tax):
    if float(tax) != 0:
        settings_ref.document("currencydata").update({
            "inflation": get_inflation() + float(tax),
            "wage": get_current_wage() + get_current_wage()*float(tax) / 100
        })
    elif float(tax) == 0: 
        settings_ref.document("currencydata").update({
            "inflation": float(tax),
            "wage": get_current_wage() - get_current_wage()*get_inflation() / 100
        })