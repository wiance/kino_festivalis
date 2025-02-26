import pickle

def save_filmData(file_path, data): #išsaugo
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def load_filmData(file_path): #nuskaito
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        save_filmData(file_path, [])
        return []     
    except EOFError:
        return []
    
def save_screeningData(screenings_path, data): #išsaugo
    with open(screenings_path, 'wb') as file:
        pickle.dump(data, file)

def load_screeningData(screenings_path): #nuskaito
    try:
        with open(screenings_path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        save_screeningData(screenings_path, [])
        return []     
    except EOFError:
        return []
