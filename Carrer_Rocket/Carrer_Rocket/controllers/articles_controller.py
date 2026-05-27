from bottle import route, request, redirect, template, view
from services.article_service import ArticleService
from services.validation_service import ValidationError


@route('/articles', method='GET')
@view('articles')
def articles_index():
    start_date = request.query.get('start_date', '')
    end_date = request.query.get('end_date', '')
    
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
        ArticleService.add_new_article(form_data)
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
            title='Статьи',
            year=2026
        )


@route('/articles/filter', method='POST')
def articles_filter():
    start_date = request.forms.get('start_date', '').strip()
    end_date = request.forms.get('end_date', '').strip()
    
    if start_date and end_date:
        redirect(f'/articles/interval?start_date={start_date}&end_date={end_date}')
    elif start_date and not end_date:
        redirect(f'/articles/date/{start_date}')
    else:
        redirect('/articles')