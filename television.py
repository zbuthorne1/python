class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__mute = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


    def power(self):
        self.__status = not self.__status
    """
    Method to turn TV on and off
    """

    def mute(self) -> None:
        if self.__status:
            self.__mute = not self.__mute
    """
    Method to mute and unmute TV
    """

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    """
    Method to go up a channel
    """

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    """
    Method to go down a channel
    """

    def volume_up(self):
        if self.__status:
            if self.__status:
                self.__mute = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME
    """
    Method to turn volume up
    """

    def volume_down(self):
        if self.__status:
            if self.__status:
                self.__mute = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME
    """
    Method to turn volume down 
    """

    def __str__(self):
        if self.__muted:
            return f'Volume = {Television.MIN_VOLUME}
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
     
