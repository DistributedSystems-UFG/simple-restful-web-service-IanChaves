import requests
import const

def serviceTester():
    api_base_url = 'http://' + const.IP_ADD + ':' + str(const.PORT) + '/empdb/employee'
    # Test get_all_employees endpoint
    #api_url = api_base_url 
    #response = requests.get(api_url)
   # print ("\n", response.json(), "\n")

    # Test get_an_employee endpoint
    #api_url = api_base_url + '/201'
    #response = requests.get(api_url)
    #print (response.json(), "\n")

    # Test update_employee endpoint
    api_url = api_base_url + '/201'
    update = {"salary":"R$ 1.500,00"}
    response = requests.put(api_url, json=update)
    print (response.json())

    # Test create_employee endpoint
    #api_url = api_base_url
    #employee = {"id":"501", "name":"Giuli Marcucci", "title":"Gestor da Informação", "salary": "R$ 2.000"}
    #response = requests.post(api_url, json=employee)
    #print (response.json(), "\n")

    # Test delete_employee endpoint
    #api_url = api_base_url + '/101'
    #response = requests.delete(api_url)
    #print (response.json(), "\n")

if __name__ == '__main__':
    serviceTester()
