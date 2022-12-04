from src.capaDatos.listarDatosMongo import listarRentals, listarBicis
import pytest

@pytest.mark.test_listarRentalsUno
def test_listarRentalsUno():

    listaRentals = [{'_idrental': 'PA01', 'company_name': 'bibike', 'address': {'zip': '07006', 'street': 'joan alcover n7  ', 'country': 'espana', 'town': 'palma'}, 'social_media': {'twitter': '@bibike', 'instagram': '@bibike'}, 'contact': {'num': '678598234', 'email': 'bibike@contact.eu'}, 'promotions': '15% descuento', 'stock': '2', 'img': 'http://imgfz.com/i/2sS6E8d.jpeg', 'icono': 'http://imgfz.com/i/x1Re2Mf.png'}, {'_idrental': 'PA02', 'company_name': 'rentbima', 'address': {'zip': '07005', 'street': 'plaza de espana', 'country': 'espana', 'town': 'palma'}, 'social_media': {'twitter': '@rentbima', 'instagram': '@rentbima'}, 'contact': {'num': '738912213', 'email': 'rentbima@contact.eu'}, 'promotions': 'No', 'stock': '2', 'img': 'http://imgfz.com/i/YlsSQVf.jpeg', 'icono': 'http://imgfz.com/i/pUvx325.png'}, {'_idrental': 'MA01', 'company_name': 'habikemall', 'address': {'zip': '07500', 'street': 'sant joan n2', 'country': 'espana', 'town': 'manacor'}, 'social_media': {'twitter': '@habikemall', 'instagram': '@habikemall'}, 'contact': {'num': '678523945', 'email': 'habikemall@contact.eu'}, 'promotions': '20% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/Iw2GXTb.jpeg', 'icono': 'http://imgfz.com/i/UkQEme7.png'}, {'_idrental': 'MA02', 'company_name': 'rybm', 'address': {'zip': '07500', 'street': 'carrer des sol n10', 'country': 'espana', 'town': 'manacor'}, 'social_media': {'twitter': '@rybm', 'instagram': '@rybm'}, 'contact': {'num': '666554223', 'email': 'rybm@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/duK0xBn.jpeg', 'icono': 'http://imgfz.com/i/eKAiq7R.png'}, {'_idrental': 'AL01', 'company_name': 'bikeandgo', 'address': {'zip': '07400', 'street': 'carrer de la creu n7', 'country': 'espana', 'town': 'alcudia'}, 'social_media': {'twitter': '@bikeandgo', 'instagram': '@bikeandgo'}, 'contact': {'num': '897524645', 'email': 'bikeandgo@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/vWtjfA5.jpeg', 'icono': 'http://imgfz.com/i/kfOGrD5.png'}, {'_idrental': 'AL02', 'company_name': 'speedyrent', 'address': {'zip': '07400', 'street': 'carrer de menorca n3', 'country': 'espana', 'town': 'alcudia'}, 'social_media': {'twitter': '@speedyrent', 'instagram': '@speedyrent'}, 'contact': {'num': '689496982', 'email': 'speedyrent@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/brfKjYW.jpeg', 'icono': 'http://imgfz.com/i/S5up7Iy.png'}, {'_idrental': 'SO01', 'company_name': 'energylegs', 'address': {'zip': '07100', 'street': 'av de asturias n10', 'country': 'espana', 'town': 'soller'}, 'social_media': {'twitter': '@energylegs', 'instagram': '@energylegs'}, 'contact': {'num': '987166998', 'email': 'energylegs@contact.eu'}, 'promotions': '10% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/AZr2KHT.jpeg', 'icono': 'http://imgfz.com/i/8pomsKj.png'}, {'_idrental': 'SO02', 'company_name': 'rentingmanakia', 'address': {'zip': '07100', 'street': 'cami des curat n9', 'country': 'espana', 'town': 'soller'}, 'social_media': {'twitter': '@rentingmanakia', 'instagram': '@rentingmanakia'}, 'contact': {'num': '213245685', 'email': 'rentingmanakia@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/NvZjUzc.jpeg', 'icono': 'http://imgfz.com/i/u3qdkED.png'}, {'_idrental': 'CA01', 'company_name': 'touristbike', 'address': {'zip': '07011', 'street': 'avinguda des capdella n10', 'country': 'espana', 'town': 'calvia'}, 'social_media': {'twitter': '@touristbike', 'instagram': '@touristbike'}, 'contact': {'num': '987987987', 'email': 'touristbike@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/PfOTSMF.jpeg', 'icono': 'http://imgfz.com/i/zPt1Yg6.png'}, {'_idrental': 'CA02', 'company_name': 'rentalride', 'address': {'zip': '07013', 'street': 'carrer serral n5', 'country': 'espana', 'town': 'calvia'}, 'social_media': {'twitter': '@rentalride', 'instagram': '@rybrentalridem'}, 'contact': {'num': '687875483', 'email': 'rentalride@contact.eu'}, 'promotions': '5% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/Rg3dPDb.jpeg', 'icono': 'http://imgfz.com/i/I5K98Hz.png'}]

    assert listarRentals() == listaRentals

@pytest.mark.test_listarBicisUno
def test_listarBicisUno():

    jsonBicis = [{'_idbike': 'PA0101', 'state': 'up', 'type': 'bici de ciudad', 'techinfo': {'groupset': 'kask', 'size': 'x', 'wheels': '29', 'brand': 'cube'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '15', 'where': [{'_idrental': 'PA01', 'company_name': 'bibike', 'address': {'zip': '07006', 'street': 'joan alcover n7  ', 'country': 'espana', 'town': 'palma'}, 'social_media': {'twitter': '@bibike', 'instagram': '@bibike'}, 'contact': {'num': '678598234', 'email': 'bibike@contact.eu'}, 'promotions': '15% descuento', 'stock': '2', 'img': 'http://imgfz.com/i/2sS6E8d.jpeg', 'icono': 'http://imgfz.com/i/x1Re2Mf.png'}], 'img': 'http://imgfz.com/i/0bzEH63.jpeg'}, {'_idbike': 'PA0102', 'state': 'down', 'type': 'bici de ciudad electrica', 'techinfo': {'groupset': 'kask', 'size': 's', 'wheels': '26', 'brand': 'specialized'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '15', 'where': [{'_idrental': 'PA01', 'company_name': 'bibike', 'address': {'zip': '07006', 'street': 'joan alcover n7  ', 'country': 'espana', 'town': 'palma'}, 'social_media': {'twitter': '@bibike', 'instagram': '@bibike'}, 'contact': {'num': '678598234', 'email': 'bibike@contact.eu'}, 'promotions': '15% descuento', 'stock': '2', 'img': 'http://imgfz.com/i/2sS6E8d.jpeg', 'icono': 'http://imgfz.com/i/x1Re2Mf.png'}], 'img': 'http://imgfz.com/i/3WgxtCF.jpeg'}, {'_idbike': 'PA0201', 'state': 'up', 'type': 'e-mtb', 'techinfo': {'groupset': 'specialized', 'size': 'l', 'wheels': '27', 'brand': 'specialized'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '14', 'where': [{'_idrental': 'PA02', 'company_name': 'rentbima', 'address': {'zip': '07005', 'street': 'plaza de espana', 'country': 'espana', 'town': 'palma'}, 'social_media': {'twitter': '@rentbima', 'instagram': '@rentbima'}, 'contact': {'num': '738912213', 'email': 'rentbima@contact.eu'}, 'promotions': 'No', 'stock': '2', 'img': 'http://imgfz.com/i/YlsSQVf.jpeg', 'icono': 'http://imgfz.com/i/pUvx325.png'}], 'img': 'http://imgfz.com/i/uLz1k3I.png'}, {'_idbike': 'PA0202', 'state': 'down', 'type': 'e-mtb', 'techinfo': {'groupset': 'orbea', 'size': 'xl', 'wheels': '29', 'brand': 'specialized'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro', 'sillita de bebe'], 'prize_euros_days': '16', 'where': [{'_idrental': 'PA02', 'company_name': 'rentbima', 'address': {'zip': '07005', 'street': 'plaza de espana', 'country': 'espana', 'town': 'palma'}, 'social_media': {'twitter': '@rentbima', 'instagram': '@rentbima'}, 'contact': {'num': '738912213', 'email': 'rentbima@contact.eu'}, 'promotions': 'No', 'stock': '2', 'img': 'http://imgfz.com/i/YlsSQVf.jpeg', 'icono': 'http://imgfz.com/i/pUvx325.png'}], 'img': 'http://imgfz.com/i/f2OzdrC.jpeg'}, {'_idbike': 'MA0101', 'state': 'up', 'type': 'mtb', 'techinfo': {'groupset': 'kask', 'size': 'm', 'wheels': '26', 'brand': 'specialized'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro', 
    'sillita de bebe'], 'prize_euros_days': '18', 'where': [{'_idrental': 'MA01', 'company_name': 'habikemall', 'address': {'zip': '07500', 'street': 'sant joan n2', 'country': 'espana', 'town': 'manacor'}, 'social_media': {'twitter': '@habikemall', 'instagram': '@habikemall'}, 'contact': {'num': '678523945', 'email': 'habikemall@contact.eu'}, 'promotions': '20% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/Iw2GXTb.jpeg', 'icono': 'http://imgfz.com/i/UkQEme7.png'}], 'img': 'http://imgfz.com/i/ZYmUuQV.jpeg '}, {'_idbike': 'MA0102', 'state': 'down', 'type': 'e-mtb', 'techinfo': {'groupset': 'specialized', 'size': 'm', 'wheels': '26', 'brand': 'giant'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '17', 'where': [{'_idrental': 'MA01', 'company_name': 'habikemall', 'address': {'zip': '07500', 'street': 'sant joan n2', 'country': 'espana', 'town': 'manacor'}, 'social_media': {'twitter': '@habikemall', 'instagram': '@habikemall'}, 'contact': {'num': '678523945', 'email': 'habikemall@contact.eu'}, 'promotions': '20% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/Iw2GXTb.jpeg', 'icono': 'http://imgfz.com/i/UkQEme7.png'}], 'img': 'http://imgfz.com/i/fLM1rap.jpeg'}, {'_idbike': 'MA0201', 'state': 'up', 'type': 'bici de ciudad', 'techinfo': {'groupset': 'kask', 'size': 'l', 'wheels': '29', 'brand': 'cube'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '15', 'where': [{'_idrental': 'MA02', 'company_name': 'rybm', 'address': {'zip': '07500', 'street': 'carrer des sol n10', 'country': 'espana', 'town': 'manacor'}, 'social_media': {'twitter': '@rybm', 'instagram': '@rybm'}, 'contact': {'num': '666554223', 'email': 'rybm@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/duK0xBn.jpeg', 'icono': 'http://imgfz.com/i/eKAiq7R.png'}], 'img': 'http://imgfz.com/i/yspcgEA.jpeg'}, {'_idbike': 'MA0202', 'state': 'down', 'type': 'mtb', 'techinfo': {'groupset': 'orbea', 'size': 'xs', 'wheels': '26', 'brand': 'giant'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado'], 'prize_euros_days': '15', 'where': [{'_idrental': 'MA02', 'company_name': 'rybm', 'address': {'zip': '07500', 'street': 'carrer des sol n10', 'country': 'espana', 'town': 'manacor'}, 'social_media': {'twitter': '@rybm', 'instagram': '@rybm'}, 'contact': {'num': '666554223', 'email': 'rybm@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/duK0xBn.jpeg', 'icono': 'http://imgfz.com/i/eKAiq7R.png'}], 'img': 'http://imgfz.com/i/VSt9ABZ.jpeg'}, {'_idbike': 'AL0101', 'state': 'up', 'type': 'mtb', 'techinfo': {'groupset': 'specialized', 'size': 'l', 'wheels': '26', 'brand': 'giant'}, 'complements': ['casco', 'luz', 'guardabarros', 'candado', 'potenciometro', 'sillita de bebe'], 'prize_euros_days': '14', 'where': [{'_idrental': 'AL01', 'company_name': 'bikeandgo', 'address': {'zip': '07400', 'street': 'carrer de la creu n7', 'country': 'espana', 'town': 'alcudia'}, 'social_media': {'twitter': '@bikeandgo', 'instagram': '@bikeandgo'}, 'contact': {'num': '897524645', 'email': 'bikeandgo@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/vWtjfA5.jpeg', 'icono': 'http://imgfz.com/i/kfOGrD5.png'}], 'img': 'http://imgfz.com/i/oFsXH7a.jpeg'}, {'_idbike': 'AL0102', 'state': 'down', 'type': 'bici de ciudad electrica', 'techinfo': {'groupset': 'kask', 'size': 'xl', 'wheels': '26', 'brand': 'specialized'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro', 'sillita de bebe'], 'prize_euros_days': '16', 'where': [{'_idrental': 'AL01', 'company_name': 'bikeandgo', 'address': {'zip': '07400', 'street': 'carrer de la creu n7', 'country': 'espana', 'town': 'alcudia'}, 'social_media': {'twitter': '@bikeandgo', 'instagram': '@bikeandgo'}, 'contact': {'num': '897524645', 'email': 'bikeandgo@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/vWtjfA5.jpeg', 'icono': 'http://imgfz.com/i/kfOGrD5.png'}], 'img': 'http://imgfz.com/i/ASf5R7d.jpeg'}, {'_idbike': 'AL0201', 'state': 'up', 'type': 'bici de ciudad', 'techinfo': {'groupset': 'kask', 'size': 'l', 'wheels': '26', 'brand': 'cube'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro', 'sillita de bebe'], 'prize_euros_days': '18', 'where': [{'_idrental': 'AL02', 'company_name': 'speedyrent', 'address': {'zip': '07400', 'street': 'carrer de menorca n3', 'country': 'espana', 'town': 'alcudia'}, 'social_media': {'twitter': '@speedyrent', 'instagram': '@speedyrent'}, 'contact': {'num': '689496982', 'email': 'speedyrent@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/brfKjYW.jpeg', 'icono': 'http://imgfz.com/i/S5up7Iy.png'}], 'img': 'http://imgfz.com/i/u1qZJXl.jpeg'}, {'_idbike': 'AL0202', 'state': 'down', 'type': 'mtb', 'techinfo': {'groupset': 'specialized', 'size': 'm', 'wheels': '27', 'brand': 'giant'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'potenciometro'], 'prize_euros_days': 
    '17', 'where': [{'_idrental': 'AL02', 'company_name': 'speedyrent', 'address': {'zip': '07400', 'street': 'carrer de menorca n3', 'country': 'espana', 'town': 'alcudia'}, 'social_media': {'twitter': '@speedyrent', 'instagram': '@speedyrent'}, 'contact': {'num': '689496982', 'email': 'speedyrent@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/brfKjYW.jpeg', 'icono': 'http://imgfz.com/i/S5up7Iy.png'}], 'img': 'http://imgfz.com/i/F9tJs46.jpeg'}, {'_idbike': 'SO0101', 'state': 'up', 'type': 'e-mtb', 'techinfo': {'groupset': 'giro', 'size': '', 'wheels': '26', 'brand': 'cannondale'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '15', 'where': [{'_idrental': 'SO01', 'company_name': 'energylegs', 'address': {'zip': '07100', 'street': 'av de asturias n10', 'country': 'espana', 'town': 'soller'}, 'social_media': {'twitter': '@energylegs', 'instagram': '@energylegs'}, 'contact': {'num': '987166998', 'email': 'energylegs@contact.eu'}, 'promotions': '10% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/AZr2KHT.jpeg', 'icono': 'http://imgfz.com/i/8pomsKj.png'}], 'img': 'http://imgfz.com/i/aoBKA5Z.jpeg'}, {'_idbike': 'SO0102', 'state': 'down', 'type': 'e-mtb', 'techinfo': {'groupset': 'giro', 'size': 'l', 'wheels': '27', 'brand': 'cube'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '15', 'where': [{'_idrental': 'SO01', 'company_name': 'energylegs', 'address': {'zip': '07100', 'street': 'av de asturias n10', 'country': 'espana', 'town': 'soller'}, 'social_media': {'twitter': '@energylegs', 'instagram': '@energylegs'}, 'contact': {'num': '987166998', 'email': 'energylegs@contact.eu'}, 'promotions': '10% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/AZr2KHT.jpeg', 'icono': 'http://imgfz.com/i/8pomsKj.png'}], 'img': 'http://imgfz.com/i/cgK7Uxf.jpeg'}, {'_idbike': 'SO0201', 'state': 'up', 'type': 'mtb', 'techinfo': {'groupset': 'giro', 'size': 'm', 'wheels': '26', 'brand': 'giant'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '14', 'where': [{'_idrental': 'SO02', 'company_name': 'rentingmanakia', 'address': {'zip': '07100', 'street': 'cami des curat n9', 'country': 'espana', 'town': 'soller'}, 'social_media': {'twitter': '@rentingmanakia', 'instagram': '@rentingmanakia'}, 'contact': {'num': '213245685', 'email': 'rentingmanakia@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/NvZjUzc.jpeg', 'icono': 'http://imgfz.com/i/u3qdkED.png'}], 'img': 'http://imgfz.com/i/baoeuFc.jpeg'}, {'_idbike': 'SO0202', 'state': 'down', 'type': 'bici de ciudad', 'techinfo': {'groupset': 'orbea', 'size': 'xl', 'wheels': '27', 'brand': 'specialized'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro', 'sillita de bebe'], 'prize_euros_days': '16', 'where': [{'_idrental': 'SO02', 'company_name': 'rentingmanakia', 'address': {'zip': '07100', 'street': 'cami des curat n9', 'country': 'espana', 'town': 'soller'}, 'social_media': {'twitter': '@rentingmanakia', 'instagram': '@rentingmanakia'}, 'contact': {'num': '213245685', 'email': 'rentingmanakia@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/NvZjUzc.jpeg', 'icono': 'http://imgfz.com/i/u3qdkED.png'}], 'img': 'http://imgfz.com/i/g31AHse.jpeg'}, {'_idbike': 'CA0101', 'state': 'up', 'type': 'bici de ciudad electrica', 'techinfo': {'groupset': 'kona', 'size': 'l', 'wheels': '26', 'brand': 'cube'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro', 'sillita de bebe'], 'prize_euros_days': '18', 'where': [{'_idrental': 'CA01', 'company_name': 'touristbike', 'address': {'zip': '07011', 'street': 'avinguda des capdella n10', 'country': 'espana', 'town': 'calvia'}, 'social_media': {'twitter': '@touristbike', 'instagram': '@touristbike'}, 'contact': {'num': '987987987', 'email': 'touristbike@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/PfOTSMF.jpeg', 'icono': 'http://imgfz.com/i/zPt1Yg6.png'}], 'img': 'http://imgfz.com/i/ZoKTLvs.jpeg'}, {'_idbike': 'CA0102', 'state': 'down', 'type': 'mtb', 'techinfo': {'groupset': 'giro', 'size': 'xs', 'wheels': '26', 'brand': 'giant'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro', 'sillita de bebe'], 'prize_euros_days': '17', 'where': [{'_idrental': 'CA01', 'company_name': 'touristbike', 'address': {'zip': '07011', 'street': 'avinguda des capdella n10', 'country': 'espana', 'town': 'calvia'}, 'social_media': {'twitter': '@touristbike', 'instagram': '@touristbike'}, 'contact': {'num': '987987987', 'email': 'touristbike@contact.eu'}, 'promotions': 'No', 'stock': '1', 'img': 'http://imgfz.com/i/PfOTSMF.jpeg', 'icono': 'http://imgfz.com/i/zPt1Yg6.png'}], 
    'img': 'http://imgfz.com/i/p8eYINZ.jpeg'}, {'_idbike': 'CA0201', 'state': 'up', 'type': 'mtb', 'techinfo': {'groupset': 'specialized', 'size': 'm', 'wheels': '29', 'brand': 'cannondale'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado', 'potenciometro'], 'prize_euros_days': '15', 'where': [{'_idrental': 'CA02', 'company_name': 'rentalride', 'address': {'zip': '07013', 
    'street': 'carrer serral n5', 'country': 'espana', 'town': 'calvia'}, 'social_media': {'twitter': '@rentalride', 'instagram': '@rybrentalridem'}, 'contact': {'num': '687875483', 'email': 'rentalride@contact.eu'}, 'promotions': '5% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/Rg3dPDb.jpeg', 'icono': 'http://imgfz.com/i/I5K98Hz.png'}], 'img': 'http://imgfz.com/i/1VcN9HE.jpeg'}, {'_idbike': 'CA0202', 'state': 'down', 'type': 'bici de carretera', 'techinfo': {'groupset': 'kona', 'size': 'xs', 'wheels': '27', 'brand': 'cube'}, 'complements': ['casco', 'luz', 'bomba', 'guardabarros', 'candado'], 'prize_euros_days': '15', 'where': [{'_idrental': 'CA02', 'company_name': 'rentalride', 'address': {'zip': '07013', 'street': 'carrer serral n5', 'country': 'espana', 'town': 
    'calvia'}, 'social_media': {'twitter': '@rentalride', 'instagram': '@rybrentalridem'}, 'contact': {'num': '687875483', 'email': 'rentalride@contact.eu'}, 'promotions': '5% descuento', 'stock': '1', 'img': 'http://imgfz.com/i/Rg3dPDb.jpeg', 'icono': 'http://imgfz.com/i/I5K98Hz.png'}], 'img': 'http://imgfz.com/i/b4jVFNa.jpeg'}]

    assert listarBicis() == jsonBicis