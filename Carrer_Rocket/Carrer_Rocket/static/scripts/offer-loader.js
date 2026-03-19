// offer-loader.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('Скрипт загружен, начинаем загрузку данных...');
    loadOffers();
});

async function loadOffers() {
    try {
        const possiblePaths = [
            '/data/offers.json',
            'data/offers.json',
            './data/offers.json',
            '/static/data/offers.json'
        ];
        
        let data = null;
        let lastError = null;
        
        for (const path of possiblePaths) {
            try {
                console.log(`Пробуем загрузить из: ${path}`);
                const response = await fetch(path);
                
                if (response.ok) {
                    data = await response.json();
                    console.log(`Успешно загружено из: ${path}`);
                    break;
                }
            } catch (e) {
                lastError = e;
                console.log(`Не удалось загрузить из: ${path}`);
            }
        }
        
        if (data) {
            renderOffers(data.offers);
        } else {
            throw lastError || new Error('Не удалось загрузить данные');
        }
        
    } catch (error) {
        console.error('Ошибка загрузки:', error);
        showError();
    }
}

function renderOffers(offers) {
    const container = document.querySelector('.packages-grid');
    
    if (!container) {
        console.error('Контейнер .packages-grid не найден!');
        return;
    }
    
    container.innerHTML = '';
    
    offers.forEach(offer => {
        const card = document.createElement('div');
        card.className = 'package-card' + (offer.popular ? ' popular' : '');
        
        const formattedPrice = offer.price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
        
        let html = `
            <div class="package-header">
                <span class="badge">${offer.badge}</span>
                <div class="package-name">${offer.name}</div>
                <div class="package-price">
                    <span class="price-amount">${formattedPrice}</span>
                    <span class="price-period">${offer.currency} / ${offer.period}</span>
                </div>
            </div>
            <p class="package-description">${offer.description}</p>
            <ul class="features-list">
        `;
        
        offer.features.forEach(feature => {
            html += `<li class="feature-item">${feature}</li>`;
        });
        
        html += `</ul>`;
        
        if (offer.consultation_tag) {
            html += `<div class="consultation-tag">${offer.consultation_tag}</div>`;
        }
        
        html += `<button class="${offer.button_class}">${offer.button_text}</button>`;
        
        card.innerHTML = html;
        container.appendChild(card);
    });
    
    console.log('Карточки успешно отрисованы');
}

function showError() {
    const container = document.querySelector('.packages-grid');
    if (container) {
        container.innerHTML = `
            <div style="grid-column: 1/-1; text-align: center; padding: 40px;">
                <p style="color: #dc3545; margin-bottom: 15px;">Ошибка загрузки данных</p>
                <button onclick="location.reload()" style="background: #2F4454; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;">
                    Обновить страницу
                </button>
            </div>
        `;
    }
}
