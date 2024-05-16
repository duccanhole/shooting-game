from enum import Enum
import socket

from encode import encode


class GAME_ACTION(Enum):
    MOVE = 0
    FIRE = 1
    HITTING = 2
    START = 3
    SCORE = 4


MOVE_DATA = [{"player": 0, "x": 20, "y": 20}, {"player": 1, "x": 700, "y": 500}]

BULLET_DATA = [{"player": 0, "x": 0, "y": 0}, {"player": 1, "x": 0, "y": 0}]

SCORE_DATA = [0, 0]


def receiveHandle(conn: socket, data: dict, player: int) -> None:
    action = data.get("action")
    if action == GAME_ACTION.MOVE.value:
        MOVE_DATA[player] = data["data"]
        sendData = encode(
            {
                "action": GAME_ACTION.MOVE.value,
                "data": MOVE_DATA[0] if player == 1 else MOVE_DATA[1],
            }
        )
        conn.sendall(sendData)
    if action == GAME_ACTION.FIRE.value:
        BULLET_DATA[player] = data["data"]
        sendData = encode(
            {
                "action": GAME_ACTION.FIRE.value,
                "data": BULLET_DATA[0] if player == 1 else BULLET_DATA[1],
            }
        )
        conn.sendall(sendData)
    if action == GAME_ACTION.SCORE.value:
        SCORE_DATA = data["data"]
        sendData = encode({"action": GAME_ACTION.SCORE.value, "data": SCORE_DATA})
        conn.sendall(sendData)
