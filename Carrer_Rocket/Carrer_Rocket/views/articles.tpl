% rebase('layout.tpl', title='Статьи', year=2026)

<link rel="stylesheet" href="/static/content/articles.css">

<div class="page-header">
    <h1>Статьи и публикации</h1>
    <p>Полезные материалы о карьере в IT</p>
</div>

<div class="articles-container">
    <div class="filter-section">
        <h3>Фильтр по дате</h3>
        <form action="/articles/filter" method="POST" class="filter-form">
            <div class="filter-group">
                <label for="start_date">Дата от:</label>
                <input type="date" id="start_date" name="start_date" value="{{start_date}}" class="filter-input">
            </div>
            <div class="filter-group">
                <label for="end_date">Дата до:</label>
                <input type="date" id="end_date" name="end_date" value="{{end_date}}" class="filter-input">
            </div>
            <button type="submit" class="btn-filter">Применить</button>
            <a href="/articles" class="btn-reset">Сбросить</a>
        </form>
    </div>
    
    <div class="add-article-section">
        <h2>Добавить статью</h2>
        <form action="/articles/add" method="POST" class="article-form">
            <div class="form-group">
                <label for="header">Заголовок</label>
                <input type="text" id="header" name="header" 
                       value="{{form_data.get('header', '')}}"
                       placeholder="Введите заголовок статьи" class="form-input">
                % if errors.get('header'):
                    <span class="error-message">{{errors['header']}}</span>
                % end
            </div>
            
            <div class="form-group">
                <label for="description">Краткое описание</label>
                <textarea id="description" name="description" rows="2"
                          placeholder="Краткое описание статьи" class="form-textarea">{{form_data.get('description', '')}}</textarea>
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
                <label for="text">Текст статьи</label>
                <textarea id="text" name="text" rows="8"
                          placeholder="Текст статьи" class="form-textarea">{{form_data.get('text', '')}}</textarea>
                % if errors.get('text'):
                    <span class="error-message">{{errors['text']}}</span>
                % end
            </div>
            
            <button type="submit" class="btn-submit">Опубликовать статью</button>
        </form>
    </div>
    
    <div class="articles-list">
        <h2>Все статьи <span class="articles-count">({{len(articles)}})</span></h2>
        
        % if not articles:
            <div class="no-articles">
                <p>Статей пока нет</p>
                <p>Будьте первым, кто опубликует статью!</p>
            </div>
        % else:
            % for article in articles:
                <div class="article-card">
                    <div class="article-card-header">
                        <h3 class="article-title">{{article.header}}</h3>
                        <div class="article-meta">
                            <span class="article-author">{{article.author}}</span>
                            <span class="article-date">{{article.postDate}}</span>
                        </div>
                    </div>
                    <div class="article-card-body">
                        <p class="article-description">{{article.description}}</p>
                        <div class="article-divider"></div>
                        <div class="article-text">
                            <p>{{article.text}}</p>
                        </div>
                    </div>
                </div>
            % end
        % end
    </div>
</div>