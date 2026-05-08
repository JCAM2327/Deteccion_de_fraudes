<section class="hero">
  <h1>🔍 Sistema Inteligente de Detección de Fraudes</h1>

  <p>
    Plataforma de Machine Learning para detección de fraudes
    financieros utilizando XGBoost, SHAP y Streamlit.
  </p>

  <div class="buttons">
    <a href="#dashboard">Ver Dashboard</a>
    <a href="https://github.com/JCAM2327/Deteccion_de_fraudes">
      GitHub
    </a>
  </div>
</section>

<section>
  <h2>📋 Sobre el Proyecto</h2>

  <p>
    Este proyecto implementa un sistema avanzado de detección
    de fraudes basado en Machine Learning utilizando el dataset
    IEEE Fraud Detection de Kaggle con más de 590 mil transacciones.
  </p>

  <ul>
    <li>XGBoost y Random Forest</li>
    <li>Balanceo de clases con SMOTE</li>
    <li>Explicabilidad con SHAP</li>
    <li>Dashboard interactivo con Streamlit</li>
    <li>Arquitectura modular reutilizable</li>
  </ul>
</section>

<section>
  <h2>⚙️ Tecnologías Utilizadas</h2>

  <div class="tech-grid">

    <div class="card">Python</div>
    <div class="card">Pandas</div>
    <div class="card">Scikit-Learn</div>
    <div class="card">XGBoost</div>
    <div class="card">SHAP</div>
    <div class="card">Streamlit</div>
    <div class="card">Plotly</div>
    <div class="card">Jupyter</div>

  </div>
</section>

<section>
  <h2>🧠 Pipeline de Machine Learning</h2>

  <div class="pipeline">

    <div>EDA</div>
    <div>Preprocesamiento</div>
    <div>Feature Engineering</div>
    <div>SMOTE</div>
    <div>Entrenamiento</div>
    <div>SHAP</div>
    <div>Dashboard</div>

  </div>
</section>

<section>
  <h2>📊 Resultados del Modelo</h2>

  <div class="metrics">

    <div class="metric">
      <h3>92%</h3>
      <p>Precision</p>
    </div>

    <div class="metric">
      <h3>87%</h3>
      <p>Recall</p>
    </div>

    <div class="metric">
      <h3>0.92</h3>
      <p>ROC-AUC</p>
    </div>

    <div class="metric">
      <h3>98%</h3>
      <p>Especificidad</p>
    </div>

  </div>
</section>

<section id="dashboard">
  <h2>🚀 Dashboard Interactivo</h2>

  <p>
    El sistema incluye un dashboard desarrollado con Streamlit
    para monitoreo, predicción y análisis de fraudes en tiempo real.
  </p>

  <img src="assets/dashboard.png" alt="Dashboard">

</section>

<section>
  <h2>🔍 Explicabilidad con SHAP</h2>

  <p>
    Se implementaron SHAP values para interpretar las predicciones
    del modelo y comprender el impacto de cada característica.
  </p>

  <img src="assets/shap_summary.png">
</section>

<section>
  <h2>📁 Arquitectura Modular</h2>

<pre>
src/
├── preprocessing.py
├── model.py
└── explainability.py
</pre>

</section>

<section>
  <h2>🛠️ Instalación</h2>

<pre>
git clone https://github.com/JCAM2327/Deteccion_de_fraudes.git

cd Deteccion_de_fraudes

pip install -r requirements.txt

streamlit run dashboard/app.py
</pre>

</section>

<footer>
  <p>
    Desarrollado por JCAM2327 • Machine Learning • Data Science
  </p>
</footer>