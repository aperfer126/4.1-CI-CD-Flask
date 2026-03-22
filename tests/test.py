import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de prueba usando la aplicación Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Envía una solicitud GET a la ruta '/'
        result = self.app.get('/')
        
        # Verifica que la respuesta sea "Hello, World!"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello, World!")

    def test_health(self):
        # Envía una solicitud GET a la ruta '/health'
        result = self.app.get('/health')

        # Verifica que la respuesta sea "Healthy"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Healthy")

    def test_not_found(self):
        # Envía una solicitud GET a una ruta inexistente
        result = self.app.get('/non_existent_route')

        # Verifica que el código de estado sea 404
        self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()