# -*- coding: utf-8 -*-
addresses = ["www.address_1.com", "www.address_2", "address_3.com", "address_4"]
addresses = [i + ".com" if not i[-4:] == ".com" else i for i in ["http://" + i if i[:4] == "www." else i for i in addresses]]
addresses = [i + ".com" if not i[-4:] == ".com" else i for i in addresses]
print(addresses)
input()