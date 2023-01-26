from CharacterEnum import Character

class TrainTimer:

    TRAIN_VELOCITY = 8.33333

    @staticmethod
    def parseSeconds(distanceInKm: str) -> float:
        distance = float(distanceInKm.replace(Character.COMMA.value, Character.DOT.value))
        distanceMeters = distance * 1000.0
        return distanceMeters / TrainTimer.TRAIN_VELOCITY