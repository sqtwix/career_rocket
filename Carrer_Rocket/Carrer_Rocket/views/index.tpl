% rebase('layout.tpl', title='Главная', year=2026)

<link rel="stylesheet" href="/static/content/mainpage.css">

<div class="jumbotronhome">
    <img src="static/images/rocket.png" width="200" height="150">
    <p class="lead">Career Rocket помогает находить работу и стажировку в сфере IT.</p>
    <p><a href="http://bottlepy.org/docs/dev/index.html" class="btnhome btn-primary">Learn more &raquo;</a></p>
</div>

<div class="search">
    <form action="https://tgaijobs.ru/vacancies" method="get" class="search-form" target="_blank">
        <div class="search-input-group">
            <input type="text" name="title" placeholder="Поиск вакансий, стажировок..." class="search-input">
            <button type="submit" class="btnhome btn-default">Найти</button>
        </div>
    </form>
<div class="popular-tagshome">
        <a href="https://tgaijobs.ru/vacancies?title=python" class="tag">Python</a>
        <a href="https://tgaijobs.ru/vacancies?title=JavaScript" class="tag">JavaScript</a>
        <a href="https://tgaijobs.ru/vacancies?employment_type_id=5" class="tag">Стажировка</a>
        <a href="https://tgaijobs.ru/vacancies?title=Frontend" class="tag">Frontend</a>
        <a href="https://tgaijobs.ru/vacancies?title=Backend" class="tag">Backend</a>
    </div>
</div>

<div class="rowhome">
    <div class="containerhome">
        <div class="col-md-4home">
            <h2>Персональный подбор вакансий</h2>
            <p>
                Наш алгоритм анализирует ваш стек технологий 
                (Python, JavaScript, Java, C# и др.), опыт работы и зарплатные ожидания. 
                Мы подбираем релевантные вакансии из базы в 10 000+ предложений, экономя ваше время на поиске.
            </p>
            <ul class="card-list">
                <li>✓ Фильтр по грейду: Junior, Middle, Senior</li>
                <li>✓ Удаленка, гибрид, офис</li>
                <li>✓ Зарплата от 50 000 до 500 000+ ₽</li>
            </ul>
        </div>
        <div class="col-md-4home">
            <h2>Стажировки для начинающих</h2>
            <p>Специальный раздел для джунов и студентов: стажировки с наставником, оплачиваемые практики и позиции Trainee. 
            Многие компании берут кандидатов без коммерческого опыта, но с хорошим портфолио.</p>
            <ul class="card-list">
                <li>✓ Стажировки от 3 до 6 месяцев</li>
                <li>✓ Оплата от 30 000 до 80 000 ₽</li>
                <li>✓ Возможность перехода в штат</li>
            </ul>
        </div>
        <div class="col-md-4home">
            <h2>Вакансии по всей России</h2>
            <p>Работайте в офисе в своем городе или переезжайте в IT-хабы: Москва, Санкт-Петербург, Казань, Новосибирск, Екатеринбург. 
            Многие компании предлагают релокационную поддержку.</p>
            <ul class="card-list">
                <li>✓ Помощь с переездом</li>
                <li>✓ Компенсация аренды жилья</li>
                <li>✓ Города с развитой IT-инфраструктурой</li>
            </ul>
        </div>
    </div>
</div>
