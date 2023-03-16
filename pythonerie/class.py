# file = open(filename, "a")
# file.write(sniffed_infos.ip + ";"+ self.mac + ";" + self.epoch_time)

##### On peut simplifier l’écriture des données en utilisant une syntaxe appelée fstring, propre au Python 3 :

# file = open(filename)
# file.write(f"{self.ip};{self.mac};{self.epoch_time}")




# class SniffedPacketInfos:
#     print("one")
#     def __init__(self, ip, mac, epoch_time):
#         self.ip = ip
#         self.mac = mac
#         self.epoch_time = epoch_time

#     def to_csv(self, file):
#         file.write(f"{self.ip};{self.mac};{self.epoch_time}\n")



# file = open("my_file.csv", "a")
# sniffed_packet_infos = SniffedPacketInfos("8.8.8.8", "ab-cd-ef-12-34-56", 151516515)
# sniffed_packet_infos.to_csv(file)
# file.close()




## Possible de construire une classe sur la base d’une classe existante, ce mécanisme s’appelle l’héritage.


###Déclareration d'un héritage, on utilise la syntaxe suivante :
# class DerivedClassName(BaseClassName):


# def __init__(self, <optional parameters>) :
# 	super().__init__(<an other optional set of parameters>)



class SniffedPacketInfos:
    def __init__(self, ip, mac, epoch_time):
        self.ip = ip
        self.mac = mac
        self.epoch_time = epoch_time

    def to_csv(self, file):
        file.write(f"{self.to_csv_string()}\n")

    def to_csv_string(self):
        return f"{self.ip};{self.mac};{self.epoch_time}"


class SniffedHttpPacketInfos(SniffedPacketInfos):
    def __init__(self, ip, mac, epoch_time, type):
        super().__init__(ip, mac, epoch_time)
        self.type = type
    
    def to_csv(self, file):
        file.write(f"{self.to_csv_string()}\n")
    
    def to_csv_string(self):
        return f"{super().to_csv_string()};{self.type}"
    




file = open("my_file.csv", "a")
sniffed_packet_infos = SniffedPacketInfos("8.8.8.8", "ab-cd-ef-12-34-56", 151516515)
sniffed_packet_infos.to_csv(file)
file.close()





