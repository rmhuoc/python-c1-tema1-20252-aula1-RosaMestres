"""
Tests para el ejercicio ej1c1.py
"""

import unittest
from unittest.mock import patch, Mock
import sys
import os
import json

# Añadir el directorio padre al path para importar el módulo
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from 1c.ej1c1 import get_wikipedia_article, extract_article_info, print_article_summary

class TestWikipediaClient(unittest.TestCase):
    
    def setUp(self):
        # Ejemplo de respuesta de la API de Wikipedia
        self.sample_response = {
            "title": "Python (programming language)",
            "description": "High-level programming language",
            "extract": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."
        }
    
    @patch('requests.get')
    def test_get_wikipedia_article_success(self, mock_get):
        # Configurar el mock para simular una respuesta exitosa
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_response
        mock_get.return_value = mock_response
        
        result = get_wikipedia_article("Python_(programming_language)")
        self.assertEqual(result, self.sample_response)
        mock_get.assert_called_once()
    
    @patch('requests.get')
    def test_get_wikipedia_article_failure(self, mock_get):
        # Configurar el mock para simular un error
        mock_get.side_effect = Exception("Error en la conexión")
        
        result = get_wikipedia_article("Python_(programming_language)")
        self.assertIsNone(result)
        mock_get.assert_called_once()
    
    @patch('requests.get')
    def test_get_wikipedia_article_not_found(self, mock_get):
        # Configurar el mock para simular un artículo no encontrado
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = get_wikipedia_article("NonexistentArticle")
        self.assertIsNone(result)
        mock_get.assert_called_once()
    
    def test_extract_article_info_success(self):
        result = extract_article_info(self.sample_response)
        expected = {
            "title": "Python (programming language)",
            "description": "High-level programming language",
            "extract": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."
        }
        self.assertEqual(result, expected)
    
    def test_extract_article_info_none(self):
        result = extract_article_info(None)
        self.assertIsNone(result)
    
    def test_extract_article_info_missing_fields(self):
        incomplete_data = {
            "title": "Python (programming language)"
            # Missing description and extract
        }
        result = extract_article_info(incomplete_data)
        self.assertIsNone(result)
    
    @patch('builtins.print')
    def test_print_article_summary(self, mock_print):
        article_info = {
            "title": "Python (programming language)",
            "description": "High-level programming language",
            "extract": "Python is a high-level, general-purpose programming language."
        }
        print_article_summary(article_info)
        
        # Verificar que se hicieron las llamadas a print con la información correcta
        mock_print.assert_any_call("TÍTULO: Python (programming language)")
        mock_print.assert_any_call("DESCRIPCIÓN: High-level programming language")
        mock_print.assert_any_call("EXTRACTO: Python is a high-level, general-purpose programming language.")
    
    @patch('builtins.print')
    def test_print_article_summary_none(self, mock_print):
        print_article_summary(None)
        mock_print.assert_called_once_with("Error: No se pudo obtener información del artículo.")


if __name__ == '__main__':
    unittest.main()
