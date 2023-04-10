import requests
import json
import telegram_send
import time
def get_data():
    while True:

        cookies = {
                    'PHPSESSID': 'b44cba640cd4b13b6c7237e8a063f797',
                    '__utma': '66441069.875942648.1664559390.1664559390.1664559390.1',
                    '__utmb': '66441069.4.10.1664559390',
                    '__utmc': '66441069',
                    '__utmz': '66441069.1664559390.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
                    '__utmt': '1',
                    'extreme_open': 'false',
                    'cto_bundle': 'DS5ZQF82TUpIMGZXNWh5VWJoeE9aR1p1ZlFjd1NDSmF6QWtoWFFtNlhucDJGR0h2YXZONWpxUlIzelpza0xYRkklMkZBOFh3RkluWTRheTFocElNY1BkcEtBVFRZWSUyRmoxdU5RS05WQWdXQ0VGN09yenN0WWFRS2RuWWxHdEZoeGRUQkt1R3A',
                    'i': '4429%7C4429%7C2525',
                    'iru': '4429%7C4429%7C2525',
                    'ru': '%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%7C%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%7C%D0%93%D0%B5%D0%BB%D0%B5%D0%BD%D0%B4%D0%B6%D0%B8%D0%BA',
                    'last_visited_page': 'http%3A%2F%2Frp5.ru%2F%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%93%D0%B5%D0%BB%D0%B5%D0%BD%D0%B4%D0%B6%D0%B8%D0%BA%D0%B5',
                    'lang': 'ru',
                }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'PHPSESSID=b44cba640cd4b13b6c7237e8a063f797; __utma=66441069.875942648.1664559390.1664559390.1664559390.1; __utmb=66441069.4.10.1664559390; __utmc=66441069; __utmz=66441069.1664559390.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; extreme_open=false; cto_bundle=DS5ZQF82TUpIMGZXNWh5VWJoeE9aR1p1ZlFjd1NDSmF6QWtoWFFtNlhucDJGR0h2YXZONWpxUlIzelpza0xYRkklMkZBOFh3RkluWTRheTFocElNY1BkcEtBVFRZWSUyRmoxdU5RS05WQWdXQ0VGN09yenN0WWFRS2RuWWxHdEZoeGRUQkt1R3A; i=4429%7C4429%7C2525; iru=4429%7C4429%7C2525; ru=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%7C%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%7C%D0%93%D0%B5%D0%BB%D0%B5%D0%BD%D0%B4%D0%B6%D0%B8%D0%BA; last_visited_page=http%3A%2F%2Frp5.ru%2F%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%93%D0%B5%D0%BB%D0%B5%D0%BD%D0%B4%D0%B6%D0%B8%D0%BA%D0%B5; lang=ru',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
        }

        response = requests.get('https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%93%D0%B5%D0%BB%D0%B5%D0%BD%D0%B4%D0%B6%D0%B8%D0%BA%D0%B5', cookies=cookies, headers=headers).json()
        # print(response)
        
        products_ids = response.get('body').get('products')
        
        with open('1_products_ids.json', 'w') as file:
            json.dump(products_ids, file, indent=4, ensure_ascii=False)
        
        # print(products_ids)
        
        json_data = {
            'productIds': products_ids,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }

        response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
        
        with open('2_items.json', 'w') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)
            
        # print(len(response.get('body').get('products')))
        
        products_ids_str = ','.join(products_ids)
        
        params = {
            'productIds': products_ids_str,
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
        }

        response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
        
        with open('3_prices.json', 'w') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)
            
        items_prices = {}
        
        material_prices = response.get('body').get('materialPrices')
        
        for item in material_prices:
            item_id = item.get('price').get('productId')
            item_base_price = item.get('price').get('basePrice')
            item_sale_price = item.get('price').get('salePrice')
            item_bonus = item.get('bonusRubles').get('total')
            
            
            items_prices[item_id] = {
                'item_basePrice': item_base_price,
                'item_salePrice': item_sale_price,
                'item_bonus': item_bonus
            }
            
        with open('4_items_prices.json', 'w') as file:
            json.dump(items_prices, file, indent=4, ensure_ascii=False)
            
        

        
        with open('2_items.json') as file:
            products_data = json.load(file)

        with open('4_items_prices.json') as file:
            products_prices = json.load(file)
            
        products_data = products_data.get('body').get('products')
        
        for item in products_data:
            product_id = item.get('productId')
            
            if product_id in products_prices:
                prices = products_prices[product_id]
                
                
            item['item_basePrice'] = prices.get('item_basePrice')
            item['item_salePrice'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')
        telegram_send.send(messages=['##########################'])
        for item in products_data:
            name = item.get('name')
            telegram_send.send(messages=[f'{name}, {item_base_price}-базовая цена, {item_sale_price}-цена со скидкой, {item_bonus}-бонусы'])
        with open('5_result.json', 'w') as file:
            json.dump(products_data, file, indent=4, ensure_ascii=False)
        time.sleep(86400)

def main():
    get_data()
    #get_result()
    
    
if __name__ == '__main__':
    main()
