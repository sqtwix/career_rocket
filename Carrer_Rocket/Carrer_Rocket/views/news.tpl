% rebase('layout.tpl', title='Актуальные новинки', year=year)

<link rel="stylesheet" href="/static/content/mainpage.css">

<!-- Заголовок страницы -->
<div class="jumbotronhome text-center">
    <h1>Актуальные новинки</h1>
    <p>Свежие IT-события, вакансии и стажировки</p>
</div>

<!-- Список добавленных новинок -->
<div class="jumbotronhome empty-news">
    <p>Пока нет добавленных новинок. Будьте первым!</p>
</div>

<!-- Форма добавления новой новинки -->
<div class="jumbotronhome form-wrapper">
    <h2>Добавить новинку</h2>
    <div class="form-group">
            <input type="text" name="title" placeholder="Название" required class="search-input">
    </div>
    <form action="/news" method="post">
        <div class="form-group form-row">
            <select name="category" required class="tag select-category">
                <option value="">Категория</option>
                <option>Вакансия</option>
                <option>Стажировка</option>
                <option>Мероприятие</option>
                <option>Статья/Совет</option>
                <option>Новая компания</option>
            </select>
            <input type="date" name="date" required class="search-input date-input">
        </div>
        <div class="form-group form-new">
            <input type="text" name="description" placeholder="Описание" required class="search-input">
        </div>
        <div class="form-group text-center">
            <button type="submit" class="btnhome btn-default">Добавить новинку</button>
        </div>
    </form>
</div>