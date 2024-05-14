#Source: https://stackoverflow.com/questions/75237185/typeerror-init-missing-1-required-argument-id-name
class Cart(CartTemplate):
  def __init__(self, items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.order = []
    self.items_1 = items
    self.items_2 = items
    self.items_3 = items

  
    if not self.items_1: 
      self.empty_cart_panel.visible = True
      self.column_panel_1.visible = False
    
    self.repeating_panel_1.items = self.items_1
    self.repeating_panel_2.items = self.items_2
    self.repeating_panel_3.items = self.items_3
    
    
    self.subtotal_1 = sum(dairy['price'] * item['quantity'] for item in self.items_1)
    
    self.subtotal_2 = sum(fruit['price'] * item['quantity'] for item in self.items_2)
    
    self.subtotal_3 = sum(vegetable['price'] * item['quantity'] for item in self.items_3)
    
    self.subtotal = self.subtotal_1 + self.subtotal_2 + self.subtotal_3
    self.subtotal_label.text = f"AED {self.subtotal:.02f}"
    
    if self.subtotal >= 40: #free shipping for orders over AED 40
      self.shipping_label.text = 'FREE'     
    else: #add $5 shipping
      self.shipping_label.text = "$5.00"
      self.subtotal = self.subtotal + 5
      
    self.total_label.text = f"${self.subtotal:.02f}"
      

  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().title_link_click()

  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked"""  
    for i in self.items:
      self.order.append({'name':dairy['name'], 'quantity':i['quantity']})
      self.order.append({'name':fruit['name'], 'quantity':i['quantity']})
      self.order.append({'name':vegetable['name'], 'quantity':i['quantity']})
    try:
      charge = stripe.checkout.charge(amount=self.subtotal*100,
                                      currency="AED",
                                      shipping_address=True,
                                      title="Fresh Fields")
    except:
      return
    
    anvil.server.call('charge_user', token, user["email"])

    get_open_form().cart_items = []
    get_open_form().cart_link_click()
    Notification("Your order has been received!").show()