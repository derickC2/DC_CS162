import player
import goblin

def __main__():
    a_player = player.Player()
    a_goblin = goblin.Goblin()

    a_player.inspect_character()

    a_player.attack(a_goblin)
    a_goblin.get_health()
    a_goblin.attack(a_player)


if __name__ == "__main__":
    __main__()