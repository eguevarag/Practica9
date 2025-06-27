import redis

# Conexión a Redis (asegúrate de que host y puerto coincidan)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Insertar string
r.set('app:mensaje', 'Prueba con Python')
print('String:', r.get('app:mensaje'))

# Crear hash de sesión
session_key = 'session:3003'
r.hset(session_key, mapping={
    'user_id': 3003,
    'username': 'ernesto3',
    'login_time': '2025-06-27 13:30:00',
    'token': 'PYTHON_TOKEN'
})
r.expire(session_key, 1800)

print('Hash:', r.hgetall(session_key))

# Actualizar campo
r.hset(session_key, 'token', 'PYTHON_TOKEN_UPDATED')
print('Hash actualizado:', r.hgetall(session_key))

# Eliminar
r.delete('app:mensaje')
r.delete(session_key)
print('Eliminado.')
