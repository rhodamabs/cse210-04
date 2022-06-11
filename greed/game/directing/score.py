class Score:
    """
    Responsible for keeping track of the points in the game
    
    Attributes:
    score(int): The number of points earned by the player

    """

    def __init__(self):
        """
        Creates a new score
        """
        self.myScore = 0
        
       
    def set_score_plus(self):
        """
        Adds a score when player catches a gem
        """
        self.myScore += 1
        
    

    def set_score_minus(self):
        """
        Deducts a score when player catches a rock
        """
        self.myScore -= 1
        

    def get_score(self):
        """Updates the score

        Returns:
            Total score
        """
        return self.myScore