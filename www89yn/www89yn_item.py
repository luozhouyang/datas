class Item:

    def __init__(self, name="", id="", gender="", age="", birth="", constellation="",
                 height="", weight="", size="", degree="", marriage="", occupational="",
                 lives="", origin="", area="", payment="", serve_time="", language="",
                 serve_type="", hobbits="", characteristic="", message=""):
        self.name = name
        self.id = id
        self.gender = gender
        self.age = age
        self.birth = birth
        self.constellation = constellation
        self.height = height
        self.weight = weight
        self.size = size
        self.degree = degree
        self.marriage = marriage
        self.occupational = occupational
        self.lives = lives
        self.origin = origin
        self.area = area
        self.payment = payment
        self.serve_time = serve_time
        self.language = language
        self.serve_type = serve_type
        self.hobbits = hobbits
        self.character = characteristic
        self.message = message

    def __str__(self):
        return "name={},id={},gender={},age={},birth={},constellation={},height={},weight={}," \
               "size={},degree={},marriage={},occupational={},lives={},origin={},area={},payment={}," \
               "serve_time={},language={},serve_type={},hobbits={},characteristic={},message={}" \
            .format(self.name, self.id, self.gender, self.age, self.birth, self.constellation,
                    self.height, self.weight, self.size, self.degree, self.marriage, self.occupational,
                    self.lives, self.origin, self.area, self.payment, self.serve_time, self.language,
                    self.serve_type, self.hobbits, self.character, self.message)
