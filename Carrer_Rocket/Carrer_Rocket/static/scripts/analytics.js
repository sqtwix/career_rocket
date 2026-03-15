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

