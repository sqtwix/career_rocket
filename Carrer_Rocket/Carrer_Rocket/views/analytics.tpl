<!-- Шапка страницы -->
<div class="page-header text-center">
    <div class="container">
        <h1>📊 Аналитика рынка IT</h1>
        <p>Актуальные данные за {{ year }} год • Более 4000 вакансий</p>
    </div>
</div>

<!-- Три окна для отображение самой статистики -->
<div class="container">
    <div class="row">
        <!-- Окно круговой диаграммы-->
        <div class="col-md-6">
            <div class="window window-pie">
                <h2>Распределение вакансий</h2>
                <canvas id="pieChart"></canvas>
            </div>
        </div>

        <!-- Окно cправки по вакансиям -->
        <div class="col-md-6">
            <div class="window window-info">
                <h2>Детали по категориям</h2>
                <div id="categoryList"></div>
            </div>
        </div>
    </div>

    <div class="row">
        <!-- Окно со столбцовой диаграммой -->
        <div class="col-md-12">
            <div class="window window-bar">
                <h2>Средние зарплаты</h2>
                <canvas id="barChart"></canvas>
            </div>
        </div>
    </div>
</div>