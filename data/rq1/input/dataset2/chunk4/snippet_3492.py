#Source: https://stackoverflow.com/questions/66229529/how-may-i-solve-attributeerror-nonetype-object-has-no-attribute-text-for-th
nodiscount_price = container.find("div",{"class":"discount_block tab_item_discount no_discount"})

if(nodiscount_price != None):
    nodiscount_price = nodiscount_price.text