#
# The original code for this example is credited to S. Subramanian,
# from this post on DZone: https://dzone.com/articles/restful-web-services-with-python-flask
#

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)

def converter_valor_string(valor_string):
    # Remove o símbolo de moeda
    valor_string = valor_string.replace("R$", "")

    # Remove os pontos de separação de milhares
    valor_string = valor_string.replace(".", "")

    # Substitui a vírgula decimal pelo ponto decimal
    valor_string = valor_string.replace(",", ".")

    # Converte a string em um float
    valor_float = float(valor_string)

    # Converte o float para inteiro
    valor_inteiro = int(valor_float)

    return valor_inteiro

empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader',
 'salary': 'R$ 5.000,00'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer',
 'salary': 'R$ 5.000,00'
 }
 ]

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':usr})


@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):

    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        if 'name' in request.json : 
            em[0]['name'] = request.json['name']

        if 'title' in request.json:
            em[0]['title'] = request.json['title']

        if 'salary' in request.json :
            em[0]['salary'] = request.json['salary']

    return jsonify(em)


@app.route('/empdb/employee',methods=['POST'])
def createEmp():

    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title'],
    'salary': request.json['salary']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        empDB.remove(em[0])
        return jsonify({'response':'Success'})
    else:
        return jsonify({'response':'Failure'})


@app.route('/empdb/employee/soma',methods=['SOMA'])
def createEmp():

    js = jsonify({'emps':empDB})
    salario = 0
    contador = 0
    for a in js:
        contador = contador + 1
        salario = salaraio + converter_valor_string(a['salary'])
    return salario/contador


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
