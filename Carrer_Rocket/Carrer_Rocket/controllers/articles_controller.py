from bottle import route, request, redirect, template, view
from services.article_service import ArticleService
from services.validation_service import ValidationError


@route('/articles', method='GET')
@view('articles')
def articles_index():
    start_date = request.query.get('start_date', '')
    end_date = request.query.get('end_date', '')
    scroll_to = request.query.get('scroll_to', '')
    
    try:
        if start_date and end_date:
            articles = ArticleService.get_all_articles_by_interval(start_date, end_date)
        elif start_date and not end_date:
            articles = ArticleService.get_all_articles_by_date(start_date)
        else:
            articles = ArticleService.get_all_articles()
    except ValueError:
        articles = ArticleService.get_all_articles()
    
    articles.sort(key=lambda x: x.postDate, reverse=True)
    
    return dict(
        articles=articles,
        errors={},
        form_data={},
        start_date=start_date,
        end_date=end_date,
        scroll_to=scroll_to,
        title='Статьи',
        year=2026
    )


@route('/articles/date/<postDate>', method='GET')
@view('articles')
def articles_by_date(postDate):
    try:
        articles = ArticleService.get_all_articles_by_date(postDate)
    except ValueError:
        articles = ArticleService.get_all_articles()
    
    articles.sort(key=lambda x: x.postDate, reverse=True)
    
    return dict(
        articles=articles,
        errors={},
        form_data={},
        start_date=postDate,
        end_date=postDate,
        scroll_to='',
        title=f'Статьи за {postDate}',
        year=2026
    )


@route('/articles/interval', method='GET')
@view('articles')
def articles_by_interval():
    start_date = request.query.get('start_date', '')
    end_date = request.query.get('end_date', '')
    
    if not start_date or not end_date:
        redirect('/articles')
    
    try:
        articles = ArticleService.get_all_articles_by_interval(start_date, end_date)
    except ValueError:
        articles = ArticleService.get_all_articles()
    
    articles.sort(key=lambda x: x.postDate, reverse=True)
    
    return dict(
        articles=articles,
        errors={},
        form_data={},
        start_date=start_date,
        end_date=end_date,
        scroll_to='',
        title=f'Статьи с {start_date} по {end_date}',
        year=2026
    )


@route('/articles/add', method='POST')
def articles_add():
    form_data = {
        'header': request.forms.get('header', '').strip(),
        'description': request.forms.get('description', '').strip(),
        'author': request.forms.get('author', '').strip(),
        'postDate': request.forms.get('postDate', '').strip(),
        'text': request.forms.get('text', '').strip()
    }
    
    try:
        new_article = ArticleService.add_new_article(form_data)
        articles = ArticleService.get_all_articles()
        articles.sort(key=lambda x: x.postDate, reverse=True)
        
        for idx, article in enumerate(articles):
            if article.header == form_data['header'] and article.postDate == form_data['postDate']:
                redirect(f'/articles?scroll_to=article_{idx}')
                return
        
        redirect('/articles')
    except ValidationError as e:
        articles = ArticleService.get_all_articles()
        articles.sort(key=lambda x: x.postDate, reverse=True)
        return template(
            'articles',
            articles=articles,
            errors=e.errors,
            form_data=form_data,
            start_date='',
            end_date='',
            scroll_to='',
            title='Статьи',
            year=2026
        )


@route('/articles/filter', method='POST')
def articles_filter():
    start_date = request.forms.get('start_date', '').strip()
    end_date = request.forms.get('end_date', '').strip()
    
    if start_date and end_date:
        redirect(f'/articles/interval?start_date={start_date}&end_date={end_date}&scroll_to=articles_list')
    elif start_date and not end_date:
        redirect(f'/articles/date/{start_date}?scroll_to=articles_list')
    else:
        redirect('/articles')