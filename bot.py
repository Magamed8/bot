from pybit.unified_trading import HTTP

session = HTTP(api_key="", api_secret="")
try:
    response = session.get_wallet_balance(accountType="UNIFIED", coin="USDT")

    if response['retCode'] == 0:
        result = response['result']['list'][0]
        print(f"Общая сумма активов: {result['totalEquity']} USDT")
        print(f"Тип аккаунта: {result['accountType']}")
        print(f"Доступный баланс: {result['totalAvailableBalance']} USDT")
        print(f"Баланс на кошельке: {result['totalWalletBalance']} USDT")
    
        coin_info = result['coin'][0]
        print(f"\nИнформация по монете {coin_info['coin']}:")
        print(f"  - Доступно для вывода: {coin_info['availableToWithdraw']} USDT")
        print(f"  - Эквити: {coin_info['equity']} USDT")
    else:
        print("Ошибка:", response['retMsg'])

except Exception as e:
    print("Ошибка при получении баланса:", e)
