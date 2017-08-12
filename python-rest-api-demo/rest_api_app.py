from flask import Flask

from org.mahajan.controllers.controller import CustomerController

app = Flask(__name__)

customer = CustomerController()
app.add_url_rule("/customers","addCustomer",customer.addCustomer,methods=['POST'])
app.add_url_rule("/customers/<int:customerId>","getCustomer",customer.getCustomer,methods=['GET'])


if __name__ == '__main__':
    app.run(debug=False)