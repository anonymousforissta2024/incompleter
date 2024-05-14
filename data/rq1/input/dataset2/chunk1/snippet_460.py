#Source: https://stackoverflow.com/questions/72198110/typeerror-cannot-pickle-thread-lock-object-while-using-pool-map-over-a-metho
def return_brands_of_product(self,product):
        if product['_source']['brand_id'] != "" and product['_source']['brand_id'] not in self.brands_ids:
            self.brands.append({"brand_id":product['_source']['brand_id'],"name":product['_source']['brand'][0]['name']
                                ,"en_name":product['_source']['brand'][0]['en_name']})
            self.brands_ids.append(product['_source']['brand_id'])

instance = GenerateBrandsFromCategories(cat['_id'])
products = instance.return_products_by_cat_id()
pool.map(instance.return_brands_of_product, products)