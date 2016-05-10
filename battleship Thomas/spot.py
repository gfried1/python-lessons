class Spot(object):
    def __init__(self):
    	self.has_shot=False
    	self.has_boat=False
    def print_spot(self):
        if self.has_boat and self.has_shot:
            return ' [*] '
        elif self.has_boat:
            return ' [B] '
        elif self.has_shot:
            return ' [O] '
        else:
            return ' [ ] '
# if letter.number = board row column put y
