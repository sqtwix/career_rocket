% rebase('layout.tpl', title='Актуальные новинки', year=year)

<link rel="stylesheet" href="/static/content/mainpage.css">

<!-- Заголовок страницы -->
<div class="jumbotronhome text-center">
    <h1>Актуальные новинки</h1>
    <p>Свежие IT-события, вакансии и стажировки</p>
</div>

<!-- Список добавленных новинок -->
% if news_list:
    <div class="rowhome">
        % for item in news_list:
            <div class="col-md-4home">
                <div class="news-header">
                    <span class="tag tag-category">{{item['category']}}</span>
                    <span class="news-date">{{item['date']}}</span>
                </div>
                <h3 class="news-title">{{item['title']}}</h3>
                <p class="news-description">{{item['description']}}</p>
            </div>
        % end
    </div>
% else:
<div class="jumbotronhome empty-news">
    <p>Пока нет добавленных новинок. Будьте первым!</p>
</div>
% end

<!-- Форма добавления новой новинки -->
<div class="jumbotronhome form-wrapper">
    <h2>Добавить новинку</h2>
     % if error:
        <div class="alert-error">
            {{!error}}
        </div>
    % end
    <form action="/news" method="post" novalidate accept-charset="UTF-8">
    <div class="form-group">
        <input type="text" name="title" placeholder="Название" value="{{form_data.get('title', '')}}" class="search-input">
    </div>
    
    <div class="form-group form-row">
        <select name="category" required class="tag select-category">
            <option value="">– Категория –</option>
            <option value="Вакансия" {{'selected' if form_data.get('category') == 'Вакансия' else ''}}>Вакансия</option>
            <option value="Стажировка" {{'selected' if form_data.get('category') == 'Стажировка' else ''}}>Стажировка</option>
            <option value="Мероприятие" {{'selected' if form_data.get('category') == 'Мероприятие' else ''}}>Мероприятие</option>
            <option value="Статья/Совет" {{'selected' if form_data.get('category') == 'Статья/Совет' else ''}}>Статья/Совет</option>
            <option value="Новая компания" {{'selected' if form_data.get('category') == 'Новая компания' else ''}}>Новая компания</option>
        </select>
        <input type="date" name="date" value="{{form_data.get('date', '')}}" class="search-input date-input">
    </div>
    
    <div class="form-group">
        <textarea name="description" rows="2" placeholder="Описание" class="search-input">{{form_data.get('description', '')}}</textarea>
    </div>
        <div class="form-group text-center">
            <button type="submit" class="btnhome btn-default">Добавить новинку</button>
        </div>
    </form>
</div>