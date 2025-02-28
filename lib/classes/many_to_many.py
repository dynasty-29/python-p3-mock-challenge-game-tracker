class Game:
    all_games = []
    def __init__(self, title):
        self.title = title
        Game.all_games.append(self)

    # Game property title
    @property
    def title(self):
        return self._title
    
    # Titles must be of type str
    # Titles must be longer than 0 characters
    # Should not be able to change after the game is instantiated
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        if len(value) == 0:
            raise ValueError("Titles must be longer than 0 characters")
        if hasattr(self, '_title'):
            raise AttributeError("Title should not be able to change after the game is instantiated")
        self._title = value
        
    # Returns a list of all results for that game
    # Results must be of type Result        
    def results(self):
        return [result for result in Result.all_results if result.game == self]

    # Returns a unique list of all players that played a particular game
    # Players must be of type Player
    def players(self):
        return list({result.player for result in self.results()})

    # Receives a player object as argument
    # Returns the average of all the player's scores for a particular game instance
    # Reminder: you can calculate the average by adding up all the results' scores of the 
    # player specified and dividing by the number of those results
    def average_score(self, player):
        player_results = [result.score for result in self.results() if result.player == player]
        return sum(player_results)/len(player_results) if player_results else 0

class Player:
    all_players = []
    def __init__(self, username):
        self.username = username
        Player.all_players.append(self)

    # Player property username
    @property
    def username(self):
        return self._username
    
    # Usernames must be of type str
    # Usernames must be between 2 and 16 characters, inclusive.
    # Should be able to change after the player is instantiated
    @username.setter
    def username(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Usernames must be of type str")
        if not 2 <= len(new_name) <= 16:
            raise ValueError("Usernames must be between 2 and 16 characters, inclusive")
        self._username = new_name
        
    # Returns a list of all results for that player
    # Results must be of type Result    
    def results(self):
        return [result for result in Result.all_results if result.player == self]

    # Returns a unique list of all games played by a particular player
    # Games must be of type Game
    def games_played(self):
        return list({result.game for result in self.results()})

    # Receives a game object as argument
    # Returns True if the player has played the game object provided
    # Returns False otherwise
    def played_game(self, game):
        return any(result.game == game for result in self.results())
        # return game in self.games_played()

    # Receives a game object as argument
    # Returns the number of times the player has played the game instance provided
    # Returns 0 if the player never played the game provided
    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)
        # return len([result for result in self.results() if result.game == game])

    # Player classmethod highest_scored(game)
    # Receives a game object as argument
    # Returns the Player instance with the highest average score for the game provided.
    # Returns None if there are no players that played the game provided.
    # hint: will need a way to remember all player objects
    # hint: do you have a method to get the average score on a game for a particular player?
    @classmethod
    def highest_scored(cls, game):
        player_with_scores = [player for player in cls.all_players if player.played_game(game)]
        if not player_with_scores:
            return None
        return max(player_with_scores, key=lambda x: x.average_score(game))
    
class Result:
    all_results = []
    def __init__(self, player, game, score):
        # if not isinstance(player, Player):
        #     raise ValueError("Must be of type Player")
        self._player = player
        # if not isinstance(game, Game):
        #     raise ValueError("Must be of type Game")
        self._game = game
        self.score = score
        Result.all_results.append(self)
        
    # Result property score    
    @property
    def score(self):
        return self._score 
    
    # Scores must be of type int
    # Scores must be between 1 and 5000, inclusive
    # Should not be able to change after the result is instantiated
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Scores must be of type int")
        if not (1 <= value <= 5000):
            raise ValueError("Scores must be between 1 and 5000, inclusive")
        if hasattr(self, '_score'):
            raise AttributeError("Score should not be able to change after the result is instantiated")
        self._score = value
    
    # Result property player
    # Returns the player object for that result
    # Must be of type Player
    @property
    def  player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise ValueError("Must be of type Player")
        self._player = player
       
    # Result property game
    # Returns the game object for that result
    # Must be of type Game 
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise ValueError("Must be of type Game")
        self._game = game