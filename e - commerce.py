 $("label").removeClass('radio-label-selected');
  $(this).addClass('radio-label-selected');
});

$(".billing-label").click(function(){
  $("label").removeClass('billing-label-selected');
  $(this).addClass('billing-label-selected');
});


  // This identifies your website in the createToken call below
  Stripe.setPublishableKey('{{ stripe_pub }}');

@@ -91,6 +98,37 @@
  cursor: pointer;
}

.billing-label {
  font-size: 22px;
  font-weight: normal;
  padding: 4px 30px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.billing-label input[type=radio] {
  display: none;
}

.billing-label:hover {
  font-size: 22px;
  font-weight: normal;
  background-color: #428bca;
  color: white;
  cursor: pointer;

}

.billing-label-selected {
  font-size: 22px;
  font-weight: normal;
  background-color: #428bca;
  color: white;
  cursor: pointer;
}




@media(min-width: 1200px) {
  .total { 
@@ -162,10 +200,10 @@ <h3>Billing Addresses</h3>
              {% for address in billing_addresses %}

              {% if request.user.userdefaultaddress.billing.id == address.id %} 
                <label class='radio-label radio-label-selected'>
                <label class='billing-label billing-label-selected'>
              <input type='radio' name='billing_address' value='{{ address.id }}' checked='checked'/> {{ address.get_address }} <br/>
              {% else %}
              <label class='radio-label'>
              <label class='billing-label'>
              <input type='radio' name='billing_address' value='{{ address.id }}' /> {{ address.get_address }} <br/>

              {% endif %}
