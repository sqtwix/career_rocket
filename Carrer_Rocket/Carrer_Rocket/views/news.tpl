<!-- views/news.tpl -->
% rebase('layout.tpl', title='Новости', year=2026)

<link rel="stylesheet" href="/static/content/news.css">

<div class="page-header">
    <h1>Новости индустрии</h1>
    <p>Актуальные события и тренды в мире IT</p>
</div>

<div class="news-container">
    <div class="filter-section">
        <h3>Фильтр по дате</h3>
        <form action="/news/filter" method="POST" class="filter-form">
            <div class="filter-group">
                <label for="start_date">Дата от:</label>
                <input type="date" id="start_date" name="start_date" value="{{start_date}}" class="filter-input">
            </div>
            <div class="filter-group">
                <label for="end_date">Дата до:</label>
                <input type="date" id="end_date" name="end_date" value="{{end_date}}" class="filter-input">
            </div>
            <button type="submit" class="btn-filter">Применить</button>
            <a href="/news" class="btn-reset">Сбросить</a>
        </form>
    </div>
    
    <div class="add-news-section">
        <h2>Добавить новость</h2>
        <form action="/news/add" method="POST" class="news-form">
            <div class="form-group">
                <label for="header">Заголовок</label>
                <input type="text" id="header" name="header" 
                       value="{{form_data.get('header', '')}}"
                       placeholder="Введите заголовок новости" class="form-input">
                % if errors.get('header'):
                    <span class="error-message">{{errors['header']}}</span>
                % end
            </div>
            
            <div class="form-group">
                <label for="description">Краткое описание</label>
                <textarea id="description" name="description" rows="2"
                          placeholder="Краткое описание новости" class="form-textarea">{{form_data.get('description', '')}}</textarea>
                % if errors.get('description'):
                    <span class="error-message">{{errors['description']}}</span>
                % end
            </div>
            
            <div class="form-group">
                <label for="author">Автор</label>
                <input type="text" id="author" name="author" 
                       value="{{form_data.get('author', '')}}"
                       placeholder="Имя автора" class="form-input">
                % if errors.get('author'):
                    <span class="error-message">{{errors['author']}}</span>
                % end
            </div>
            
            <div class="form-group">
                <label for="postDate">Дата публикации</label>
                <input type="date" id="postDate" name="postDate" 
                       value="{{form_data.get('postDate', '')}}" class="form-input">
                % if errors.get('postDate'):
                    <span class="error-message">{{errors['postDate']}}</span>
                % end
            </div>
            
            <div class="form-group">
                <label for="text">Полный текст</label>
                <textarea id="text" name="text" rows="6"
                          placeholder="Текст новости" class="form-textarea">{{form_data.get('text', '')}}</textarea>
                % if errors.get('text'):
                    <span class="error-message">{{errors['text']}}</span>
                % end
            </div>
            
            <button type="submit" class="btn-submit">Разместить новость</button>
        </form>
    </div>
    
    <div class="news-list">
        <h2>Все новости <span class="news-count">({{len(news_list)}})</span></h2>
        
        % if not news_list:
            <div class="no-news">
                <p>Новостей пока нет</p>
                <p>Будьте первым, кто добавит новость!</p>
            </div>
        % else:
            % for news in news_list:
                <div class="news-card">
                    <div class="news-card-header">
                        <h3 class="news-title">{{news.header}}</h3>
                        <div class="news-meta">
                            <span class="news-author">✍️ {{news.author}}</span>
                            <span class="news-date">📅 {{news.postDate}}</span>
                        </div>
                    </div>
                    <div class="news-card-body">
                        <p class="news-description">{{news.description}}</p>
                        <div class="news-divider"></div>
                        <p class="news-text">{{news.text}}</p>
                    </div>
                </div>
            % end
        % end
    </div>
</div>