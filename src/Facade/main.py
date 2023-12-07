# Subsystem components
class MusicPlayer:
    def play_music(self):
        print("Playing music")

    def stop_music(self):
        print("Stopping music")


class VideoPlayer:
    def play_video(self):
        print("Playing video")

    def stop_video(self):
        print("Stopping video")


class Projector:
    def turn_on(self):
        print("Turning on projector")

    def turn_off(self):
        print("Turning off projector")


# Facade
class MultimediaFacade:
    def __init__(self, music_player, video_player, projector):
        self.music_player = music_player
        self.video_player = video_player
        self.projector = projector

    def start_movie(self):
        self.projector.turn_on()
        self.video_player.play_video()
        self.music_player.play_music()

    def stop_movie(self):
        self.music_player.stop_music()
        self.video_player.stop_video()
        self.projector.turn_off()


# Client code
if __name__ == "__main__":
    # Instantiate subsystem components
    music_player = MusicPlayer()
    video_player = VideoPlayer()
    projector = Projector()

    # Instantiate facade with subsystem components
    multimedia_facade = MultimediaFacade(music_player, video_player, projector)

    # Use the facade to start and stop a movie
    print("Starting the movie:")
    multimedia_facade.start_movie()

    print("\nStopping the movie:")
    multimedia_facade.stop_movie()
