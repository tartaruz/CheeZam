class Test:
    def __init__(self):
        self.CBR = None
        self.correct = 0
        self.error = 0
        self.amount = 0

    def setCBR(self, CBR):
        self.CBR = CBR

    def run_test(self):
        pass
    
    def logging(self):
        log_file = open("./log/log.txt", "w")
        log_file.write("dddd")
        pass

    def results(self):
        pass


def main():
    t =  Test()
    t.logging()


if __name__ == '__main__':
    main()
