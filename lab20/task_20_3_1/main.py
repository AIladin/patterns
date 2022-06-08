from media_player import MediaPlayer


def main():
    player = MediaPlayer()
    player.add_track("track 1")
    player.add_track("track 2")
    player.add_track("track 3")
    player.add_track("track 4")
    player.add_track("track 5")
    player.add_track("track 6")

    player.play()
    player.pause()
    player.play()
    player.prev()
    player.next()
    player.next()
    player.prev()
    player.pause()
    player.next()
    player.play()
    player.stop()


if __name__ == "__main__":
    main()
