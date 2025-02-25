import pickle

def save_data(file_path, data): #išsaugo
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def load_data(file_path): #nuskaito
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        save_data(file_path, [])
        return []     
    except EOFError:
        return []
