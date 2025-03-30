#!/usr/bin/.venv python3
import tcod
import color
import copy
from engine import Engine
import entity_factories
from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = screen_width
    map_height = screen_height -7

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tile_set = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32,8,tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)
    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine
    )
    engine.update_fov()
    engine.message_log.add_message(
        "Welcome to the The Returner!", color.welcome_text
    )
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tile_set,
        title = "The Returner",
        vsync = True,
    )as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)
            engine.event_handler.handle_events_for(context)

if __name__ == "__main__":
        main()