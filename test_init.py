from lab1 import createBD
from lab1 import fillBD
from lab1 import showClientsBD
from lab1 import showOrdersBD
import modelsLab1
import lab1

def test_createBD_true():
    assert createBD() == True

def test_fillClients_true():
    assert modelsLab1.Client.Name == True
    assert modelsLab1.Client.City == True
    assert modelsLab1.Client.Address == True

def test_fillOrders_true():
    assert modelsLab1.Order.Client_id == True
    assert modelsLab1.Order.Amount ==True
    assert modelsLab1.Order.Date == True
    assert modelsLab1.Order.Description == True
def test_countClients():
    lab1.fillBD()
    assert showClientsBD() >= 10

def test_countOrders():
    assert showOrdersBD() >= 10
