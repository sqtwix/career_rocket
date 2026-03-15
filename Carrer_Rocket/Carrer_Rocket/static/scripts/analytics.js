// Логика страницы analytic.js

// Ждем загрузки DOM, проверка что страница загрузилась 
// и вызов всех методов для отображения графиков
document.addEventListener('DOMContentLoaded', function () {
    console.log('Analytics page loaded');

    // Проверка загрузки даннных из метода analytics в routes.py
    if (!window.categoriesData || !window.salariesData) {
        console.log("ERROR. Данные из json файлов не загружены");
        return;
    }

    // Создание всех графиков и заполнение иных данных
    createPieChart(window.categoriesData);
    createBarChart(window.salariesData);
    populateCategoryList(window.salariesData);
});

// Метод создания круговой диаграммы 
function createPieChart(data) {
    const ctx = document.getElementById('pieChart')?.getContext('2d');
    if(!ctx) return;

    const colors = ['#4361ee', '#3f37c9', '#4cc9f0', '#f72585', '#f8961e',
        '#90be6d', '#577590', '#7209b7', '#b5838d', '#2d9cdb'];

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: data.categories.map(c => c.name),
            datasets: [{
                data: data.categories.map(c => c.count),
                backgroundColor: colors.slice(0, data.categories.length),
                borderWidth: 2,
                borderColor: 'white'
            }]
        },
        options: {
            responsive: true,
           // maintainAspectRatio: false,
            plugins: {
                legend: { position: 'right' },
                tooltip: {
                    callbacks: {
                        label: (ctx) => {
                            const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                            const percent = ((ctx.raw / total) * 100).toFixed(1);
                            return `${ctx.label}: ${ctx.raw} вакансий (${percent}%)`;
                        }
                    }
                }
            }
        }
    });
}

// Метод отображения информации по каждой категории
function populateCategoryList(data) {
    const list = document.getElementById('categoryList');
    if (!list) {
        console.error('Элемент categoryList не найден');
        return;
    }

    list.innerHTML = data.salaries.map(item => `
        <div class="category-item">
            <div class="category-name">${item.category}</div>
            <div class="category-stats">
                <span><i class="fas fa-users"></i> ${item.candidates.toLocaleString()} соиск.</span>
                <span><i class="fas fa-building"></i> ${item.employers.toLocaleString()} работ.</span>
            </div>
            <div class="salary-range">
                <span class="salary-badge badge-min">${item.min.toLocaleString()} ₽</span>
                <span class="salary-badge badge-avg">${item.avg.toLocaleString()} ₽</span>
                <span class="salary-badge badge-max">${item.max.toLocaleString()} ₽</span>
            </div>
            <div class="salary-bar">
                <div class="salary-fill" style="width: ${(item.min / item.max) * 100}%"></div>
            </div>
        </div>
    `).join('');

    console.log('Cписок категорий заполнен');
}

// Метод для создания столбцатой диаграммы
function createBarChart(data) {
    const ctx = document.getElementById('barChart')?.getContext('2d');
    if (!ctx) return;


    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.salaries.map(s => s.category),
            datasets: [
                {
                    label: 'Мин',
                    data: data.salaries.map(s => s.min),
                    backgroundColor: '#e3f2fd',
                    borderColor: '#0d47a1',
                    borderWidth: 1
                },
                {
                    label: 'Средняя',
                    data: data.salaries.map(s => s.avg),
                    backgroundColor: '#4361ee',
                    borderColor: '#3f37c9',
                    borderWidth: 1
                },
                {
                    label: 'Макс',
                    data: data.salaries.map(s => s.max),
                    backgroundColor: '#fff3e0',
                    borderColor: '#e65100',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                tooltip: {
                    callbacks: {
                        label: (ctx) => `${ctx.dataset.label}: ${ctx.raw.toLocaleString()} ₽`
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: (v) => v.toLocaleString() + ' ₽'
                    }
                }
            }
        }
    });
}



