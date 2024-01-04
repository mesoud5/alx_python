class base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
         self.id = id
        else:
           base.__nb_objects += 1
           self.id = base.__nb_objects