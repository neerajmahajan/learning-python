from flask import Flask

from org.mahajan.controllers.controller import CustomerController


app = Flask(__name__)

customer = CustomerController()
app.add_url_rule("/customers/","customer",customer.test,methods=['GET'])
app.add_url_rule("/customers/<string:name>","customer2",customer.test2,methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)