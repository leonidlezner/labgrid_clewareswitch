import abc


class SwitchProtocol(abc.ABC):
    @abc.abstractmethod
    def on(self, index):
        raise NotImplementedError

    @abc.abstractmethod
    def off(self, index):
        raise NotImplementedError

    @abc.abstractmethod
    def all_on(self):
        raise NotImplementedError

    @abc.abstractmethod
    def all_off(self):
        raise NotImplementedError
