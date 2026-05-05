country = "india"

class ace:
    clg = "ACE Engineering College"

    def give_details(self, a, b, c, d):
        self.tot = a + b + c
        self.name = d

    def display(self):
        print("1. Name:", self.name)
        print("2. Marks:", self.tot)
        print("3. College:", ace.clg)
        print("4. Country:", country)
        print()


class bvrit:
    clg = "BVRIT Engineering College"

    def set_dim(self, a, b, c, d):
        self.tot = a + b + c
        self.name = d

    def display(self):
        print("1. Name:", self.name)
        print("2. Marks:", self.tot)
        print("3. College:", bvrit.clg)
        print("4. Country:", country)
        print()


# objects
a = ace()
b = bvrit()
a2 = ace()
b2 = bvrit()
a.give_details(20, 30, 40, "surya")
b.set_dim(20, 30, 41, "vidyesh")
a2.give_details(50, 60, 70, "Randa pavan")
b2.set_dim(35, 45, 55, "hansh")
a.display()
b.display()
a2.display()
b2.display()