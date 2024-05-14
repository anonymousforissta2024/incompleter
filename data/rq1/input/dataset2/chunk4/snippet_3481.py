#Source: https://stackoverflow.com/questions/70862542/typeerror-user-object-is-not-iterable
@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)[0]
    if not saved_address.is_fully_filled():
        messages.info(request,f'Please complete shipping address!')
        return redirect('checkout')
    if not request.user.profile.is_fully_filled():
        messages.info(request,f'Please complete profile details!')
        return redirect('profile')
    
    store_id = '$$$$$$$$$$$$$$$'
    API_key= '$$$$$$$$$$$$$$$@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)
    
    
    status_url= request.build_absolute_uri(reverse('complete'))
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
    
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    order_items=order_qs[0].orderitems.all()
    order_item_count=order_qs[0].orderitems.count()
    order_total=order_qs[0].get_totals()
    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Mixed', product_name=order_items, num_of_item=order_item_count, shipping_method='Courier', product_profile='None')
    
    current_user=request.user
    
    mypayment.set_customer_info(name=current_user.profile.full_name, email=current_user, address1=current_user.profile.address_1, address2=current_user.profile.address_1, city=current_user.profile.city, postcode=current_user.profile.zipcode, country=current_user.profile.country, phone=current_user.profile.phone)
    
    mypayment.set_shipping_info(shipping_to=current_user.profile.full_name, address=saved_address.address, city=saved_address.city, postcode=saved_address.zipcode, country=saved_address.country)

    response_data = mypayment.init_payment()
    



    return render(request,'payment/payment.html',context={})