# Contribuyendo al Proyecto 🤝

¡Gracias por tu interés en contribuir al proyecto de Detección de Fraudes! 

## 📋 Cómo Contribuir

### 1. Reportar Problemas
Si encuentras un bug o tienes una sugerencia:
- Abre un [GitHub Issue](https://github.com/JCAM2327/Deteccion_de_fraudes/issues)
- Describe el problema claramente
- Incluye pasos para reproducirlo

### 2. Proponer Mejoras
- Abre una discusión en Issues
- Describe la mejora propuesta
- Explica el beneficio

### 3. Enviar Pull Requests
```bash
# 1. Fork el repositorio
# 2. Clona tu fork
git clone https://github.com/tu-usuario/Deteccion_de_fraudes.git

# 3. Crea una rama para tu feature
git checkout -b feature/mi-mejora

# 4. Realiza cambios y commit
git add .
git commit -m "feat: descripción clara del cambio"

# 5. Push a tu fork
git push origin feature/mi-mejora

# 6. Abre un Pull Request
```

## 💻 Estándares de Código

### Python
- Usa [PEP 8](https://www.python.org/dev/peps/pep-0008/) para estilo
- Ejecuta `black` antes de commit:
  ```bash
  black src/
  ```
- Ejecuta `flake8` para linting:
  ```bash
  flake8 src/
  ```

### Docstrings
Todas las funciones deben tener docstrings:
```python
def mi_funcion(param1, param2):
    """
    Descripción breve de la función.
    
    Descripción más larga si es necesaria.
    
    Args:
        param1: Descripción del parámetro 1
        param2: Descripción del parámetro 2
        
    Returns:
        Descripción del valor retornado
        
    Example:
        >>> mi_funcion(1, 2)
        resultado
    """
    pass
```

### Commits
- Usa mensajes descriptivos
- Formato: `tipo: descripción`
- Tipos: `feat`, `fix`, `docs`, `refactor`, `test`

Ejemplos:
```
feat: agregar SHAP explainability al modelo
fix: corregir cálculo de ROC-AUC
docs: actualizar README con instrucciones
refactor: simplificar preprocesamiento
test: agregar tests para DataProcessor
```

## 🧪 Testing

Antes de enviar un PR, ejecuta las pruebas:

```bash
# Instalar pytest
pip install pytest

# Ejecutar todas las pruebas
pytest

# Con cobertura
pytest --cov=src
```

## 📝 Documentación

Si realizas cambios importantes:
- Actualiza la documentación correspondiente
- Agrega comentarios al código complejo
- Actualiza el README si corresponde

## 🔍 Proceso de Review

Todo PR será revisado por el mantenedor:
1. Revisión de código
2. Verificación de tests
3. Validación de estándares
4. Feedback y sugerencias



¡Gracias por contribuir! 🎉
