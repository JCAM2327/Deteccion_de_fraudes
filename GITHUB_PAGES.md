# ⚡ Cómo Habilitar GitHub Pages

Tu sitio de documentación ya está creado. Aquí está cómo publicarlo.

## 3 Pasos para Publicar

### 1️⃣ Push a GitHub

```bash
git add .
git commit -m "docs: GitHub Pages documentation"
git push origin main
```

### 2️⃣ Habilitar GitHub Pages

En tu repositorio de GitHub:

1. Vé a **Settings** → **Pages**
2. En "Branch" selecciona: `main`
3. En "Folder" selecciona: `/ (root)`
   - O: `/docs` si usas la carpeta docs
4. Haz clic en **Save**

### 3️⃣ Espera 1-2 minutos

GitHub generará tu sitio automáticamente.

Tu sitio estará en:
```
https://JCAM2327.github.io/Deteccion_de_fraudes/
```

---

## Estructura de tu Sitio

```
index.md                  → Página Principal
├── getting-started.md    → Inicio Rápido
├── features.md           → Características
├── api-reference.md      → Documentación API
├── examples.md           → Ejemplos de Código
└── installation.md       → Guía de Instalación
```

---

## Personalizaciones Disponibles

### Cambiar Tema

Edita `docs/_config.yml`:

```yml
# Temas disponibles:
# jekyll-theme-slate (actual)
# jekyll-theme-architect
# jekyll-theme-cayman
# jekyll-theme-dinky
# jekyll-theme-hacker
# jekyll-theme-leap-day
# jekyll-theme-merlot
# jekyll-theme-minimal
# jekyll-theme-modernist
# jekyll-theme-primer
# jekyll-theme-slate
# jekyll-theme-tactile
# jekyll-theme-time-machine

theme: jekyll-theme-slate
```

### Agregar Logo

En `docs/_config.yml`:

```yml
logo: https://example.com/logo.png
```

### Personalizar Título

En `docs/_config.yml`:

```yml
title: Mi Proyecto Increíble
description: Una descripción alucinante
```

---

## ¿Qué Ves?

Tu sitio tendrá:

✅ **Página Principal profesional**
✅ **Navegación intuitiva**
✅ **Código resaltado**
✅ **Búsqueda automática**
✅ **SEO optimizado**
✅ **Responsive (funciona en móvil)**
✅ **HTTPS gratis**

---

## Ejemplo de URL Final

```
https://JCAM2327.github.io/Deteccion_de_fraudes/
├── / → Inicio
├── /getting-started.md → Quickstart
├── /features.md → Características
├── /api-reference.md → API
├── /examples.md → Ejemplos
└── /installation.md → Instalación
```

---

## Verificar que Está Activo

Después de 2 minutos:

1. Vé a https://JCAM2327.github.io/Deteccion_de_fraudes/
2. Deberías ver tu sitio

Si no aparece:
- Espera 5 minutos más
- Revisa que `docs/_config.yml` existe
- Verifica que sea un repo público

---

## Actualizar Contenido

Cada vez que hagas push:

```bash
git add docs/
git commit -m "docs: updates"
git push
```

GitHub actualizará automáticamente en 1-2 minutos.

---

## Ideas para Mejorar

Agrega a tu sitio:

- 📸 Screenshots del dashboard
- 🎬 GIFs en acción
- 📊 Gráficos de rendimiento
- 🏆 Badges de GitHub
- 📝 Blog posts
- 🎓 Tutorials
- 👥 Creditos

---

¡Tu documentación profesional está lista! 🎉
