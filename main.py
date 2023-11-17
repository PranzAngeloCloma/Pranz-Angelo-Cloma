#Pranz Angelo Cloma
#ITCC 14 PRATICAL EXAM

from flask import Flask, jsonify, request

app = Flask(__name__)

games_data = {
    'Dragon Age: Inquisition': {
        'name': 'Dragon Age: Inquisition',
        'release_date': 'November 18, 2014',
        'platforms': ['PlayStation 3', 'PlayStation 4', 'Windows', 'Xbox 360', 'Xbox One'],
        'genres': ['Adventure', 'Role-Playing', 'Strategy'],
        'rating': 4.5,
        'developers': ['BioWare'],
    },
    'The Witcher 3: Wild Hunt': {
        'name': 'The Witcher 3: Wild Hunt',
        'release_date': 'May 18, 2015',
        'platforms': ['PlayStation 5', 'PlayStation 4', 'Nintendo Switch', 'Xbox One', 'Xbox Series X and Series S', 'Windows PC'],
        'genres': ['Open World', 'Role-Playing', 'Action-Adventure'],
        'rating': 4.7,
        'developers': ['CD Projekt RED', 'CD Projekt'],
    },
    'Overwatch': {
        'name': 'Overwatch',
        'release_date': 'May 3, 2016',
        'platforms': ['PlayStation 4', 'Nintendo Switch', 'Xbox One', 'Microsoft Windows'],
        'genres': ['First-person shooter', 'Fighting game'],
        'rating': 3.9,
        'developers': ['Blizzard Entertainment'],
    },
    'The Legend of Zelda: Breath of the Wild': {
        'name': 'The Legend of Zelda: Breath of the Wild',
        'release_date': 'March 3, 2017',
        'platforms': ['Nintendo Switch', 'Wii U'],
        'genres': ['Open world', 'Puzzle', 'Action-adventure'],
        'rating': 4.8,
        'developers': ['Nintendo', 'Nintendo Entertainment Planning & Development'],
    },
    'God of War': {
        'name': 'God of War',
        'release_date': 'April 20, 2018',
        'platforms': ['PlayStation 4', 'Microsoft Windows'],
        'genres': ['Action-adventure', 'Fighting', 'Role-playing'],
        'rating': 4.8,
        'developers': ['Sony Interactive Entertainment', 'Santa Monica Studio'],
    },
    'Sekiro: Shadows Die Twice': {
        'name': 'Sekiro: Shadows Die Twice',
        'release_date': 'February 25, 2022',
        'platforms': ['PlayStation 4', 'Xbox One', 'Microsoft Windows', 'Google Stadia'],
        'genres': ['Action-adventure', 'Fighting', 'Role-playing'],
        'rating': 4.4,
        'developers': ['Activision', 'FromSoftware Inc'],
    },
    'The Last of Us Part II': {
        'name': 'The Last of Us Part II',
        'release_date': 'June 19, 2020',
        'platforms': ['PlayStation 4'],
        'genres': ['Action-adventure', 'Fighting', 'Horror'],
        'rating': 3.0,
        'developers': ['Naughty Dog'],
    },
    'It Takes Two': {
        'name': 'It Takes Two',
        'release_date': 'March 25, 2021',
        'platforms': ['PlayStation 5', 'PlayStation 4', 'Xbox One', 'Microsoft Windows', 'Nintendo Switch'],
        'genres': ['Platform', 'Puzzle', 'Action-Adventure'],
        'rating': 4.8,
        'developers': ['Hazelight Studios'],
    },
    'Elden Ring': {
        'name': 'Elden Ring',
        'release_date': 'February 25, 2022',
        'platforms': ['PlayStation 5', 'PlayStation 4', 'Xbox One', 'Xbox Series X and Series S', 'Microsoft Windows'],
        'genres': ['Action-Adventure', 'Platform', 'Action-Role Playing'],
        'rating': 4.3,
        'developers': ['FromSoftware'],
    }
}

print("Available game names:")
for name in games_data.keys():
    print(name)

@app.route('/game-info', methods=['GET'])
def get_game_info():
    game_name = request.args.get('name')
    print(f"Received game_name: {game_name}")

    if not game_name:
        return jsonify({'error': 'Missing parameter: name'}), 400

    if game_name.lower() in games_data:
        return jsonify({'game_info': games_data[game_name.lower()]})
    else:
        return jsonify({'error': 'Game not found'}), 404

@app.route('/add-game', methods=['POST'])
def add_game():
    data = request.json

    if 'name' not in data or data['name'] in games_data:
        return jsonify({'error': 'Invalid or duplicate game name'}), 400

    games_data[data['name']] = data
    return jsonify({'message': 'Game added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
