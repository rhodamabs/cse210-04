from game.directing.score import Score
from game.shared.point import Point
import random

COLS = 60
ROWS = 40

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = Score()
   
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)     

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
      
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                
                
                for _ in artifacts:
                    
                    if artifact.get_text() == 'O':  
                        self.score.set_score_minus()
                        aux = f'SCORE: {self.score.get_score()}'
                        
                       
                        banner.set_text(aux)
                       
                        x = random.randint(1, COLS - 1)
                        y = random.randint(1, ROWS - 1)
                        position = Point(x, y)
                        artifactPosition = artifact.set_position(position)
                    elif artifact.get_text() == '*': 
                        self.score.set_score_plus()
                       
                        aux = f'SCORE: {self.score.get_score()}'
                        
                        
                        banner.set_text(aux)
                        
                        x = random.randint(1, COLS - 1)
                        y = random.randint(1, ROWS - 1)
                        position = Point(x, y)
                        artifactPosition = artifact.set_position(position)
                    
                
            position = artifact.move_next(max_x,max_y)
            artifact.set_position(position)
            aux = "SCORE  " + str(self.score.get_score())
            banner.set_text(aux)
            
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()