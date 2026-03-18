%rebase('layout.tpl', title='Пакеты услуг - Career Rocket')

{{!offers_store_styles.tpl}}

<div class="offers-container">
    <div class="offers-header">
        <h1>Найди работу своей мечты в IT</h1>
        <p>Индивидуальный подход, персональные консультации и помощь в трудоустройстве</p>
    </div>

    <div class="packages-grid">
        <!-- Базовый пакет -->
        <div class="package-card">
            <div class="package-header">
                <span class="badge">Старт</span>
                <div class="package-name">Базовый</div>
                <div class="package-price">
                    <span class="price-amount">5 900</span>
                    <span class="price-period">₽ / месяц</span>
                </div>
            </div>
            <p class="package-description">Первые шаги в IT: подбор вакансий и базовая поддержка</p>
            <ul class="features-list">
                <li class="feature-item">Подбор 10 вакансий в неделю</li>
                <li class="feature-item">Шаблоны резюме и сопроводительных</li>
                <li class="feature-item">Чат поддержки (ответ 24ч)</li>
                <li class="feature-item">Личные консультации</li>
                <li class="feature-item">Разбор собеседований</li>
            </ul>
            <button class="btn">Выбрать пакет</button>
        </div>

        <!-- Оптимальный пакет (популярный) -->
        <div class="package-card popular">
            <div class="popular-badge">Самый популярный</div>
            <div class="package-header">
                <span class="badge" style="background: rgba(226, 133, 46, 0.2); border-color: #E2852E; color: #E2852E;">Рекомендуем</span>
                <div class="package-name">Оптимальный</div>
                <div class="package-price">
                    <span class="price-amount">12 900</span>
                    <span class="price-period">₽ / месяц</span>
                </div>
            </div>
            <p class="package-description">Индивидуальный подход и активная помощь в трудоустройстве</p>
            <ul class="features-list">
                <li class="feature-item">Подбор 20+ вакансий в неделю</li>
                <li class="feature-item">Персональная доработка резюме</li>
                <li class="feature-item">2 личные консультации в месяц</li>
                <li class="feature-item">Подготовка к собеседованиям</li>
                <li class="feature-item">Сопровождение на всех этапах</li>
            </ul>
            <div class="consultation-tag">Чат с экспертом 24/7</div>
            <button class="btn btn-primary">Выбрать пакет</button>
        </div>

        <!-- Премиум пакет -->
        <div class="package-card">
            <div class="package-header">
                <span class="badge">VIP</span>
                <div class="package-name">Премиум</div>
                <div class="package-price">
                    <span class="price-amount">24 900</span>
                    <span class="price-period">₽ / месяц</span>
                </div>
            </div>
            <p class="package-description">Полное сопровождение до оффера и поддержка на испытательном сроке</p>
            <ul class="features-list">
                <li class="feature-item">Индивидуальный подбор вакансий</li>
                <li class="feature-item">Личный карьерный консультант</li>
                <li class="feature-item">Еженедельные встречи 1 на 1</li>
                <li class="feature-item">Сопровождение до подписания оффера</li>
                <li class="feature-item">Поддержка на испытательном сроке</li>
            </ul>
            <div class="consultation-tag" style="border-color: #ABE0F0; color: #ABE0F0;">Приоритетная поддержка 24/7</div>
            <button class="btn">Выбрать пакет</button>
        </div>
    </div>
</div>
