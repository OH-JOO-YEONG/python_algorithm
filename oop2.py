class PC:
    processor = "Xeon"
    def set_processor(self, new_processor):
        processor = new_processor


class Desktop(PC):
    os = "Mac OS High Sierra"
    ram = "32"

class Laptop(PC):
    os = "Window"
    ram = "16"

desk = Desktop()
print(desk.processor, desk.os, desk.ram)

desk.processor = "insang"
print(desk.processor, desk.os, desk.ram)

lap = Laptop()
print(lap.processor, lap.os, lap.ram)