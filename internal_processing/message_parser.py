from server import *
import ast

db = Data_base(db_folder + db_name)

def receive_message(userId, message):
	status = db.get_user_state(userId)
	operacao = ast.literal_eval(db.get_user_dictionary(userId))
	if(('cancelar' in message.split()) or ('cancela' in message.split())):
		db.set_user_dictionary(userId, '')
		db.set_user_state(userId, 'escolha')
		return 'Operação cancelada. O que deseja fazer agora? Digite 1 para transferencia, 2 para saldo, 3 para extrato, 4 para boleto e 5 para receber.'
	elif(status == 'init'):
		return 'Ola! O que gostaria de fazer? Digite 1 para transferencia, 2 para saldo, 3 para extrato, 4 para boleto e 5 para receber.'
	elif(status == 'escolha'):
		if(message == '1'):	
			db.set_user_state(userId, 'transf1')
			operacao['op'] = 'transferencia'
			db.set_user_dictionary(userId, str(operacao))
			return 'Quanto quer mandar?'
		elif(message == '2'):
			db.set_user_state(userId, 'saldo1')
			operacao['op'] = 'saldo'
			db.set_user_dictionary(userId, str(operacao))
		elif(message == '3'):
			db.set_user_state(userId, 'extrato1')
			operacao['op'] = 'extrato'
			db.set_user_dictionary(userId, str(operacao))
			return 'Qual o período que deseja ver?'
		elif(message == '4'):
			db.set_user_state(userId, 'boleto1')
			operacao['op'] = 'boleto'
			db.set_user_dictionary(userId, str(operacao))
			return 'Digite o código do boleto que quer pagar.'
		else:
			db.set_user_state(userId, 'receber1')
			operacao['op'] = 'receber'
			db.set_user_dictionary(userId, str(operacao))
			return 'Quanto quer pedir para o responsável?'
	elif(status == 'transf1'):
		db.set_user_state(userId, 'transf2')
		operacao['valor'] = message
		db.set_user_dictionary(userId, str(operacao))
		return 'Mandar para quem?'
	elif(status == 'transf2'):
		db.set_user_state(userId, 'transf3')
		operacao['destino'] = message
		db.set_user_dictionary(userId, str(operacao))
	elif(status == 'extrato1'):
		db.set_user_state(userId, 'extrato2')
		operacao['periodo'] = message
		db.set_user_dictionary(userId, str(operacao))
	elif(status == 'boleto1'):
		db.set_user_state(userId, 'boleto2')
		operacao['codigo'] = message
		db.set_user_dictionary(userId, str(operacao))
	elif(status == 'receber1'):
		db.set_user_state(userId, 'receber2')
		operacao['valor'] = message
		db.set_user_dictionary(userId, str(operacao))
	elif(status in ['saldo1', 'receber2', 'boleto2', 'transf3', 'extrato2']):
		db.set_user_dictionary(userId, '')
		return operacao

receive_message(1234, 'boleto1')
print(db.users)



# Extrato
# Qual o período que deseja ver?
# 	Op1: Hoje
# 	Op2: Essa semana
# 	Op3: Mes

# Saldo

# Receber
# Quanto quer pedir para o responsável?

# Pagar boleto
# Digite o código do boleto que quer pagar

# Transfeência
# Quanto quer mandar?
# Mandar para quem?
# 	Ops: mostrar cada dependente