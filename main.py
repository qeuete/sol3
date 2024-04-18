from web3 import Web3
from web3.middleware import geth_poa_middleware 
from contractinfo import abi, contract_address


w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_address, abi=abi)

print(f"Баланс первого аккаунта: {w3.eth.get_balance('DA534ad708d035CE9F6D1Ff783b90ad108e093d3')}")
print(f"Баланс второго аккаунта: {w3.eth.get_balance('4170f9CFBa9f2534b6a1D5C84B4b5Af8ED933E7c')}")
print(f"Баланс тртьего аккаунта: {w3.eth.get_balance('b7439618CE139720AE1A39504f5B8a81788D8277')}")
print(f"Баланс четвертого аккаунта: {w3.eth.get_balance('f72E7d3797b882295E7f76127B0bE3Cc2BE43F0b')}")
print(f"Баланс пятого аккаунта: {w3.eth.get_balance('56073811852f896815a02adD85acd310efEcfB5c')}")
